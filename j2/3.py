t = 2, 3, 4, 5, 6, 7, 8
print(type(t))
l = list(t)
l[5] = "test"
t = tuple(l)
print(t)
print(1, 2, 3)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits


print(green)
print(yellow)
print(red)

x = 10
y = 20
x, y = y, x
print(x, y)