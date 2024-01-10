a = [1, 2, 3]
b = (1, 2, 3)
c = [4, 5, 6]
d = a + c
e = {1, 2, 3}
f = {"a", "b", "c"}
e.add("a")
e.add(6)
e.remove("a")
g = e.union(f)
print(e)
print(d)
v = {"name": "ali"}
s = set()
print(s)
dd = dict()
l = list()
print(type(s))
print(type(v))
v["age"] = 18
v.update({"age":18})
print(v.items())
v.pop("name")
print(v.items())