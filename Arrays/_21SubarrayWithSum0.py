'''
Question:Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.
example Input : [4 2 -3 1 6]  Input: [4 2 0 1 6]
		output: Yes		      Output:Yes
Algorithm: Time complexity = O(n)
Step 1 : Take a set and sum  =0 
Step 2  : as we traverse array we do add arr[i] to sum  and check if it is 0 or if sum already exists,then we return True
Step 3: if sum not is in set we add to set 
Step 4 : return false if we didn't got any answer

'''
def solution(arr):
	set1 = set()
	sum1 = 0
	for i in range(len(arr)):#O(n)
		sum1+=arr[i]
		if sum1==0 or sum1 in set1:#if sum1 = 0 subarray is exists with sum =0,sum1 is already exist means
			return True            #for that sum to now the subarray sum is 0
		set1.add(sum1)
	return False   
if __name__ =='__main__':
	arr = [4,2,-3,1,6]
	print(solution(arr))#Output: True
	arr1=[4,2,0,1,6]
	print(solution(arr1))#Output: True