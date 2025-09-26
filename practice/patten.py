n = int(input("Enter the value: "))

def print_triangle(n):
    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    for i, row in enumerate(triangle):
        print(" " * (n - i), end=" ") 
        print(" ".join(str(x) for x in row))

print_triangle(n) 



# from math import factorial
# n = 5
# for i in range(n):
#     for j in range(n-i+1):
#         print(end=" ")

#     for j in range(i+1):
#         print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
#     print()