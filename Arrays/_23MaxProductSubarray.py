'''
Question :Given an array Arr that contains N integers (may be positive, negative or zero).
 Find the product of the maximum product subarray.
 example: Input : {6, -3, -10, 0, 2},output : 180 (6*-10*-3)
          Input : {2, 3, 4, 5, -1,0},output : 120(2*3*4*5)
Algortithm : Time complexity :O(n)
'''
def maxProduct(arr, n):
        minVal = arr[0]
        maxVal = arr[0]
        maxProduct = arr[0]
        for i in range(1, n):#O(n)
        # When multiplied by -ve number,
        # maxVal becomes minVal
        # and minVal becomes maxVal.
            if (arr[i] < 0):#we swap min and max values
                maxVal,minVal = minVal,maxVal
             
        # maxVal and minVal stores the
        # product of subarray ending at arr[i].
            maxVal = max(arr[i], maxVal * arr[i])# if now max value already -ve here it will become +ve if arr[i]<0
            minVal = min(arr[i], minVal * arr[i])
 
        # Max Product of array.
            maxProduct = max(maxProduct, maxVal)
 
    # Return maximum product
    # found in array.
        return maxProduct
if __name__ == '__main__':
    arr1 = [-6,-3,10,0,2]
    arr2 = [2,3,4,5,-1,0]
    print(maxProduct(arr1,len(arr1)))#180
    print(maxProduct(arr2,len(arr2)))#120