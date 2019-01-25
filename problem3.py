import math

def decompose(x):
    for i in range(2, math.ceil(math.sqrt(x[0]))+1):
        print('for x = ' + str(x[0]) + ' checking ' + str(i)) 
        if x[0] % i == 0:
            print('success! ' + str(x[0]) + ' divided by ' + str(i))
            x.insert(0, x[0] // i)
            del x[1] 
            x.append(i)
            print('x = ' + str(x))
            decompose(x)
            quit()
    return x



argument = input('what number do you want to check?')
arg = [int(argument)]

decompose(arg)
