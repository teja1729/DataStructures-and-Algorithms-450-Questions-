#Question:Given an array of integers nums containing n + 1 integers
#where each integer is in the range [1, n] inclusive.
#There is only one repeated number in nums, return this repeated number.
#input:nums = [1,3,4,2,2]
#output:2
#Algo: Time complexity is O(n)
#first we create an empty set 
#while iterating through array first we check if the number in set
#if it is already present in the set return the number
#if it is not in set add the element in set
#We used set instead of new array is because in set time complexity of searching is O(!)
def solution(array):
	set1=set()
	for i in array:#O(n)
		if i in set1:#O(1)
			return i
		set1.add(i)
if __name__ == '__main__':
	array = [1,2,3,4,2]
	duplicate_element = solution(array)
	print("duplicate element is :",duplicate_element)
	#output: duplicate element is :2