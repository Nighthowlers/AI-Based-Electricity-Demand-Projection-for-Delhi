document.getElementById('queryForm').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Your query has been submitted! We will get back to you shortly.');
    this.reset();
});

document.getElementById('feedbackForm').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Thank you for your feedback! We appreciate your input.');
    this.reset();
});