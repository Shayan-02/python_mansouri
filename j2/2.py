
a = "hello world!... hi"
print(a[10:2:-2])
print(a[::-1]) # reverse

print(a[6])

lst = [1, 2, 3, [4, "ali", "rezaee", 20], 5, 6]
print(lst[3][2])
lst[3][2] = "akbari"
print(lst)
lst.insert(1, "reza")
# lst.clear()
print(lst)
lst2 = [[1, 2, 3], [4, 4, 6], [7, 8, 9]]

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

a = [1, 2, 3]
b = a.copy()
c = list(b)
print(c)
print(b)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list3.reverse()
print(list3)