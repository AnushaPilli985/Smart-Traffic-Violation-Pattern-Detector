(function injectVideo() {
    const video = document.createElement("video");
    video.src = chrome.runtime.getURL("videos/sign_translation.mp4");
    video.controls = true;
    video.style.position = "fixed";
    video.style.bottom = "10px";
    video.style.right = "10px";
    video.style.width = "300px";
    video.style.zIndex = 9999;
    
    document.body.appendChild(video);
  })();