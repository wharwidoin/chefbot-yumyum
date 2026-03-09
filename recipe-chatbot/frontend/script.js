async function sendMessage(){

    let input = document.getElementById("message")
    let chatbox = document.getElementById("chatbox")

    let message = input.value

    if(message === "") return

    chatbox.innerHTML += `<div class="user"><b>You:</b> ${message}</div>`

    input.value = ""

    let response = await fetch("http://127.0.0.1:8000/chat",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            message:message
        })
    })

    let data = await response.json()

    chatbox.innerHTML += `<div class="bot"><b>ChefBot:</b> ${data.response}</div>`

    chatbox.scrollTop = chatbox.scrollHeight
}