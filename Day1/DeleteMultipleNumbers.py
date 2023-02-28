list1 = [1, 4, 10, 30, 60, 70, 80 , 100]
Delete_ind=[3,7,4]
print("indexes to be deleted: ",Delete_ind)
a=len(Delete_ind)
print("Original list: ",list1)
for i in range(a):
    #print("The position of {} is {}".format(i,list1[3]))
    for j in range(a):
        if(Delete_ind[i]>Delete_ind[j]):
            temp= Delete_ind[i]
            Delete_ind[i]= Delete_ind[j]
            Delete_ind[j]=temp
print("Ordered index list: ", Delete_ind)
for i in range(a):
    list1.pop(Delete_ind[i])
print("After removing elements: ",list1)