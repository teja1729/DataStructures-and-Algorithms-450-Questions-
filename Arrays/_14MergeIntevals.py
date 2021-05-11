#Question 14:Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals
		   # and return an array of the non-overlapping intervals that cover all the intervals in the input.
 #example   input: [[1,3],[2,6],[8,10],[15,18]]
 #expected output: [[1,6],[8,10],[15,18]]
 #Algorithm:
 #Step1:First we sort the given array based on there first elements of subarrays
 #Step2:take a stack and append first sub array of intervals
 #Step3:traverse through intervals one by one
 #step4: while traversing pop the stack and check it with interval if they merge append there merge else append the interval
 #step5: return the stack 
 #Time complexity is O(nlogn)+O(n) = O(nlogn)
def merge(intervals):
	intervals = sorted(intervals)#O(nlogn)
	result = [intervals[0]]
	for interval in intervals[1:]:#O(n)
		if result[-1][1]>=interval[0]:#suppose [a,b],[c,d] if b<c 
			c=result.pop()
			result.append([c[0],max(interval[1],c[1])])#append([a,max(b,d)])
		else:
			result.append(interval)
	return result
if __name__ == '__main__':
	intervals = [[1,3],[2,6],[8,10],[15,18]]
	merged_array = merge(intervals)
	print(merged_array)
	#output :[[1,6],[8,10],[15,18]]