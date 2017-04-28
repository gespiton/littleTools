def fib(num):
    li = [0, 1]
    for i in range(num):
        li.append(li[-1] + li[-2])
    print(li)


li = [4]
li *= 5
print(li)
fib(4)
