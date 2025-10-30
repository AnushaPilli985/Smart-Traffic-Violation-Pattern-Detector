document.addEventListener("DOMContentLoaded", function () {
    // Get references to UI elements
    const videoElement = document.getElementById("videoPlayer");
    const convertBtn = document.getElementById("convertBtn");
    const textInput = document.getElementById("textInput");
    const toggleBtn = document.getElementById("toggleTranslation");
    const fullscreenBtn = document.getElementById("openFullscreen");
  
    // Dictionary mapping words to local MP4 files in "videos/" folder
    const signDictionary = {
      "hello": "videos/hello.mp4",
      "thanks": "videos/thanks.mp4",
      "yes": "videos/yes.mp4",
      "no": "videos/no.mp4",
      "sorry": "videos/sorry.mp4"
    };
  
    // 1. Text-to-Sign Conversion
    convertBtn.addEventListener("click", function () {
      const inputWord = textInput.value.trim().toLowerCase();
      if (signDictionary[inputWord]) {
        const videoURL = chrome.runtime.getURL(signDictionary[inputWord]);
        console.log("Loading video for:", inputWord, "from", videoURL);
  
        // Clear existing <source> elements
        videoElement.innerHTML = '';
        // Create a new <source> element with type="video/mp4"
        const sourceEl = document.createElement("source");
        sourceEl.src = videoURL;
        sourceEl.type = "video/mp4";
        videoElement.appendChild(sourceEl);
  
        // Load and play the new video
        videoElement.load();
        videoElement.play();
      } else {
        alert("Sorry, no sign language video available for that word.");
      }
    });
  
    // 2. Toggle Play/Pause
    toggleBtn.addEventListener("click", function () {
      if (videoElement.paused) {
        videoElement.play();
        toggleBtn.innerText = "Pause Translation";
      } else {
        videoElement.pause();
        toggleBtn.innerText = "Toggle Translation";
      }
    });
  
    // 3. Open Fullscreen (in a new tab)
    fullscreenBtn.addEventListener("click", function () {
      // If you added a <source> tag, grab its src; otherwise, use videoElement.src
      const currentSource = videoElement.querySelector("source")?.src || videoElement.src;
      // Open the current video in a new tab for real fullscreen
      window.open(currentSource, "_blank");
    });
  });