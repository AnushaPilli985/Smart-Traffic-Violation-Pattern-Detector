import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import json
from datetime import datetime
from detection import detect_violations, detect_video_violations



# Get the absolute path to the backend directory
backend_dir = os.path.dirname(os.path.abspath(__file__))
frontend_dir = os.path.join(os.path.dirname(backend_dir), 'frontend')

app = Flask(__name__,
            template_folder=os.path.join(frontend_dir, 'templates'),
            static_folder=os.path.join(frontend_dir, 'static'))
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(backend_dir), 'database', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
HISTORY_FILE = os.path.join(os.path.dirname(backend_dir), 'database', 'history.json')

# Load history
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

# Save history
def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2, default=str)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history-page')
def history_page():
    return render_template('history.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Determine if it's a video or image
        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext in ['.mp4', '.avi', '.mov', '.mkv']:
            # Video processing
            results = detect_video_violations(filepath)
        else:
            # Image processing
            results = detect_violations(filepath)

        # Add file URL to results
        results['file_url'] = f'/uploads/{file.filename}'
        results['timestamp'] = datetime.now().isoformat()

        # Save to history
        history = load_history()
        history_entry = {
            'filename': file.filename,
            'file_url': results['file_url'],
            'timestamp': results['timestamp'],
            'results': results
        }
        history.append(history_entry)  # Add to end (chronological order)
        # Keep only last 10 entries
        history = history[-10:]
        save_history(history)

        return jsonify(results)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/history')
def get_history():
    history = load_history()
    return jsonify(history)

@app.route('/delete_history/<timestamp>', methods=['DELETE'])
def delete_history_entry(timestamp):
    history = load_history()
    # Find and remove the entry with matching timestamp
    history = [entry for entry in history if entry['timestamp'] != timestamp]
    save_history(history)
    return jsonify({'message': 'History entry deleted successfully'})

if __name__ == '__main__':

    app.run(debug=True)

