fib = [1,2]
sum = 0
while fib[1] < 4000000:
    newFib = fib[0] + fib[1]
    fib[0] = fib[1]
    fib[1] = newFib
    print('fib = ' + str(fib))
    if newFib % 2 == 0:
        print("adding " + str(newFib) + " to current sum: " + str(sum))
        sum += newFib
print('solution = ' + str(sum))
