x = 1
y = 2
z = x
x = y
y = z
print(x, y)

x = int(input(1))
y = int(input(2))
x = x % y
x = x % y
y = y % x

print(y)