list1=[1, 2,4, 13, 30,71, 19, 70, 80,99, 100]

def prime():
    for i in list1:
        if (i == 1):
            print("1 is neither prime nor composite")
        elif (i == 2) or (i == 3):
            print(i)
        else:
            count = 0
            for j in range(1, i):
                if ((i % j) == 0):
                    count = count + 1
            if (count == 1):
                print(i)

print("The prime numbers in the list are")
prime()


