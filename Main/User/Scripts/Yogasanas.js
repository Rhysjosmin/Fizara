// http://127.0.0.1:5000/Yogasanas/BreastCancer
const Yogasanas = document.getElementById('Yogasanas')
const template=document.createElement('div')
let Yogas=[]
const YogaTemplate = document.getElementById('YogaTemplate')

fetch(`${SERVER_URL}/Yogasanas/${Page}`)
.then(response=>response.json())
.then(array=>{
    Yogas=array.map(element => {
        const yoga=document.createElement('div')
        const ul=document.createElement('ul')
        element['paragraphs'].forEach(paragraph => {
            const p=document.createElement('li')
            p.innerText=paragraph.normalize().replace(' ','')
            p.style.listStyle='none'
            ul.appendChild(p)
            yoga.className='Yoga'
            yoga.innerHTML=`
       
                <img src='${element['image']}' alt=''/>
                <div>  
                    <h1>${element['heading']}</h1>
                      ${ul.innerHTML}
                        </div>
                    
            `
        });
        Yogasanas.appendChild(yoga)
        return{heading:element['heading'],paragraph:ul,img:element['image'],element:yoga}
    });
})




const searchInput=document.getElementById('search')
searchInput.placeholder='Search Yogasanas'
searchInput.addEventListener('input',(e)=>{

  value=e.target.value.toLowerCase();
  Yogas.forEach(_yoga=>{
    const isVisible=_yoga.heading.toLowerCase().includes(value) || _yoga.paragraph.innerHTML.toLowerCase().includes(value)
    _yoga.element.classList.toggle('hide',!isVisible)
    
  })
  let hiddenYogas=document.getElementsByClassName('hide')

})