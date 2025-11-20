// Log a message when the page is loaded
window.onload = () => {
    console.log("Important Links page loaded");
};

// Handle link clicks (for tracking user clicks)
document.querySelectorAll('.link-box').forEach((linkBox) => {
    linkBox.addEventListener('click', () => {
        console.log(`Clicked on: ${linkBox.querySelector('h2').textContent}`);
    });
});

// Toggle Dark Mode
const toggleButton = document.getElementById("toggle-mode");

toggleButton.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    if (document.body.classList.contains('dark-mode')) {
        toggleButton.textContent = 'Toggle Light Mode';
    } else {
        toggleButton.textContent = 'Toggle Dark Mode';
    }
});
