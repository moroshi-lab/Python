fruits = ["りんご","ばなな","みかん"]
print(fruits[0])
fruits.append("ぶどう")
fruits.remove("みかん")

for i in fruits:
    print(i)


items = {
    "りんご" : 120,
    "バナナ" : 100,
    "みかん" : 80
}

total = 0

for name, price in items.items():
    print(name, "は",price,"円です")
    total += price

print("合計金額は",total,"円です。")