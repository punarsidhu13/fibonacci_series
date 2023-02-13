def fib_series(n):
    x = 0
    print(x)
    y = 1 
    print(y)
    for i in range(n-2):
        temp = y
        y = x + y
        x = temp
        print(y)

num = int(input("Enter a number \n "))
fib_series(num)