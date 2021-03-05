#Question:Given an array, rotate the array by one position in clock-wise direction.
#INPUT:{1, 2, 3, 4, 5}
#OUTPUT:{5,1, 2, 3, 4}
#Algo:Time complexity O(n-1)
#When iterating through the array
#we swap the last element with i=0 position and i+=1
#we swap until i=n-1
def rotate(arr,n):#parameters array and length of array
    i=0#position
    while i!=n-1:#O(n-1) loop runs until i = n-1
        arr[n-1],arr[i]=arr[i],arr[n-1]
        i+=1
    return 0
if __name__=='__main__':
    array=[1,2,3,4,5]
    n=len(array)
    rotate(array,n)
    print("OUTPUT :",array)
    #output:[5,1,2,3,4]
