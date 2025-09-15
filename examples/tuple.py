# a1 = str(input("enter movie name: "))
# a2 = str(input("enter movie name: "))
# a3 = str(input("enter movie name: "))

# print("movie names are: ", a1, a2, a3)
# list_of_movies = (a1,a2,a3)
# print("list of movies: ", list_of_movies)


# movies = []
# movies.append(input("enter first movie: "))

# print(movies)


# "pallidrome  both side same just like 121,pop,level"



# tup = [1, 2, 3, 4]
# tup.append( (5) ) 
# print(len(tup)) 


# tup = {} 
# tup[(1,2,4)] = 8
# tup[(4,2,1)] = 10
# tup[(1,2)] = 12
# sum1 = 0
# for k in tup: 
# 	sum1 += tup[k] 
# print(len(tup) + sum1)    #keys 3 and values 30 so ans is 33



# tup1 = (1, 2, 4, 3) 
# tup2 = (1, 2, 3, 4) 
# print(tup1 < tup2) # False


# tup = (1, 2, 3) 
# print(2 * tup) # Output: (1, 2, 3, 1, 2, 3)

# tup=("Check")*3
# print(tup) # Output: (CheckCheckCheck)


# s = 'geeks' 
# a, b, c, d, e = s 
# b = c = '*'
# s = (a, b, c, d, e) 
# print(s) 


# tup = (2e-04, True, False, 8, 1.001, True)
# val = 0
# for x in tup:
#     val += int(x)
# print(val)# Output: 11 - sum of int values in the tuple


# li = [3, 1, 2, 4] 
# tup = ('A', 'b', 'c', 'd') 
# li.sort() 
# counter = 0
# for x in tup: 
# 	li[counter] += int(x) 
# 	counter += 1
# 	break
# print(li) 
# # Output: [3, 1, 2, 4] - no change since break exits the loop immediately


# li = [3, 1, 2, 4] 
# tup = ('9', '7', '5', '2') 
# li.sort() 
# counter = 0
# for x in tup: 
# 	li[counter] += int(x) 
# 	counter += 1
# 	break
# print(li) 
# # Output: [10, 2, 3, 4]- no change since break exits the loop immediately



# li = [2e-04, 'a', False, 87] 
# tup = (6.22, 'boy', True, 554) 
# for i in range(len(li)): 
# 	if li[i]: 
# 		li[i] = li[i] + tup[i] 
# 	else: 
# 		tup[i] = li[i] + li[i] 
# 		break


# import sys 
# tup = tuple() 
# print(sys.getsizeof(tup), end = " ") 
# tup = (1, 2) 
# print(sys.getsizeof(tup), end = " ") 
# tup = (1, 3, (4, 5)) 
# print(sys.getsizeof(tup), end = " ") 
# tup = (1, 2, 3, 4, 5, [3, 4], 'p', '8', 9.777, (1, 3)) 
# print(sys.getsizeof(tup)) 


# tup1 = (4) 
# tup2 = (3, 4) 
# tup1 += 5
# print(tup1) #output: 9


def my_tuple(item): 
 return item.__sizeof__() 
item = (56, 35, 66, 23, 87)
print(f"The size of the tuple is: {my_tuple(item)} bytes")

