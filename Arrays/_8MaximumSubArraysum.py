#Given an array arr of N integers. Find the Maximum contiguous sub-array sum.
#INPUT:{-2, -3, 4, -1, -2, 1, 5, -3}
#OUTPUT:7
#Kadane's Algorithm :Time complexity O(n)
#Basic notion is we will compare the sum of mamximum sub array of each element with the max_global as we iterate through array
#and update max_global whenever it lower then max current
#steps:      0,i=1  2 3 4 5 6 7 
#max_current -2 -3  4 3 1 2 7 4#change of max_current in each iteration
#max_global	 -2 -2  4 4 4 4 7 4#change of max_global in each iteration
# so max_global = 4
def maxSubArraySum(a,size):
        ##Your code here
        max_current=max_global=a[0]
        for i in range(1,size):#O(n)
            max_current=max(a[i],max_current+a[i])
            if max_current>max_global:
                max_global = max_current
        return max_global
if __name__ == '__main__':
	array = [-2, -3, 4, -1, -2, 1, 5, -3]
	size = len(array)
	max_sum = maxSubArraySum(array,size)
	print("OUTPUT: ",max_sum)
	#OUTPUT: 7