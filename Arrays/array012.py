#Question:Given an array of size N containing only 0s, 1s, and 2s; sort the array with using sorting algo.
#Algo: Time Complexity O(n)
#the idea is to count the no of 0's,1's,2's
#and recreate array using there counts
def solution(arr):
    fa=[0,0,0]
    for i in arr:
        if i == 0:
            fa[0]+=1
        if i == 1:
            fa[1]+=1
        if i == 2:
            fa[2]+=1
        arr = [0]*fa[0]+[1]*fa[1]+[2]*fa[2]
    return arr
if __name__=='__main__':
    array=[0,2,1,2,0]
    array = solution(array)
    for i in array:print(i,end=" ")
    #output: 0 0 1 2 2