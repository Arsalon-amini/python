#primative types are immutable (value at original memory location cannot be updated)
x = 1
print(id(x))

x = x + 1
print(id(x))

#lists are mutable
y = [1, 2, 3, 4]
print(id(y))

y.append(4)
print(id(y))
