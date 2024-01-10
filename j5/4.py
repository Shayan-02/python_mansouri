def sayHello(number):
    print("hello" , number)

def sayHello2():
    for i in range(1, 11):
        sayHello(i)

def sums(a, b):
    global c
    c = a + b
    print(c)

sums(5, 6)
print(c)