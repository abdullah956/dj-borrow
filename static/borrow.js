function sendMessage() {
  let inputField = document.getElementById("user-input");
  let message = inputField.value.trim();
  let chatBox = document.getElementById("chat-box");

  if (message === "") return;

  // Display user message
  let userMessage = document.createElement("div");
  userMessage.className = "bg-blue-500 text-white p-2 rounded mb-2";
  userMessage.innerText = "You: " + message;
  chatBox.appendChild(userMessage);

  inputField.value = "";

  // Send request to chatbot API
  fetch("/chat/api/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message }),
  })
    .then((response) => response.json())
    .then((data) => {
      let botMessage = document.createElement("div");
      botMessage.className = "bg-gray-200 p-2 rounded mb-2";
      botMessage.innerText = "Bot: " + data.response;
      chatBox.appendChild(botMessage);

      chatBox.scrollTop = chatBox.scrollHeight;
    });
}
