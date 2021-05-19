'''Question:Given an array arr of size n and an integer X.
 Find if there's a triplet in the array which sums up to the given integer X.
 Example input : [1 4 45 6 10 8],x =13
 		 output: True(1,+4+8 ==13)
Algorithm : Timecomplexity O(n^2)
step1: we sort the array
step2: as we traverse through the array 
step3: apply two pointer method two on the rest of elements in each iteration,pos1 =i+1,pos2 =n-1
step4: if sum1 = arr[i]+arr[pos1]+arr[pos2] ,sum1 > x greater than expected so to reduce the sum we update pos2-=1
step5: sum1<x lesser than expected so to increase the sum we update pos1+=1
'''
def threeSum(arr, n, X):#array = arr, n = length of array , X  = target 
        arr = sorted(arr)
        for i in range(n):
            pos1 = i+1
            pos2 = n-1
            while pos1<pos2:
                sum1 = arr[i]+arr[pos1]+arr[pos2]
                if sum1 == X:
                    return True,(arr[i],arr[pos1],arr[pos2])
                if sum1>X:
                    pos2-=1
                else:
                    pos1+=1
        return False
if __name__ =='__main__':
	arr1 = [1,4,45,6,10,8]
	n = len(arr1)
	X = 13
	bool_value,triplet = threeSum(arr1,n,X)
	print(bool_value)#True
	print(triplet)#(1,4,8)
