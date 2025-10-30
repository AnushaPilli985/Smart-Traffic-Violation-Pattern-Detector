document.getElementById("videoInput").addEventListener("change", function(event) {
    const file = event.target.files[0];
    if (file) {
        const videoPlayer = document.getElementById("videoPlayer");
        videoPlayer.src = URL.createObjectURL(file);
        videoPlayer.load();
        displayCaptions();
    }
});

function displayCaptions() {
    const captions = [
        { time: 2, text: "Welcome to the video." },
        { time: 5, text: "This is an accessible video with sign language." },
        { time: 10, text: "Captions help improve understanding." }
    ];

    const video = document.getElementById("videoPlayer");
    const captionsText = document.getElementById("captionsText");

    video.addEventListener("timeupdate", function() {
        const currentTime = video.currentTime;
        const caption = captions.find(c => Math.floor(currentTime) === c.time);
        if (caption) {
            captionsText.innerText = caption.text;
        }
    });
}