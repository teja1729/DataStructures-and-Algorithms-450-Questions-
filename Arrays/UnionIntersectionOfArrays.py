#Question:Give union and intersection of two arrays
#Union of two arrays
#Algo:time complexity O(m+n+c) where m,n sizes of two arrays,c=n(aub)(no of elements)
#First we define an empty set
#and we add elements into set as repetitions are not allowed in set(we will ignore duplicates)
def union(a,b):
    set1=set()
    for i in a:#O(a)
        set1.add(i)
    for i in b:#O(b)
        set1.add(i)
    return list(set1)#O(c)
#intersection 
#Algo time complexity O(m+n):
#first we add one array elements in set
#second we iterate through second array and check whether the element is present in the set
#append those elements common to list and return list
def intersection(a,b):
    set2=set()
    list1=[]
    for i in a:#O(m)
        set2.add(i)
    for j in b:#O(n)
        if j in set2:#O(1) time complexity to search in set
            list1.append(j)
    return list1
if __name__=='__main__':
    array1={1,1,2,4,5,2,8}
    array2={33,1,1,4,4,90,77}
    union_arrays=union(array1,array2)
    intersection_arrays=intersection(array1,array2)
    print("Union Of Arrays :",union_arrays)
    print("Intersection Of Arrays : ",intersection_arrays)
#Output:
#Union Of Arrays : [1, 2, 33, 4, 5, 8, 77, 90]
#Intersection Of Arrays :  [1, 4]
