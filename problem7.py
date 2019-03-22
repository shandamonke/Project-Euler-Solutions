# brute force solution



# a function that returns True or False based on primacy of integer input
def isprime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
            break
    return True


# find prime numbers
checkedNumber = 5
primeList = [2, 3]
primeCount = 2

while primeCount < 10001:
    if isprime(checkedNumber) == True:
        primeCount += 1
        print('primeCount = ' + str(primeCount))
        primeList.append(checkedNumber)
        checkedNumber += 2
    else:
        checkedNumber += 2

print('10001st = ' + str(primeList[-1]))
