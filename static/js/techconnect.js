// Function to navigate to the Tech Connect page
function techConnect() {
    window.location.href = '/tech_connect/';
}

// Add event listener to the Tech Connect button
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('tech-connect').addEventListener('click', techConnect);
});
