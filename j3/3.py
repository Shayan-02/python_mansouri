d = {1 : "student", "name" : "ali", "family" : "rezaee", "age" : 20, "ismarrid" : True}
print(d)
for i in d:
    print(i, end = " ")
print()
for _ in d.values():
    print(_, end =" ")
print()
for _ in d.items():
    print(_, end = " ")

d2 = {}