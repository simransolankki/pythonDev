document.addEventListener("DOMContentLoaded", () => {
    const videoItems = document.querySelectorAll(".video-item");

    videoItems.forEach(item => {
        const video = item.querySelector(".video-preview");

        let playTimeout, pauseTimeout;

        item.addEventListener("mouseover", () => {
            clearTimeout(pauseTimeout);
            playTimeout = setTimeout(() => {
                video.play().catch(error => {
                    console.error("Error trying to play video:", error);
                });
            }, 200); // Slight delay before playing
        });

        item.addEventListener("mouseout", () => {
            clearTimeout(playTimeout);
            pauseTimeout = setTimeout(() => {
                video.pause();
                video.currentTime = 0; // Reset the video to the start
            }, 200); // Slight delay before pausing
        });
    });
});
