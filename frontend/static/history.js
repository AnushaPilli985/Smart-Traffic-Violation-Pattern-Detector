// Detection History Page JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const historyList = document.getElementById('historyList');

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
                <div class="history-media">
                    ${getMediaElement(entry.file_url, entry.filename)}
                </div>
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

    // Handle delete history entry
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('delete-btn')) {
            const timestamp = e.target.getAttribute('data-timestamp');
            if (confirm('Are you sure you want to delete this history entry?')) {
                deleteHistoryEntry(timestamp);
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