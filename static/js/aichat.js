// aichat.js

document.addEventListener('DOMContentLoaded', function() {
    const chatButton = document.getElementById('chat-button');
    if (chatButton) {
        chatButton.addEventListener('click', navigateToChat);
    }

    function navigateToChat() {
        console.log("Navigating to AI Chat Support");
        window.location.href = '/aichat/';
    }
});
