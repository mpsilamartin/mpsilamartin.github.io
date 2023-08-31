x,y = [42],[1515]

# V1 :
temp = x
x = y
y = temp
print('x = ',x)
print('y = ',y)

x,y = [42],[1515]

# V2 :
x,y = y,x
print('x = ',x)
print('y = ',y)
