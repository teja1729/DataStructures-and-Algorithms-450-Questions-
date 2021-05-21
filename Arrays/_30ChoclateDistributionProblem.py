'''
Question:Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet.
Each packet can have a variable number of chocolates.
There are M students, the task is to distribute chocolate packets among M students such that :
1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum
Example:
Input:
N = 8, M = 5
A = {3, 4, 1, 9, 56, 7, 9, 12}
Output: 6
Explanation: The minimum difference between 
maximum chocolates and minimum chocolates 
is 9 - 3 = 6 by choosing following M packets :
{3, 4, 9, 7, 9}.
Algorithm: Time complexity :O(nlogn)
Step1: We sort the array so that we have least values at the beginning
Step2: Take to pointers pos1 =0,pos2 =M+pos1-1 such that size of array is M
Step3: let minimum difference diff = 99999(Very large value)
Step4: As we traverse through the array and find difference and if it is minimum then the present diff update diff
Step5:return diff

'''
def findMinDiff(A,N,M):
        A = sorted(A)#O(nlogn)
        pos1 = 0
        pos2 = M+pos1-1
        diff = 99999
        while pos2<N:#O(N-M)
            t = A[pos2]-A[pos1]
            diff = min(t,diff)
            pos1+=1
            pos2+=1
        return diff
if __name__=='__main__':
	A =[3, 4, 1, 9, 56, 7, 9, 12]
	M =5
	N =8
	print(findMinDiff(A,N,M))
	#Output:3(9-6)