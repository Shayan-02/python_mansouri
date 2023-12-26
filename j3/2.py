# i = 0
# while i < 10:
#     if i == 6:
#         continue
#     if i == 8:
#         break
#     print(i)
#     i += 1

# for i in range(10):
#     if i == 8:
#         break
#     if i == 6:
#         continue
#     print(i)
s1 = {"a", "b", "c", "d", "e", "f"}
lst = []
l = int(input("Enter the list length: "))
i = 1
while i <= l:
    b = int(input(f"Enter number{i}: "))
    lst.append(b)
    i += 1
print(lst)
s = set(lst)
print(s)
# s2 = s1.union(s)
t = tuple(s)
t2 = [2, 4, 5, 6]
t2[2] = 4