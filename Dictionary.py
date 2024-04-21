print("Demo of Dictonary")

price = {
    "python": 2000,
    "java":1500,
    "c":1100,
    "c++":3000
}

print(price)

print(type(price))

print(price["c"])

price["c++"] = 9090

print(price)
print(price.keys())
print(price.values())
print(price.get("c++"))

# for data in price:
#     print(type(data))
#     print(price[data])