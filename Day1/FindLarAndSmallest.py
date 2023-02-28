#no=list(input("Enter the numbers"))
#no=[30,20,9,45,12]
no=[]
count=int(input("Enter the no.of elements:"))
for i in range(0,count):
    ele = int(input("Enter the no"))
    no.append(ele)
print("Entered list ",no)
a=len(no)
for i in range(a):
    for j in range(a):
        if(no[i]>no[j]):
            temp=no[i]
            no[i]=no[j]
            no[j]=temp
print("Ordered list: ",no)
print('The Largest number in the list: ',no[0])
print('The Second Largest number in the list: ',no[1])
print('The smallest number in the list:', no[a-1])



