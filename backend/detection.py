import cv2
import numpy as np
from ultralytics import YOLO
import os
def boxes_overlap(box1, box2, threshold=0.2):
    """
    Check if two bounding boxes overlap significantly
    box1, box2: [x1, y1, x2, y2]
    Adjusted threshold for better accuracy
    """
    # Calculate intersection
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    if x2 <= x1 or y2 <= y1:
        return False

    intersection_area = (x2 - x1) * (y2 - y1)

    # Calculate union
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    union_area = box1_area + box2_area - intersection_area

    # Calculate IoU
    iou = intersection_area / union_area if union_area > 0 else 0

    return iou > threshold

def is_valid_motorcycle(bbox, image_shape):
    """
    Validate motorcycle detection based on size and aspect ratio
    """
    x1, y1, x2, y2 = bbox
    width = x2 - x1
    height = y2 - y1

    # Check minimum size (motorcycle should be reasonably large)
    min_area = image_shape[0] * image_shape[1] * 0.001  # 0.1% of image area
    area = width * height
    if area < min_area:
        return False

    # Check aspect ratio (motorcycles are typically wider than tall)
    aspect_ratio = width / height if height > 0 else 0
    if aspect_ratio < 0.5 or aspect_ratio > 4.0:  # Reasonable range for motorcycles
        return False

    return True

def helmet_associated_with_person(helmet_box, person_box):
    """
    Check if helmet is associated with person by checking overlap and proximity
    """
    # First check IoU
    if boxes_overlap(helmet_box, person_box, threshold=0.1):
        return True

    # If no overlap, check if helmet is near the head area (upper 60% of person)
    helmet_center_x = (helmet_box[0] + helmet_box[2]) / 2
    helmet_center_y = (helmet_box[1] + helmet_box[3]) / 2

    person_x1, person_y1, person_x2, person_y2 = person_box

    # Check if helmet center is within expanded person box (10% margin)
    margin_x = (person_x2 - person_x1) * 0.1
    margin_y = (person_y2 - person_y1) * 0.1

    expanded_x1 = person_x1 - margin_x
    expanded_x2 = person_x2 + margin_x
    expanded_y1 = person_y1 - margin_y
    expanded_y2 = person_y2 + margin_y

    if helmet_center_x < expanded_x1 or helmet_center_x > expanded_x2:
        return False
    if helmet_center_y < expanded_y1 or helmet_center_y > expanded_y2:
        return False

    # Check if helmet is in the upper 60% of the person (head and shoulder area)
    person_height = person_y2 - person_y1
    upper_area_y = person_y1 + person_height * 0.6

    return helmet_center_y < upper_area_y

# Load YOLO model (assuming you have a trained model)
MODEL_PATH = '../database/yolov8n.pt'  # Update this path to your trained model

def load_model():
    if os.path.exists(MODEL_PATH):
        return YOLO(MODEL_PATH)
    else:
        # Fallback to a pre-trained model if available
        return YOLO('yolov8n.pt')  # You should replace this with your custom model

# Add debug logging
import logging
logging.basicConfig(level=logging.INFO)

model = load_model()

def detect_violations(image_path):
    """
    Detect violations in the given image/video
    Returns: dict with detection results
    """
    # Read image
    image = cv2.imread(image_path)
    if image is None:
        return {'error': 'Could not read image'}

    # Perform detection
    results = model(image)

    violations = []
    motorcycle_count = 0
    person_count = 0
    vehicle_types = []
    motorcycle_boxes = []
    person_boxes = []
    helmet_boxes = []

    # Process results
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            class_name = model.names[cls]
            bbox = box.xyxy[0].cpu().numpy()  # Get bounding box coordinates

            logging.info(f"Detected: {class_name} with confidence {conf:.2f} at {bbox}")

            if conf > 0.4:  # Lower threshold for better detection
                if class_name.lower() == 'motorcycle':
                    motorcycle_count += 1
                    vehicle_types.append('motorcycle')
                    motorcycle_boxes.append(bbox)
                    logging.info(f"Motorcycle detected: {bbox}")
                elif class_name.lower() in ['car', 'truck', 'bus']:
                    vehicle_types.append(class_name.lower())
                elif class_name.lower() == 'person' and conf > 0.5:  # Higher threshold for persons to avoid false positives
                    person_count += 1
                    person_boxes.append(bbox)
                    logging.info(f"Person detected: {bbox}")
            if class_name.lower() == 'helmet' and conf > 0.4:  # Adjusted threshold for helmets
                helmet_boxes.append(bbox)
                logging.info(f"Helmet detected: {bbox} with confidence {conf:.2f}")

    # Check for violations: persons without helmets
    persons_without_helmet = 0
    for person_box in person_boxes:
        has_helmet = False
        for helmet_box in helmet_boxes:
            if helmet_associated_with_person(helmet_box, person_box):
                has_helmet = True
                logging.info(f"Helmet found for person at {person_box}")
                break
        if not has_helmet:
            persons_without_helmet += 1
            violations.append({
                'type': 'no_helmet',
                'confidence': 0.9,  # Higher confidence for violation detection
                'message': 'Person detected without helmet'
            })
            logging.info(f"No helmet violation detected for person at {person_box}")

    # Also check motorcycles without helmets (for cases where person is not detected but motorcycle is)
    # Use IoU for motorcycle-helmet association since no person box
    for motorcycle_box in motorcycle_boxes:
        has_helmet = False
        for helmet_box in helmet_boxes:
            if boxes_overlap(motorcycle_box, helmet_box, threshold=0.05):  # Lower threshold for motorcycle
                has_helmet = True
                break
        if not has_helmet:
            violations.append({
                'type': 'no_helmet',
                'confidence': 0.7,  # Lower confidence since no person detected
                'message': 'Motorcycle detected without helmet'
            })

    # Determine if violation occurred
    has_violation = len(violations) > 0

    return {
        'violations': violations,
        'motorcycle_count': motorcycle_count,
        'person_count': person_count,
        'persons_without_helmet': persons_without_helmet,
        'vehicle_types': list(set(vehicle_types)),
        'has_violation': has_violation,
        'alert_message': 'Violation detected!' if has_violation else 'No violations detected'
    }

def detect_video_violations(video_path):
    """
    Detect violations in video by processing frames
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return {'error': 'Could not open video'}

    violations = []
    total_motorcycle_count = 0
    total_person_count = 0
    total_persons_without_helmet = 0
    all_vehicle_types = set()
    frame_count = 0
    process_every_n_frames = 30  # Process every 30th frame to speed up

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % process_every_n_frames != 0:
            continue

        # Perform detection on frame
        results = model(frame)

        motorcycle_count = 0
        person_count = 0
        vehicle_types = []
        motorcycle_boxes = []
        person_boxes = []
        helmet_boxes = []

        # Process results
        for result in results:
            boxes = result.boxes
            for box in boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                class_name = model.names[cls]
                bbox = box.xyxy[0].cpu().numpy()

                if conf > 0.3:  # Even lower threshold for motorcycles
                    if class_name.lower() == 'motorcycle' and conf > 0.35:  # Specific threshold for motorcycles
                        if is_valid_motorcycle(bbox, frame.shape):
                            motorcycle_count += 1
                            vehicle_types.append('motorcycle')
                            motorcycle_boxes.append(bbox)
                    elif class_name.lower() in ['car', 'truck', 'bus']:
                        vehicle_types.append(class_name.lower())
                    elif class_name.lower() == 'person' and conf > 0.5:  # Higher threshold for persons to avoid false positives
                        person_count += 1
                        person_boxes.append(bbox)
                if class_name.lower() == 'helmet' and conf > 0.4:  # Adjusted threshold for helmets
                    helmet_boxes.append(bbox)

        # Check for violations: persons without helmets
        persons_without_helmet = 0
        for person_box in person_boxes:
            has_helmet = False
            for helmet_box in helmet_boxes:
                if helmet_associated_with_person(helmet_box, person_box):
                    has_helmet = True
                    break
            if not has_helmet:
                persons_without_helmet += 1
                violations.append({
                    'type': 'no_helmet',
                    'confidence': 0.9,
                    'message': f'Person detected without helmet at frame {frame_count}'
                })

        # Also check motorcycles without helmets
        for motorcycle_box in motorcycle_boxes:
            has_helmet = False
            for helmet_box in helmet_boxes:
                if boxes_overlap(motorcycle_box, helmet_box, threshold=0.05):
                    has_helmet = True
                    break
            if not has_helmet:
                violations.append({
                    'type': 'no_helmet',
                    'confidence': 0.7,
                    'message': f'Motorcycle detected without helmet at frame {frame_count}'
                })

        total_motorcycle_count += motorcycle_count
        total_person_count += person_count
        total_persons_without_helmet += persons_without_helmet
        all_vehicle_types.update(vehicle_types)

    cap.release()

    has_violation = len(violations) > 0

    return {
        'violations': violations,
        'motorcycle_count': total_motorcycle_count,
        'person_count': total_person_count,
        'persons_without_helmet': total_persons_without_helmet,
        'vehicle_types': list(all_vehicle_types),
        'has_violation': has_violation,
        'alert_message': 'Violation detected!' if has_violation else 'No violations detected'
    }