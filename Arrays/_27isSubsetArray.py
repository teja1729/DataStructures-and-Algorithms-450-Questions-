'''Question:Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m. Task is to check whether a2[] is a subset of a1[] or not.
 Both the arrays can be sorted or unsorted.It may be assumed that elements in both array are distinct.
Example : Inpout: a1 ={11, 1, 13, 21, 3, 7},a2={11, 3, 7, 1} ,Output: Yes(a2 is subset of a1)
Algorithm:
step1: define count = 0 , set1 = set(a1) as searching in set is O(1)
step2: as we traverse a2 count+=1 if a2[i] lies in set1:
step3: if count == len(a2) that means return True else False
 '''
def isSubset(a1, a2, n, m):
    set1 = set(a1)
    count =0
    for i in range(m):#O(n)
        if a2[i] in set1:#O(1)
            count+=1
    if count==m:
        return 'Yes'
    else:
        return 'No'
if __name__ =='__main__':
	a1 = [11,1,13,21,3,7]
	a2 = [11,3,7,1]
	n  = len(a1)
	m  = len(a2)
	print(isSubset(a2,a2,n,m))
	#Output : Yes