# 網路連線
import urllib.request as req
import json
# 第一份資料
src1="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1 "
with req.urlopen(src1) as response:
    data1=json.load(response)
result1=data1["data"]["results"]
spotList=[] # 用來新增整理好的資料
for item in result1:
    title=item["stitle"] # 景點名稱
    imageURL="http"+item["filelist"].split('http')[1] # 第一張圖片URL
    longitude=item["longitude"] # 經度
    latitude=item['latitude'] # 緯度
    serial_no=item['SERIAL_NO'] # 流水號
    spotList.append({
        "title":title,
        "longitude":longitude,
        "latitude":latitude,
        "imageURL":imageURL,
        'serial_no':serial_no
    })
# print(spotList)

# 第二份資料
src2="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2 "
with req.urlopen(src2) as response2:
    data2=json.load(response2)
result2=(data2["data"]) # 拿到有用的資料
MRTlist=[]
for item in result2:
    addr=str(item['address'])[5:] # 去掉臺北市，從行政區開始的地址
    MRTlist.append({
        "站名":item['MRT']+"站", 
        "地址":addr,
        "serial_no":item['SERIAL_NO']
    })
# print(MRTlist)

# 新增一個列表，裡面的資料型態為字典-包含景點的各種資料
spotInformation=[]
for spot in spotList:
    for item in MRTlist:
        if item["serial_no"] in spot["serial_no"]:
            spotInformation.append({
                "title":spot["title"],
                "行政區":str(item["地址"][0:3]), # 找到景點位於哪一個地區
                "捷運站":item["站名"],
                "longitude":spot["longitude"],
                "latitude":spot["latitude"],
                "imageURL":spot["imageURL"]
            })

# 將資料寫入將資料寫入"spot.csv"
import csv
with open("spot.csv", mode="a", newline="", encoding="utf-8") as file:    
    writer=csv.writer(file)
    for item in spotInformation:
        writer.writerow([item["title"], item["行政區"],item["longitude"],item["latitude"],item["imageURL"]])

# 建立一個key值為站名的字典，這樣可以直接拿到站名的資料
MRTspot={}
for item in MRTlist:
    MRTspot[item["站名"]]={
        "站名":item["站名"],
        "地址":item["地址"],
        "serial_no":item["serial_no"],
        "spot":[]
    }

# 將景點加入spot內
for item in spotInformation:
    MRTspot[item["捷運站"]]["spot"].append(item["title"])

# 將資料寫入"mrt.csv"
with open("mrt.csv", mode="w",newline="", encoding="utf-8") as file2:
    writer=csv.writer(file2,quoting=csv.QUOTE_MINIMAL)
    for key, value in MRTspot.items():
        line = f"{key[0:-1]},{",".join(value['spot'])}\n"
        file2.write(line)
       
# 原本時間複雜度高的作法
# MRTspot={}
# for item in MRTlist:
#     for spot in spotInformation:
#         if item["站名"] in spot["捷運站"]:
#             if item["站名"] in MRTspot:
#                 MRTspot[item["站名"]].append(spot["title"])
#             else:
#                 MRTspot[item["站名"]] = []
# print(MRTspot)
            
            
            
