function showPopup(message) {
    var popup = document.getElementById("popup");
    popup.innerText = message;
    popup.style.display = "block";
    setTimeout(function() {
        popup.style.display = "none";
    }, 30000); // 30 seconds
}

document.addEventListener("DOMContentLoaded", function() {
    var messagesJson = document.getElementById("messages-json").textContent;
    var messages = JSON.parse(messagesJson);
    messages.forEach(function(message) {
        showPopup(message);
    });
});
