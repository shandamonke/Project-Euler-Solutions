#If you ever come back to this and forget what you did, then just run the decompose / to_max_number functions and see if you remember how they work, maybe chuck some more print statements in there for explanation

import math


# A function that decomposes into prime factors; input: list containing integers; output: list containing integers

def decompose(x):
    for i in range(2, math.ceil(math.sqrt(x[0]))+1):
        print('for x = ' + str(x[0]) + ' checking ' + str(i)) 
        if x[0] % i == 0:
            x.insert(0, x[0] // i)
            del x[1] 
            x.append(i)
            print('x = ' + str(x))
            decompose(x)
    return x


# A function that takes input of a maximum number and produces a nested list of prime factors of each of those numbers

def to_max_number(x):
    primeFactorList = []
    for i in range(2, x + 1):
        print('checking i = ' + str(i))
        primeFactorList.append(decompose([i]))
    for k in primeFactorList:
        if k[0] == 1:
            del k[0]
    print('pfl = ' + str(primeFactorList))
    return primeFactorList        

# A function that creates the list of prime factors of the final answer, takes the nested list of prime factors, iterates over it to tally the number of each prime factor and replaces the values in the list of prime factors as needed

def main(x):
    
    # create baseline answerList
    answerList = []
    nestedList = to_max_number(x)
    for j in range(len(nestedList)*len(nestedList)):
        answerList.append(0)
    print('len answerList' + str(len(answerList)))

    # start applying counts
    for i in nestedList:
        for k in i:
            print('for ' + str(k) + ' in ' + str(i))
            if answerList[k] < i.count(k):
                print('replacing ' + str(answerList[k]) + ' with ' + str(i.count(k)))
                answerList[k] = i.count(k) 
                print('new aL = ' + str(answerList))
    
    #start summing
    total = 1
    for l in range(len(answerList)):
        if answerList[l] != 0:
            print('total = ' + str(total))
            total = total * l ** answerList[l]
            print('l = ' + str(l) + ', answerList[l] = ' + str(answerList[l]))
            print('total (added) = ' + str(total))
    print('THE FINAL ANSWER IS ' + str(total))

        
to_max_number(5)


main(20)
