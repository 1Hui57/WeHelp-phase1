//抓取load more DOM
const btn = document.getElementById('btn');
//監聽事件
let clickCount=0;
btn.addEventListener('click',function(){
    clickCount++;
    loadMore(10);
});
function loadMore(num){
    fetch(
        "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1 "
      )
        .then(function (response) {
          return response.json();
        })
        .then((data) => {
            let result = data.data.results; //拿到資料
            //先拿到最後一個big-box的節點
            let bigBox = document.querySelectorAll(".big-box");
            // let lastbox =BigBox.lastChild;
            //建立一個新的big-box
            for(let i=0;i<10;i++){
                //建立新的box
                let newBox = document.createElement("div");
                newBox.className = "box";
                //建立新的img
                let newImg = document.createElement("img");
                newImg.className = "width_height_30px";
                newImg.src = "star.png";
                //建立新的box-title
                let newBoxTitle = document.createElement("div");
                newBoxTitle.className = "box-title";
                console.log(result[clickCount*num+3+i].stitle);
                let newTitle = document.createTextNode(result[clickCount*num+3+i].stitle);
                newBoxTitle.style.textOverflow = "ellipsis";
                newBoxTitle.style.overflow = "hidden";
                newBoxTitle.style.whiteSpace = "nowrap";
                newBoxTitle.appendChild(newTitle);
                //將box下的兩個DOM添加到box內
                newBox.appendChild(newImg);
                newBox.appendChild(newBoxTitle);
                //添加背景圖片
                newBox.style.backgroundImage ="url('http" + result[clickCount*num+3+i].filelist.split("http")[1] + "')";
                //將每一個新的box加到最後一個box後面
                bigBox[bigBox.length-1].appendChild(newBox);
            }
        });
}

