samsung = {'color': 'blue', 'capacity': '265', 'display': '6.1', 'power battery': 'up 17h'}
print(samsung)
print(samsung['color'])
a = samsung["display"]
print(a)
d = samsung.get("power battery")
print(d)
samsung["power battery"] = 'up 5d'
print(samsung)
for x in samsung:
    print(x)
for x in samsung:
    print(samsung[x])
for x in samsung.values():
    print(x)
if "color" in samsung:
    print("yes,color is one of the kyes in samsung dictionry")
    print(len(samsung))
    samsung["price"]="1500 Aed"
    print(samsung)
    samsung.pop("color")
    print(samsung)
    samsung.popitem()
    print(samsung)
    del samsung["display"]
    print(samsung)
    Mydict = dict(samsung)
print(Mydict)
countries={
        "france":{
      "language":"french",
    "population":"66million"
         },
     "tunisia":{
         "language":"arabic",
         "population":"12 million"

     }
 }
print(countries)