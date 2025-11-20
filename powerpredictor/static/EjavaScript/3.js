document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way
    window.location.href = "Predictor.html"; // Redirect to the Energy Predictor page
});
gsap.registerPlugin(ScrambleTextPlugin, MorphSVGPlugin);
// Selecting the elements
const togglePassword = document.querySelector("#togglePassword");
const password = document.querySelector("#password");
const eyeIcon = document.querySelector("#eyeIcon");

// Toggle password visibility
togglePassword.addEventListener("click", function () {
    // Check the current type of the password field
    const type = password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);

    // Switch the eye icon based on the type
    if (type === "text") {
        eyeIcon.src = "E:\Electricity Delhi (Tulas)\eye-closed.png"; // Replace with the open eye icon path
    } else {
        eyeIcon.src = "E:\Electricity Delhi (Tulas)\eye-closed.png"; // Replace with the closed eye icon path
    }
});