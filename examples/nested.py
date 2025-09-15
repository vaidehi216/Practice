# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)



adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x, y in zip(adj, fruits):
    print(x, y)
