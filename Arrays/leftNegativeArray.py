#Question:An array contains both positive and negative numbers in random order. 
# Rearrange the array elements so that all negative numbers appear before all positive numbers.
#Input:-[-12,11,-13,-5,6,-7,5,-3,-6]
#Output:-[-12,-13,-5,-7,-3,-6,11,6,5]
#Algo:Time_complexity O(n)
#j=0,as we iterate through array if we encounter negative value
#we swap the value with array[j] that means first element and j=j+1
#next time we encounter negative we swap it array[j] that means 2nd element
#at the end of loop we get all negative values to the left
def solution(array):
    n=len(array)
    j=0
    for i in range(0,n):#O(n)
        if array[i]<0:
            array[i],array[j]=array[j],array[i]#swapping elements
            j=j+1
    return array
if __name__ =='__main__':
    array = [-12,11,-13,-5,6,-7,5,-3,-6]
    array = solution(array)
    print(array)
#output
#[-12,-13,-5,-7,-3,-6,11,6,5]