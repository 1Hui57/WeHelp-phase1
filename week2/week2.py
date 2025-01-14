# print('Task1:')
# def find_and_print(messages, current_station):
#     greenLine=("Songshan","Nanjing Sanmin","Taipei Arena",
#                "Nanjing Fuxing","Songiang Nanjing",
#                "Zhongshan","Beimen","Ximen","Xiaonanmen",
#                "Chiang Kai-Shek Memorial Hall","Guting","Taipower Building",
#                "Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang",
#                "Xindian City Hall","Xindian" )
    
#     #搜尋的站的名稱index
#     current_station_index=greenLine.index(current_station) #searchIndex為輸入的站名的index
#     dicDistance={}
#     # 第一部分，計算搜尋的站點有沒有人在
#     for who ,whoSays in messages.items(): #who為message的key，也就是名字
#         if current_station in whoSays: #當輸入的位置有在某人說的話中出現
#             print(who) #印出名字
#             return
#     #who為message的key，也就是名字
#         else:
#             for location in greenLine: # location 代入綠線站名
#                 if location in whoSays: # 每個人的位置
#                     locationIndex=greenLine.index(location) #人所在的站的index
#                     distance=abs(current_station_index-locationIndex) #距離
#                     dicDistance[who]=distance
#         # 計算位在小碧潭站的人，距離是多少
#             if "Xiaobitan" in whoSays:
#                 distance=abs(current_station_index-greenLine.index("Qizhang"))+1
#                 dicDistance[who]=distance
#     distanceList=list(dicDistance.values())    
#     distanceList.sort()
#     closestDistance=distanceList[0]
#     for x,y in dicDistance.items():
#                 if closestDistance==y:
#                     result=x
#     print(result)

# messages={
#     "Leslie":"I'm at home near Xiaobitan station.",
#     "Bob":"I'm at Ximen MRT station.",
#     "Mary":"I have a drink near Jingmei MRT station.",
#     "Copper":"I just saw a concert at Taipei Arena.",
#     "Vivian":"I'm at Xindian station waiting for you."
# }

# find_and_print(messages, "Wanlong") # print Mary
# find_and_print(messages, "Songshan") # print Copper
# find_and_print(messages, "Qizhang") # print Leslie
# find_and_print(messages, "Ximen") # print Bob
# find_and_print(messages, "Xindian City Hall") # print Vivian
# print('------------------------------')

# print('Task2:')
# # your code here, maybe 
# consultantsTime={}
# def book(consultants, hour, duration, criteria):
#     global consultantsTime
#     #先做一個時間列表 {"John":[0,1,2,3,4...,23], "Bob":[0,1,2,3,4...,23]...}
#     if consultantsTime=={}:
#         consultantsTime={people["name"]:list(range(24)) for people in consultants }
#     #有空的顧問列表
#     consultant=[]
#     #根據輸入的資料找出有空的顧問
#     #(1)根據輸入的資料生成一個要求的時間列表，例如輸入hour,dutation為2,3，生成一個list[2,3,4]
#     requestTime=list(range(hour,hour+duration))
#     #(2-1)比對顧問時間列表，列出時間對的上的顧問，並在列表中添加名字
#     for name, time in consultantsTime.items():
#         result=set(requestTime).issubset(time)
#         if result==True:
#             consultant.append(name)
#     #(2-2)如果consultants中沒有資料，return"No Service"
#     if consultant==[]:
#         print('No Service')
#         return
#     #(3)根據(2-1)生成的consultant列表及criterua生成篩選標準的字典
#     # rate部分
#     if criteria=='rate':
#         rateList={}
#         for c in consultants:
#             if c['name'] in consultant:
#                 rateList[c['name']]=c['rate']
#         # 印出顧問
#         rateList=sorted(rateList.items(), key=lambda x:x[1] )
#         print(rateList[-1][0])
#         resultName = rateList[-1][0]
#         for i in requestTime:
#             consultantsTime[resultName].remove(i)
#     # 另一寫法
#     # if criteria=='rate':
#     #     rateList={c['name']: c['rate'] for c in consultants if c['name'] in consultant}
#     #     print(rateList)

#     # price部分
#     if criteria=='price':
#         priceList={}
#         for c in consultants:
#             if c['name'] in consultant:
#                 priceList[c['name']]=c['price']
#         # 印出顧問
#         priceList=sorted(priceList.items(), key=lambda x:x[1] )
#         resultName = priceList[0][0]
#         print(priceList[0][0])
#          #將所選顧問的已售出的時間刪除
#         for i in requestTime:
#             consultantsTime[resultName].remove(i)
   
# consultants=[ 
# {"name":"John", "rate":4.5, "price":1000}, 
# {"name":"Bob", "rate":3, "price":1200}, 
# {"name":"Jenny", "rate":3.8, "price":800} 
# ] 

# book(consultants, 15, 1, "price") # Jenny 
# book(consultants, 11, 2, "price") # Jenny 
# book(consultants, 10, 2, "price") # John 
# book(consultants, 20, 2, "rate") # John 
# book(consultants, 11, 1, "rate") # Bob 
# book(consultants, 11, 2, "rate") # No Service 
# book(consultants, 14, 3, "price") # John

# print('------------------------------')
print('Task2:')