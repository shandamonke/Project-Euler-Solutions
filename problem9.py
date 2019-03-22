import math

for a in range(1,1001):
    for b in range(1, 1001):
        if a + b + math.sqrt(a ** 2 + b ** 2) == 1000:
            print('a = ' + str(a) + 'b = ' + str(b))
            c = math.sqrt(a ** 2 + b ** 2)
            print(math.sqrt(a ** 2 + b ** 2))
            print('answer = ' + str(a * b * c))
