'''
Question : Given an array of N integers, and an integer K, 
find the number of pairs of elements in the array whose sum is equal to K.
example: Input ([1,5,7,1],6) output is 2-(1,5),(5,1)
Timecomplexity : O(n)
Algorithm:
Step1: We first create a frequecncy dictionary which has frequency of each element in array and set of array elements
Step2: traversing the array if k - arr[i] in set then add count = frequency of that element
Step3: if k-arr[i]=arr[i] we reduce count by 1 to negate the duplicates

'''
#Solution
def getPairsCount( arr, n, k):
        set1=set(arr)
        dict1 = {}
        for x in set1:
            dict1[x] = 0
        for i in arr:
            dict1[i]+=1
        twice_count = 0
        for i in range(n):#O(n)
            if k - arr[i] in set1:
                twice_count +=dict1[k-arr[i]]
                if (k-arr[i]==arr[i]):
                    twice_count-=1
        return int(twice_count/2)
if __name__ == '__main__':
    arr  = [1,5,7,1]
    arr1 = [1,1,1,1]
    print(getPairsCount(arr,len(arr),6))
    print(getPairsCount(arr1,len(arr1),2))
    #2
    #6
