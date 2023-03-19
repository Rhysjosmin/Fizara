const Newsfeed = document.getElementById("Newsfeed");
NewsfeedTemplate = document.getElementById("NewsTemplate");
let Newscontent = NewsfeedTemplate.content.cloneNode(true);
function fetchNews(){
// fetch("http://127.0.0.1:5000/News")
fetch("http://127.0.0.1:5500/APITest/News.json")
  .then((response) => response.json())
  .then((data) => {
    News = data;
  })
  .then(() => {
    for (let Article in News) {
      Newscontent = NewsfeedTemplate.content.cloneNode(true);
      Newscontent.getElementById('News').href=News[Article]["link"];
      Newscontent.getElementById("NewsHeader").innerText = Article;
      Newscontent.getElementById("NewsBody").innerText = News[Article]["Body"];

      Newsfeed.appendChild(Newscontent);
    }
  });
}