const chatlist = document.getElementById("chatlist");
function InitChatList(){
    chatlist.innerHTML=''
    fetch(SERVER_URL + "/UserDB")
    .then((response) => response.json())
    .then((users) => {
        const USERDB = users[USER].ActiveChats;

        for (const key in USERDB) {
            Chats[key] = {
                Name: key,
                Email: USERDB[key].Email,
                ChatHistory: USERDB[key].Chat,
            };
            ChatList_Name = key;
            ChatList_Email = USERDB[key].Email;

            chatlist.innerHTML += `<div class="chat" onclick="activate(this)"><h1 class="Name">${ChatList_Name}</h1> <h3 class="Email">${ChatList_Email}</h3></div>`;
        }
    });
}
InitChatList()
let lastActive = document.getElementsByClassName("active")[0];
function activate(e) {
    e.classList.add("active");
    const active = document.getElementsByClassName("active");
    if (active.length > 1) {
        lastActive.classList.remove("active");
    }
    lastActive = document.getElementsByClassName("active")[0];
    ActiveChat = lastActive.getElementsByClassName("Name")[0].innerText;
    FetchChats();
}

function FetchChats() {
    ChatHistory = Chats[ActiveChat].ChatHistory;
    Name = Chats[ActiveChat].Name;
    Email = Chats[ActiveChat].Email;

    document
        .getElementById("ActiveChatName")
        .getElementsByClassName("Name")[0].innerText = Name;
    document
        .getElementById("ActiveChatName")
        .getElementsByClassName("Email")[0].innerText = Email;

    const ChatBody = document.getElementById("Chats");

    ChatBody.innerHTML = "";
    ChatHistory.forEach((message) => {
        if (message.slice(0, 2) == "##") {
            ChatBody.innerHTML +=
                '<div class="textMessage there">' + message.slice(2) + "</div>";
        } else {
            ChatBody.innerHTML +=
                '<div class="textMessage here">' + message.slice(2) + "</div>";
        }
    });
}
function Refresh() {
    const chatlist = document.getElementById("chatlist");
    fetch(SERVER_URL + "/UserDB")
        .then((response) => response.json())
        .then((users) => {
            const USERDB = users[USER].ActiveChats;
 
            for (const key in USERDB) {
                Chats[key] = {
                    Name: key,
                    Email: USERDB[key].Email,
                    ChatHistory: USERDB[key].Chat,
                };

                FetchChats();
            }
        });
}

const searchInput = document.getElementById("ChatListSearch");

searchInput.addEventListener("input", (e) => {
    value = e.target.value.toLowerCase();

    // console.log(chatlist.children[0])
    for (let index = 0; index < chatlist.children.length; index++) {
        const element = chatlist.children[index];

        // console.log(element.innerHTML.toString().toLowerCase().includes(value))
        if (element.innerHTML.toString().toLowerCase().includes(value)) {
            // console.log(element)
            element.style.display = "flex";
        } else {
            element.style.display = "none";
        }
    }
});

let Sender = USER;
addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        SendChat();
    }
});
function SendChat() {
    if (document.getElementById("ChatInputTextBoxInput").value) {
        fetch(SERVER_URL + "/Chat/AddChat/" + Sender + "/" + ActiveChat, {
            method: "POST",
            body: JSON.stringify({
                Message: '$$'+document.getElementById("ChatInputTextBoxInput").value,
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8",
            },
        }).then(() => {
            document.getElementById("ChatInputTextBoxInput").value = "";
        });
    }
}

function NewChatDialogue(){
    
    // console.log(document.querySelector('NewChat'))
 document.querySelector('NewChat').style.display='flex'
  }
let NewChatList=[]
function ListDoctors(){
    const AddChatList=document.getElementById('AddChatList')
    console.log(AddChatList)
    fetch(SERVER_URL+'/DoctorDetails').then(response=>response.json()).then(data=>{

        for (const key in data) {
            //  const element = data[key];
             AddChatList.innerHTML+='<li onclick="addChat(`'+key+'`,`'+data[key]['Email'].toString()+'`)">'+'<h1>'+key+'</h1>'+'<h3>'+data[key]['Email']+'</h3></li>'
            }
            NewChatList=AddChatList.children
            console.log('Loaded')
            console.log(NewChatList)
    })
}

ListDoctors()
function addChat(name,email){
fetch(SERVER_URL+'/Chat/NewChat/'+USER+'/'+name)
.then(()=>{
    InitChatList()
})
document.querySelector('NewChat').style.display='none'
}
const SearchForADoctor =document.getElementById('SearchForADoctor')
SearchForADoctor.addEventListener('input',()=>{
    // console.log()
    value=SearchForADoctor.value
    for (let index = 0; index < NewChatList.length; index++) {
            const element = NewChatList[index];
            
            if(element.innerText.includes(value)){
                console.log(element.innerText)
                element.style.display = "list-item";
            }else{
                element.style.display = "none";

            }
       
    }
})
















