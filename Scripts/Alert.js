function alert2(AlertTitle,AlertMessage){
    let Alert=document.createElement('div')
    let Title=document.createElement('h1')
    let Message=document.createElement('h3')
    Title.innerText=AlertTitle
    Title.style.fontSize='1.1em'
    Title.style.fontWeight='900'
    Message.innerText=AlertMessage
    Message.style.fontWeight='600'
    Message.style.fontSize='.9em'

    Alert.appendChild(Title)
    Alert.appendChild(Message)
    // SetAlertStyle(Alert.style)
    Alert.style.position='Fixed'
    Alert.style.bottom='-1000px'
    Alert.style.right='10px'
    Alert.style.fontWeight='700'
    Alert.style.background='#ffffff'
    Alert.style.color='#010101'
    Alert.style.width='15rem'
    Alert.style.minHeight='4rem'
    Alert.style.border='solid black 2px'
    Alert.style.borderRadius='10px'
    Alert.style.boxShadow='5px 5px black'
    Alert.style.padding='5px'
    Alert.style.transition='.8s'

    document.body.appendChild(Alert)

    setTimeout(()=>{
        Alert.style.bottom='10px'

    },10)

    setTimeout(()=>{
        Alert.style.bottom='-1000px'

    },2200)
    setTimeout(()=>{
    document.body.removeChild(Alert)

    },3000)
    }
    
