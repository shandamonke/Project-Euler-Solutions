def ispalindrome(y):
    emptyList = []
    reverseString = ''
    x = str(y)
    for k in x:
        emptyList += k
    emptyList.reverse()
    reverseString = ''.join(emptyList)
    if reverseString == x:
        return True
    else:
        return False

palindromeList = [1]

for a in range(100, 999):
    for b in range(100, 999):
        if ispalindrome(a*b) == True and a*b not in palindromeList and a*b > palindromeList[-1]:
            palindromeList.append(a*b)
            palindromeList.sort()
            print(str(palindromeList))
