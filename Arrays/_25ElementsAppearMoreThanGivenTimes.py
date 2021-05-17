'''
Question: Given an array arr[] of size N and an element k.
 The task is to find all elements in array that appear more than n/k times.
example : Input :[3,1,2,2,1,2,3,3] ,k=4 Output = 2 (2,3 whose frequency is greater than 2)
Algorithm: TimeComplexity:O(n)
step1: create a frequency dictionary
step2: traverse through dictionary and count where frequency > n//k
step3: return count
'''
def countOccurence(arr,n,k):
         dict1 = {}
        for i in range(n):#O(n)creating a frequency dictionary
            if arr[i] in dict1:
                dict1[arr[i]]+=1
            else:
                dict1[arr[i]]=1
        c = n//k
        count =0
        for a,b in dict1.items():#O(n) checking values where frequency is > c
            if b>c:
                count+=1
        return count
if __name__ = '__main__':
    arr = [3,1,2,2,1,2,3,3]
    n = len(arr)
    k = 4
    print(countOccurence)#output : 2