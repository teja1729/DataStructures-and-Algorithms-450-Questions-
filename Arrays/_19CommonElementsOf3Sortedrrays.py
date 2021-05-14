'''
Question : Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Input:n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Algorithm : Time complexity : O(n1+n2+n3)
We use the same logic as merge in merge sort instead of merging we print common element.

'''

def commonElements (ar1,ar2,ar3, n1, n2, n3):
    i,j,k=0,0,0
    while (i < n1 and j < n2 and k<n3):#O(n1+n2+n3)
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
            print(ar1[i])
            i += 1
            j += 1
            k += 1  
        elif ar1[i] < ar2[j]:
            i += 1   
        elif ar2[j] < ar3[k]:
            j += 1 
        else:
            k += 1

if __name__ == '__main__':
    A =[1,5,10,20,40,80]
    B =[6,7,20,80,100]
    C=[3,4,15,20,30,70,80,120]
    commonElements(A,B,C,len(A),len(B),len(C))
    #Output 20 80


    
