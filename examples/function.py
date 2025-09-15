# def cal_sum(a, b):
#     return a + b

# sum_result = cal_sum(5, 10)
# print(sum_result)


# cities = ["mumbai", "delhi", "surat", "pune", "bangalore"]

# def print_len(list):
#     print(len(cities))
# print_len(cities)



# def cal_fact(n):
#     factorial = 1
#     for i in range(1, n + 1):       
#         factorial *= i
#     print(factorial)
# cal_fact(5)


# def covertor(usd_val):
#     inr_val = usd_val * 84
#     print(usd_val, "USD is equal to", inr_val, "INR")
# covertor(28.77)



# def even_odd(num):
#     rem = num % 2
#     if rem == 0:
#         return f"{num} is an even number"
#     else:
#         return f"{num} is an odd number"
# print(even_odd(545))


# n = int(input("Enter the number: "))
# def is_even(num):
#     return num % 2 == 0
# def is_odd(num):
#     return num % 2 != 0
# if is_even(int(n)):
#     print(f"{n} is an even number")
# else:
#     print(f"{n} is an odd number")  



def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        return x
    return inner

closure = outer()
print(closure())
print(closure())
