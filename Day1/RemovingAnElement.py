nos=[1,2,1,1,4,5]
nsize =len(nos)
x=True
print("Original list: ",nos)
for i in range(nsize):
    for j in range(1,nsize):
        if(nos[i]==nos[j]):
            x=False
            print("The number repeated at the index of", j)
            print("The number repeated at the place of",j+1)
            nos.pop(j)
            print("After removing an element from the list: ",nos)
            break
    if(x==False):
        break
