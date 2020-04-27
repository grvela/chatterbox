let buttonInput = document.querySelector("#buttonInput");
let inputForm = document.querySelector(".footbar");


function requestBot(userMessage){
  data = {
    "sender" : "User",
    "message" : userMessage
  }
  fetch('http://localhost:5000/requestBot', {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body : JSON.stringify(data)
  })
  .then(function(response){
    return response.json()
  })
  .then(function(response){
    let messageBot = response[0].text;
    let chatbox = document.querySelector('.chatbox');
    let beforeMessages = document.querySelector('.chatbox').innerHTML;
    let newMessages =
    '<div class="side"><span class="bot message">'
    + messageBot +
    '</span> </div>';
    chatbox.innerHTML =  beforeMessages + newMessages;
    chatbox.scrollTop = chatbox.scrollHeight;
  })
}

function sendMessage(){
  let input = document.querySelector('#chatInput');
  let userMessage = input.value;
  let chatbox = document.querySelector('.chatbox');
  if(userMessage != ""){
    let beforeMessages = document.querySelector('.chatbox').innerHTML;
    let newMessages =
    '<div class="side"><span class="user message">'
    + userMessage +
    '</span> </div>' ;
    chatbox.innerHTML =  beforeMessages + newMessages;
    chatbox.scrollTop = chatbox.scrollHeight;
    input.value = "";
    requestBot(userMessage);
  }
}

inputForm.addEventListener('keypress', function(key) {
  if(key.which == 13){sendMessage();}
})
buttonInput.addEventListener('click', sendMessage)
