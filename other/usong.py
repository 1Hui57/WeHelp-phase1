print('Task1:')
def find_and_print(messages, current_station):
    greenLine=("Songshan","Nanjing Sanmin","Taipei Arena",
               "Nanjing Fuxing","Songiang Nanjing",
               "Zhongshan","Beimen","Ximen","Xiaonanmen",
               "Chiang Kai-Shek Memorial Hall","Guting","Taipower Building",
               "Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang",
               "Xindian City Hall","Xindian" )
    isXiaobitan=current_station=="Xiaobitan"
    stationDistance = {}
    
    if isXiaobitan:
        sourceIndex = greenLine.index("Qizhang")
        for index, station in enumerate(greenLine):
            stationDistance[station] = abs(index - sourceIndex) + 1
        stationDistance["Xiaobitan"] = 0
    else:
        sourceIndex = greenLine.index(current_station)
        for index, station in enumerate(greenLine):
            stationDistance[station] = abs(index - sourceIndex)
        stationDistance["Xiaobitan"] = stationDistance["Qizhang"] + 1
    nameList = {}
    for name, message in messages.items():
        for station in greenLine:
            if station in message:
                nameList[name] = stationDistance[station]
                break
        if "Xiaobitan" in message:
            nameList[name] = stationDistance["Xiaobitan"]
    nameList = sorted(nameList.items(), key=lambda item: item[1])
    print(nameList[0][0])


messages={
    "Leslie":"I'm at home near Xiaobitan station.",
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Vivian":"I'm at Xindian station waiting for you."
}

find_and_print(messages, "Wanlong") # print Mary
# find_and_print(messages, "Songshan") # print Copper
# find_and_print(messages, "Qizhang") # print Leslie
# find_and_print(messages, "Ximen") # print Bob
# find_and_print(messages, "Xindian City Hall") # print Vivian
# find_and_print(messages, "Xiaobitan") # print Vivian
print('------------------------------')