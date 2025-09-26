n = int(input("Enter a number: "))
prim = []
p = 2
while len(prim) < n * n:
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            break
    else:
        prim.append(p)
    p += 1

def is_prime(num: int):
    p = str(num)
    if len(p) == 1:
        return p + "  "
    elif len(p) == 2:
        return  p + " "
    elif len(p) == 3:
        return p 
    
    
idx = 0 
for i in range(1, n + 1):
    for j in range(n - i):
        print(" " + ' ' , end="")  
    for k in range(i):
        print(is_prime(prim[idx]), end=" ")
        idx += 1 
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print("", end="  ")  
    for k in range(i):
        print(is_prime(prim[idx]), end=" ")
        idx += 1
    print()




#------------------------------------------------------------

# n = int(input("Enter number of rows: "))
# for i in range(n):
#     for j in range(n - i):
#         print("*", end="")
#     for k in range(2 * i):
#         print(" ", end="")
#     for k in range(n - i):
#         print("*", end="")
#     print()
# for i in range(n - 2, -1, -1):
#     for j in range(n - i):
#         print("*", end="")
#     for k in range(2 * i):
#         print(" ", end="")
#     for k in range(n - i):
#         print("*", end="")
#     print()
