sumSquared = 0
sumSquares = 0


# calculate the sum of all squares
for i in range(1,101):
    sumSquares += i * i
    print('sumSquares += ' + str(i*i))
    print('sumSquares' + str(sumSquares))
print('final sumSquares = ' + str(sumSquares))

# calculate sum of 1 - 100 and square it
for i in range(1,101):
    sumSquared += i
    print('sumSquared += ' + str(i))
    print('sumSquared' + str(sumSquared))
print('sumSquared sum = ' + str(sumSquared))
sumSquared = sumSquared * sumSquared
print('final sumSquared = ' + str(sumSquared))

# calculate the difference
finaldiff = sumSquared - sumSquares
print('final answer = ' + str(finaldiff))

