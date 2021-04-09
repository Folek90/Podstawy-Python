"""
a = b = c = 10
print (a, b, c)
print("Is value the same?", a == b == c == a)
print("Are the variables the samne?", id(a), id(b), id(c))

a = 20

print(a, b, c)
print("Is the value the same?", a == b == c == a)
print("Are the variables the same?", a is b, b is c, c is a)
print(id(a), id(b), id(c))


a = b = c = [1, 2, 3]
print(a, b, c)
print(id(a), id(b), id(c))
a.append(4) 
print(a, b, c)
print(id(a), id(b), id(c))
print("Is the value the same?", a==b, b==c, c==a)
print("Are the variables the same?", a is b, b is c, c is a)
"""

x = 10
y = 10
print(id(x), id(y))

y = (y + 1 - 1)
print(id(y))
y = (y + 1234567890 - 1234567890)
print(id(x), id(y))
