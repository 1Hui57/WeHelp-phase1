# 將原本的ditionary中的key或value取出並放在新的dictionay中
consultants=[ 
{"name":"John", "rate":4.5, "price":1000}, 
{"name":"Bob", "rate":3, "price":1200}, 
{"name":"Jenny", "rate":3.8, "price":800} 
] 
consultanatsTime={people["name"]:list(range(25)) for people in consultants }
print(consultanatsTime)
