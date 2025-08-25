function toggleChat() {
  const chat = document.getElementById("chatWindow");
  chat.style.display = (chat.style.display === "flex") ? "none" : "flex";
  chat.style.flexDirection = "column"; // keep vertical layout
}

async function sendMessage() {
  const input = document.getElementById("userInput");
  const msg = input.value.trim();
  if (!msg) return;

  const chatMessages = document.getElementById("chatMessages");

  // Show user message (right side)
  const userMsg = document.createElement("div");
  userMsg.className = "message user";
  userMsg.textContent = msg;
  chatMessages.appendChild(userMsg);

  // Send to backend
  const res = await fetch("/get", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: msg })
  });
  const data = await res.json();

  // Show bot message (left side)
  const botMsg = document.createElement("div");
  botMsg.className = "message bot";
  botMsg.textContent = data.response;
  chatMessages.appendChild(botMsg);

  // Auto scroll
  chatMessages.scrollTop = chatMessages.scrollHeight;

  input.value = "";
}
