print('{0:.2}'.format(1.0 / 3))
print ('{0:-2%}'.format(1.0 / 3))




i = 0
while i < 3: 
	print(i,end=' ') 
	i += 1
else: 
	print(0)
      


	
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)



print('cd'.partition('cd'))
print('abef'.partition('cd'))
print('abcefd'.replace('cd', '12'))



def f(value, values):
    v = 1
    values[0] = 44
a = 3
v = [1, 2, 3]
f(a, v)
print(a, v[0])




print(tuple[1:3] if tuple == ( 'abcd', 786 , 2.23, 'john', 70.2 ) else tuple())
