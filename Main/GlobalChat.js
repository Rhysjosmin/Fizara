let sound=new Audio('../../media/Audio/MessagePopup.mp3')

let wbskt="wss" + SERVER_URL.replace('https','').replace('http','') + "/echo/" + Sender + "/" + 'ActiveChat'
console.log(wbskt)
const socket = new WebSocket(
    wbskt
);

socket.addEventListener("message", (ev) => {
    Refresh();
    sound.play()
});
