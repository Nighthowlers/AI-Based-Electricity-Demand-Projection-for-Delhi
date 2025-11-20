// JavaScript functionality for scrolling and other actions can be added here if needed

// Example of handling marquee speed (Optional)
document.addEventListener('DOMContentLoaded', function() {
    const marquee = document.querySelector('.marquee');
    let speed = 30; // Speed of the scrolling
    marquee.style.animationDuration = `${speed}s`;

    // Optionally, you could add interaction here like changing speed or stopping on hover
    marquee.addEventListener('mouseenter', () => {
        marquee.style.animationPlayState = 'paused';
    });

    marquee.addEventListener('mouseleave', () => {
        marquee.style.animationPlayState = 'running';
    });
});
