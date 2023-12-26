list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

dict1 = {k: v for k, v in zip(list1, list2)}
print(dict1)