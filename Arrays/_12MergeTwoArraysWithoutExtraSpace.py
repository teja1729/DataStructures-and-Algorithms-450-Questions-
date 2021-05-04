#Question:Given two sorted arrays arr1[] of size N and arr2[] of size M. Each array is sorted in non-decreasing order.
# Merge the two arrays into one sorted array in non-decreasing order without using any extra space.
#Input:arr1 = [1, 3, 5, 7],arr2 = [0, 2, 6, 8, 9]
#Output: 0 1 2 3 5 6 7 8 9
#Explanation: Since you can't use any extra space, modify the given arrays to form 
#arr1 = {0, 1, 2, 3},arr2 = {5, 6, 7, 8, 9}
#Algo:Time complexity if O(mlogm+nlogn)
#first we take two variables i=n-1{last element of arr1},j=0{first element of arr1}
# now compare arr1[i],arr2[j] if arr1[i]>arr2[j],we swap as we need the arr1 elements to be small
#we increase i by 1 and decrease j by 1
# if arr1[i]<arr2[j] we break out of loop as nothing to swap
# there is nothing to swap because given arrays are sorted  so as i decreases value of arr1[i] also decrease 
#if arr1[i]<arr2[j] that means all the values of arr1[i],arr1[i-1],....arr1[0] are already lower values
#as we require arr1 to be lower valued array
#Now as we swap some numbers we sort the both arrays
def solution(arr1,arr2,n,m):
        i=n-1
        j=0
        while i>=0 and j<m:#O(max(n,m))
            if arr1[i]>=arr2[j]:
                arr1[i],arr2[j]=arr2[j],arr1[i]
                i-=1
                j+=1
            else:
                break
        arr1.sort()#O(nlogn){time complexity of merge sort}
        arr2.sort()#O(mlogm)
if __name__ == '__main__':
	arr1 = [1,3,5,7]
	arr2 = [0,2,6,8,9]
	n = len(arr1)
	m = len(arr2)
	solution(arr1,arr2,n,m)
	print(arr1+arr2)
	#Output:
	#[0,1,2,3,5,6,7,8,9]
	#Now we print their merge
