import urllib.request as req
import bs4
# 定義一個函式用來抓取文章所有資料(包括寫入)
def getData(url):
    request = req.Request(url, headers={
        "cookie":"over18=1",#滿18的cookie
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likes Gecko) Chrome/131.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data= response.read() .decode("utf-8")

    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    likes=root.find_all("div", class_="nrec")
    nextLink=root.find("a",string="‹ 上頁")

    lottery=[]
    for title, like in zip(titles, likes):
        if title.a:
            lottery.append({
                "title":title.a.string,
                "href":"https://www.ptt.cc"+title.a['href'],
                'like':like.span.string if like.span else "0"
            })

    # 抓每篇文章的發文時間
    times=[]
    for item in lottery:
        articleURL=item['href']
        #程式正常運行時執行try內的程式
        try:
            request2=req.Request(articleURL, headers={
                "cookie":"over18=1",
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likes Gecko) Chrome/131.0.0.0 Safari/537.36"
            })
            with req.urlopen(request2) as response2:
                data2=response2.read() .decode("utf-8")
            root=bs4.BeautifulSoup(data2, "html.parser")
            # print(root)
            timeSpans=root.find_all("span", class_="article-meta-value")
            if len(timeSpans)>3 and timeSpans[3] !=None:
                times.append(timeSpans[3].get_text())
            else:
                times.append("") #沒有時間的話新增空字串
        #當有出現錯誤，執行下列程式(在寫程式時有很多個文章網頁打不開，因此無法取得時間，因此時間的部分會先以"錯誤"代替)
        except:
            times.append("錯誤")
    # 將時間整合於lottery資料
    for index, item in enumerate(lottery):
        item['time']=times[index]
    # 將資料寫入article.csv
    import csv
    with open("article.csv", mode="a", newline="", encoding="utf-8") as file:
        writer=csv.writer(file)
        for item in lottery:
            #寫入的部分如果mode為"w"會覆寫檔案，因此mode以"a"執行，不會覆寫而是新增資料
            writer.writerow([item['title'],item['like'],item['time']])
    return nextLink["href"] #回傳上一頁的網址

pageURL="https://www.ptt.cc/bbs/Lottery/index.html"
count=0
while count<2:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
getData(pageURL)