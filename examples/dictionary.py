# d = dict() 
# for x in enumerate(range(2)): 
# 	d[x[0]] = x[1] 
# 	d[x[1]+7] = x[0] 
# print(d) 

# d = {1 : 1, 2 : '2', '1' : 1, '2' : 3} 
# d['1'] = 2
# print(d[d[d[str(d[1])]]]) 


# d = {1 : {'A' : {1 : "A"}, 2 : "B"}, 3 :"C", 'B' : "D", "D": 'E'} 
# print(d[d[d[1][2]]], end = " ") 
# print(d[d[1]["A"][2]]) 


# d = dict() 
# for i in range (3): 
# 	for j in range(2): 
# 		d[i] = j 
# print(d) 


# d = {1 : [1, 2, 3], 2: (4, 6, 8)} 
# d[1].append(4) 
# print(d[1], end = " ") 
# li = [d[2]]
# li.append(10) 
# d[2] = tuple(li) 
# print(d[2]) 


# s = "GeeksforGeeks"
# print(s[0], s[-1])


# a = {} 
# a.fromkeys(['a', 'b', 'c', 'd'], 98) 
# print (a) 


# dict ={} 
# print (all(dict)) 


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def show_bonus(self):
#         bonus = self.salary * 0.10   # 1, 10% bonus , 0.50
#         print(f"Bonus for {self.name} is {bonus}")

# e1 = Employee("Vaidehi", 50000)
# e1.show_bonus()


# a = {'geeks' : 1, 'gfg' : 2} 
# b = {'geeks' : 2, 'gfg' : 1} 
# print (a == b) 


# d = {'GFG' : 'geeksforgeeks.org', 
# 			'google' : 'google.com', 
# 			'facebook' : 'facebook.com'
# 			} 
# del d['google']; 
# for key, values in d.items(): 
# 	print(key, end=" ") 
# d.clear(); 
# for key, values in d.items(): 
# 	print(key) 
# del d; 
# for key, values in d.items(): 
# 	print(key) 


# d1 = {'Google' : 1, 
# 			'Facebook' : 2, 
# 			'Microsoft' : 3
# 			} 
# d2 = {'GFG' : 1, 
# 			'Microsoft' : 2, 
# 			'Youtube' : 3
# 			} 
# d1.update(d2); 
# for key, values in d1.items(): 
# 	print(key, values , end=" ") 


# d1 = {'GFG' : 1, 
# 			'Google' : 2, 
# 			'GFG' : 3
# 			} 
# print(d1['GFG']); 


# d = dict() 
# d['key1'] = {'key1' : 44, 'key2' : 566} 
# d['key2'] = [1, 2, 3, 4] 
# for (key, values) in d.items(): 
# 	print(values, end = "") 


# d = {'GFG' : 1, 
# 		'Facebook' : 2, 
# 		'Google' : 3
# 		} 
# for (key, values) in d.items(): 
# 	print(key, values, end = " ") 


# d = {} 
# d[(1,2,4)] = 8
# d[(4,2,1)] = 10
# d[(1,2)] = 12

# sum = 0
# for k in d: 
# 	sum += d[k] 

# print (len(d) + sum)


# a = {} 
# a[1] = 1
# a['1'] = 2
# a[1]= a[1]+1
# count = 0
# for i in a: 
# 	count += a[i] 
# print(count) 

# d = {"geek":10, "for":45, "geeks": 90} 
# print("geek" in d) 


d1 = {"john":40, "peter":45} 
d2 = {"john":466, "peter":45} 
print (d1 > d2) 
