// Smart Traffic Violation Detection System JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const fileInput = document.getElementById('fileInput');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    const alertMessage = document.getElementById('alertMessage');
    const motorcycleCount = document.getElementById('motorcycleCount');
    const vehicleTypes = document.getElementById('vehicleTypes');
    const violationsList = document.getElementById('violationsList');
    const historyList = document.getElementById('historyList');

    // Update file input label
    fileInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            const label = e.target.nextElementSibling;
            label.textContent = file.name;
        }
    });

    // Handle form submission
    uploadForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData();
        const file = fileInput.files[0];

        if (!file) {
            showAlert('Please select a file first.', 'warning');
            return;
        }

        formData.append('file', file);

        // Show loading
        loading.style.display = 'block';
        results.style.display = 'none';

        // Remove any existing file display
        const container = results.parentNode;
        const existingFileDisplay = container.querySelector('.file-display');
        if (existingFileDisplay) {
            existingFileDisplay.remove();
        }

        // Send request
        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            loading.style.display = 'none';
            results.style.display = 'block';

            displayResults(data);
        })
        .catch(error => {
            loading.style.display = 'none';
            console.error('Error:', error);
            showAlert('An error occurred while processing the file.', 'danger');
        });
    });

    function displayResults(data) {
        // Clear previous results
        violationsList.innerHTML = '';

        // Display alert message
        if (data.has_violation) {
            alertMessage.className = 'alert danger';
            alertMessage.textContent = data.alert_message;
            speakAlert(data.alert_message);
        } else {
            alertMessage.className = 'alert success';
            alertMessage.textContent = data.alert_message;
        }

        // Display stats
        motorcycleCount.textContent = data.motorcycle_count || 0;
        vehicleTypes.textContent = data.vehicle_types.length > 0 ?
            data.vehicle_types.join(', ') : 'None detected';


        // Display violations
        if (data.violations && data.violations.length > 0) {
            data.violations.forEach(violation => {
                const violationItem = document.createElement('div');
                violationItem.className = 'violation-item';
                violationItem.innerHTML = `
                    <h4>${violation.type.replace('_', ' ').toUpperCase()}</h4>
                    <p>${violation.message}</p>
                    <small>Confidence: ${(violation.confidence * 100).toFixed(1)}%</small>
                `;
                violationsList.appendChild(violationItem);
            });
        }

        // Remove any existing file display
        const existingFileDisplay = results.querySelector('.file-display');
        if (existingFileDisplay) {
            existingFileDisplay.remove();
        }

        // Display uploaded file
        if (data.file_url) {
            const fileDisplay = document.createElement('div');
            fileDisplay.className = 'file-display';
            const fileName = data.file_url.split('/').pop();
            const fileExt = fileName.split('.').pop().toLowerCase();

            if (['jpg', 'jpeg', 'png', 'gif', 'bmp'].includes(fileExt)) {
                // Display image
                fileDisplay.innerHTML = `
                    <h3>Uploaded Image</h3>
                    <img src="${data.file_url}" alt="Uploaded Image" class="uploaded-media">
                `;
            } else if (['mp4', 'avi', 'mov', 'mkv', 'webm'].includes(fileExt)) {
                // Display video
                fileDisplay.innerHTML = `
                    <h3>Uploaded Video</h3>
                    <video controls class="uploaded-media">
                        <source src="${data.file_url}" type="video/${fileExt === 'mkv' ? 'x-matroska' : fileExt}">
                        Your browser does not support the video tag.
                    </video>
                `;
            } else {
                // Fallback to link for other file types
                fileDisplay.innerHTML = `
                    <h3>Uploaded File</h3>
                    <a href="${data.file_url}" target="_blank" class="btn btn-secondary">View File</a>
                `;
            }
            // Insert file display after results but before history
            const historySection = document.getElementById('history');
            results.parentNode.insertBefore(fileDisplay, historySection);
        }
    }

    function showAlert(message, type) {
        alertMessage.className = `alert ${type}`;
        alertMessage.textContent = message;
        results.style.display = 'block';
    }

    // Load history on page load
    loadHistory();

    function loadHistory() {
        fetch('/history')
            .then(response => response.json())
            .then(data => {
                displayHistory(data);
            })
            .catch(error => {
                console.error('Error loading history:', error);
            });
    }

    function displayHistory(history) {
        historyList.innerHTML = '';

        if (history.length === 0) {
            historyList.innerHTML = '<p class="no-history">No detection history yet.</p>';
            return;
        }

        // Sort history by timestamp descending (newest first)
        history = history.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));

        history.forEach(entry => {
            const historyItem = document.createElement('div');
            historyItem.className = 'history-item';

            const timestamp = new Date(entry.timestamp).toLocaleString();
            const results = entry.results;

            historyItem.innerHTML = `
                <div class="history-header">
                    <span class="filename">${entry.filename}</span>
                    <span class="timestamp">${timestamp}</span>
                    <button class="btn btn-danger btn-sm delete-btn" data-timestamp="${entry.timestamp}">Delete</button>
                </div>
                <div class="history-media collapsed">
                    <button class="toggle-media-btn">Click to View Detection Details</button>
                    <div class="media-content" style="display: none;">
                        ${getMediaElement(entry.file_url, entry.filename)}
                        <div class="history-stats">
                            <div class="stat">
                                <span class="stat-label">Motorcycles:</span>
                                <span class="stat-value">${results.motorcycle_count || 0}</span>
                            </div>
                            <div class="stat">
                                <span class="stat-label">Vehicles:</span>
                                <span class="stat-value">${results.vehicle_types ? results.vehicle_types.join(', ') : 'None'}</span>
                            </div>
                            <div class="stat">
                                <span class="stat-label">Status:</span>
                                <span class="stat-value ${results.has_violation ? 'violation' : 'no-violation'}">
                                    ${results.has_violation ? 'Violation Detected' : 'No Violations'}
                                </span>
                            </div>
                        </div>
                        ${results.violations && results.violations.length > 0 ? `
                            <div class="history-violations">
                                <h4>Violations:</h4>
                                <ul>
                                    ${results.violations.map(v => `<li>${v.message}</li>`).join('')}
                                </ul>
                            </div>
                        ` : ''}
                    </div>
                </div>
            `;

            historyList.appendChild(historyItem);
        });
    }

    function getMediaElement(fileUrl, filename) {
        const fileExt = filename.split('.').pop().toLowerCase();

        if (['jpg', 'jpeg', 'png', 'gif', 'bmp'].includes(fileExt)) {
            return `<img src="${fileUrl}" alt="Detection result" class="history-media-item">`;
        } else if (['mp4', 'avi', 'mov', 'mkv', 'webm'].includes(fileExt)) {
            return `<video controls class="history-media-item">
                        <source src="${fileUrl}" type="video/${fileExt === 'mkv' ? 'x-matroska' : fileExt}">
                        Your browser does not support the video tag.
                    </video>`;
        } else {
            return `<a href="${fileUrl}" target="_blank" class="btn btn-secondary">View File</a>`;
        }
    }

    function speakAlert(message) {
        // Check if speech synthesis is supported
        if ('speechSynthesis' in window) {
            const utterance = new SpeechSynthesisUtterance(message);
            utterance.rate = 0.8;
            utterance.pitch = 1;
            utterance.volume = 0.8;

            // Use a more urgent voice for violations
            const voices = speechSynthesis.getVoices();
            const urgentVoice = voices.find(voice =>
                voice.name.toLowerCase().includes('female') ||
                voice.name.toLowerCase().includes('zira')
            );

            if (urgentVoice) {
                utterance.voice = urgentVoice;
            }

            speechSynthesis.speak(utterance);
        }
    }

    // Load voices when available
    if ('speechSynthesis' in window) {
        speechSynthesis.onvoiceschanged = function() {
            // Voices loaded
        };
    }

    // Handle delete history entry and toggle media
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('delete-btn')) {
            const timestamp = e.target.getAttribute('data-timestamp');
            if (confirm('Are you sure you want to delete this history entry?')) {
                deleteHistoryEntry(timestamp);
            }
        } else if (e.target.classList.contains('toggle-media-btn')) {
            const mediaDiv = e.target.closest('.history-media');
            const mediaContent = mediaDiv.querySelector('.media-content');
            const isCollapsed = mediaDiv.classList.contains('collapsed');

            if (isCollapsed) {
                mediaContent.style.display = 'block';
                e.target.textContent = 'Hide Detection Details';
                mediaDiv.classList.remove('collapsed');
                mediaDiv.classList.add('expanded');
            } else {
                mediaContent.style.display = 'none';
                e.target.textContent = 'Click to View Detection Details';
                mediaDiv.classList.remove('expanded');
                mediaDiv.classList.add('collapsed');
            }
        }
    });

    function deleteHistoryEntry(timestamp) {
        fetch(`/delete_history/${timestamp}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            // Reload history after deletion
            loadHistory();
        })
        .catch(error => {
            console.error('Error deleting history entry:', error);
            alert('Failed to delete history entry. Please try again.');
        });
    }
});