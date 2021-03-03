#Question:Find the Kth minmum and maximum element in given Array
#Algo: first we sort the given array.
#for kth min arr[k-1] as indexing starting from 0
#for kth max arr[len(arr)-k] suppose len(arr) =10 and 1st max is last element which is 10-1=9
#time complexity O(nlogn)
def kthMinMaxInArray(array,K):
    array=sorted(array)
    return array[k-1],array[len(array)-k]
if __name__== '__main__':
    arr=[1,231,313,10,2,3,80]
    k = 1
    kthmin,kthmax = kthMinMaxInArray(arr,k)
    print(f'{k}th max is {kthmax}')
    print(f'{k}th min is {kthmin}')
