lst1=[1,2,3,4,5]
lst2=[10,20,30,40,50]

d = {x: y for x, y in zip(lst1, lst2)}

print(d)

f = ("blue", "red", "green", "yellow", "gray")
x, y, *z = f
print(z)

