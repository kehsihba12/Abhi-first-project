# sort the given array or lisst

def sortingArray(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i] ,lst[i+1] = lst[i+1] , lst[i]
            
    return lst
print(sortingArray([7,8,5,6,2,1,2]))