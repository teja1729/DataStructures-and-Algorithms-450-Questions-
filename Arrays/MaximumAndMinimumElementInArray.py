def getMinMax(arr):#function to get min and max

    n = len(arr)
    #python inbuilt functions min and max also use loops to get values and time complexity is O(n)
    #if len of array even intialize minmum(mn),maximum(max) to minimum and maximum of first two array elements
    #if it is odd we intialize mn,mx to array first element(arr[0])
    if n%2==0:
        mn= min(arr[0],arr[1])
        mx=max(arr[0],arr[1])
        i=2#starting index of loop
    else:
        mn=mx=arr[0]
        i = 1#starting index of loop
    while(i<n):#in the loog every element is compared and change values 
        if arr[i]<=mn:
            mn=arr[i]
        if arr[i]>=mx:
            mx=arr[i]
        i+=1
    return mn,mx
if __name__=='__main__':
    array = [100,45,123,33,101,19,8,123533]
    mn,mx = getMinMax(array)
    print("Maximum element in array: ",mx)
    print("Minimum element in array: ",mn)
    #output
    #Maximum element in array: 123533
    #Minimum element in array:  8 



