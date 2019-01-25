sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        print("sum = " + str(sum) + ", adding " + str(i)) 
        sum += i
        print("new sum = " + str(sum))


        
        
