let sound=new Audio('../../media/Audio/MessagePopup.mp3')


const socket = new WebSocket(
    "wss" + SERVER_URL.replace('https','') + "/echo/" + Sender + "/" + "Isacc"
);

socket.addEventListener("message", (ev) => {
    Refresh();
    sound.play()
});
