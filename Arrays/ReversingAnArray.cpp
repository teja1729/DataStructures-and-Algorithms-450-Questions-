#include<iostream>
using namespace std;
/*input={1,2,3,4,5,6,7,8}
  output={8,7,6,5,4,3,2,1}
  algorithm:
  step1:take array ,start pos,end pos
  step2:swap values in start and end
  step3:in loop reduce end value by -1 each time and
  increase start value by +1 each time untill(start<end)
*/


void reverseArray(int arr[],int start,int end){//three parameters array,starting,end positions of array
	while(start<end){
		int temp = arr[start];
		arr[start]=arr[end];
		arr[end]=temp;
		start++;
		end--;
	}
}
int main(){

	int array[] = {1,2,3,4,5,6,7,8};
	int size = sizeof(array)/sizeof(array[0]);//sizeofarray/sizeofdatatype
	reverseArray(array,0,size-1);
	//printing array
	for(int i=0;i<size;i++){
		cout<<array[i]<<" ";
	}

	return 0;
}