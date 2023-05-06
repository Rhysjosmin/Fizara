let sound=new Audio('../../media/Audio/MessagePopup.mp3')


const socket = new WebSocket(
    "wss://" + "127.0.0.1:5000" + "/echo/" + Sender + "/" + "Isacc"
);

socket.addEventListener("message", (ev) => {
    Refresh();
    sound.play()
});
