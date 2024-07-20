document.addEventListener('DOMContentLoaded', function() {
    const startChatButton = document.getElementById('start-chat');
    const chatSection = document.getElementById('chat-section');
    const sendButton = document.getElementById('send-btn');
    const userInput = document.getElementById('user-input');
    const chatContent = document.getElementById('chat-content');

    startChatButton.addEventListener('click', function() {
        chatSection.style.display = 'block';
        startChatButton.style.display = 'none';  // Hide the start button
    });

    sendButton.addEventListener('click', async function() {
        const message = userInput.value;
        if (message.trim() === '') return;  // Avoid sending empty messages

        // Display user message in chat
        chatContent.innerHTML += `<div class="message user-message">${message}</div>`;
        userInput.value = '';  // Clear input field

        // Send message to the backend
        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message }),
            });

            const data = await response.json();
            const botResponse = data.response;

            // Display bot response in chat
            chatContent.innerHTML += `<div class="message bot-message">${botResponse}</div>`;
        } catch (error) {
            console.error('Error:', error);
        }
    });
});
