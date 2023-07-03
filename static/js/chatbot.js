$("#input-message").on("keypress", function (e) {
  if (e.which == 13) {
    sendMessage();
  }
});

$("#send-btn").on("click", function () {
  sendMessage();
});

function getTimestamp() {
  const date = new Date();
  return `${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}`;
}
 
async function sendChatRequest(userMessage, signal) {
  const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_message: userMessage }),
      signal: signal,
  });
  return await response.json();
}

async function askChatBot(userMessage, retryCount = 3) {
const controller = new AbortController();
const signal = controller.signal;

setTimeout(() => controller.abort(), 30000); // Dit annuleert de fetch request na 30 seconden

try {
  $("#typing-indicator").show();
  startTypingAnimation();
    const response = await sendChatRequest(userMessage, signal);
    console.log("Response from the backend:", response);
    const chatbotResponse = response.chatbot_response;
    const timestamp = getTimestamp();

    let responseText = chatbotResponse;
    $("#chat-output").append(`<div class="message bot"><strong>GroeimetAi:</strong> ${responseText}<span class="timestamp-bot" style="float: left;">${timestamp}</span></div>`);
    $("#chat-output").scrollTop($("#chat-output")[0].scrollHeight);
} catch (error) {
    console.error("Error:", error);
    if (error.name === 'AbortError') {
        if (retryCount > 0) {
            console.log(`Retrying... ${retryCount} attempts left.`);
            await askChatBot(`${userMessage} maak het antwoord zo klein mogelijk`, retryCount - 1);
        } else {
            console.log('Failed after 3 attempts');
            $("#chat-output").append(`<div class="message bot"><strong>GroeimetAi:</strong> Het antwoord op deze vraag is te lang, probeer de vraag kleiner te maken</div>`);
        }
    }
} finally {
  stopTypingAnimation();
}

}

let typingAnimation;
function startTypingAnimation() {
let dots = "";
typingAnimation = setInterval(() => {
  if (dots.length < 3) {
    dots += ".";
  } else {
    dots = "";
  }
  $("#typing-indicator").text(`GroeimetAi is typing${dots}`);
}, 500);
}

function stopTypingAnimation() {
clearInterval(typingAnimation);
$("#typing-indicator").hide();
}

function sendMessage() {
const userMessage = $("#input-message").val();
if (userMessage.trim().length > 0) {
  const timestamp = getTimestamp();
  $("#chat-output").append(`<div class="message user"><strong>You:</strong> ${userMessage}<span class="timestamp-user" style="float: right;">${timestamp}</span></div>`);
  $("#input-message").val("");
  var userInput = document.getElementById("input-message");
  userInput.disabled = true;
  setTimeout(function () {
    userInput.disabled = false;
    userInput.focus();
  }, 2000);

  // Scroll naar beneden na het versturen van een bericht
  $("#chat-output").scrollTop($("#chat-output")[0].scrollHeight);

  askChatBot(userMessage);
}  
}

function changePlaceholder() {
  const inputField = $("#input-message");
  const placeholderText = inputField.attr("placeholder");

  if (placeholderText === "Type your message here") {
    inputField.attr("placeholder", "Typ uw bericht hier");
  } else {
    inputField.attr("placeholder", "Type your message here");
  }
}

setInterval(changePlaceholder, 5000);

$(document).ready(async function () {
  const timestamp = getTimestamp();
  $(".timestamp-greeting").text(timestamp);

  const response = await fetch("/start-chat", { method: "GET" });
  const jsonResponse = await response.json();
  const chatbotResponse = jsonResponse.chatbot_response;

  $("#chat-output").append(`<div class="message bot"><strong>GroeimetAi:</strong> ${chatbotResponse}<span class="timestamp-bot" style="float: left;">${timestamp}</span></div>`);
});