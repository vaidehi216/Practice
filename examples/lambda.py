
# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))


# data = {'a': 10, 'b': 24, 'c': 16, 'd': 15} 
# print(max(data, key =lambda  x:data[x])) 


# defining the function for removing the key in the dictionary
def rem_key(di, key):
    if key in di: 
        del di[key]
    return di 

di = {'a': 34, 'b': 56, 'c': 6734}
key = 'c'
print(f"The values in the dictionary after removing key '{key}' is: {rem_key(di, key)}")

