#include<iostream>
using namespace std;
//time complexity is O(n)
struct Pair{//using structure to return two values from function
	int min;
	int max;
};

struct Pair getMinMax(int arr[],int n){
	struct Pair minmax;
	int i;
	if(n==1){
		minmax.min=arr[0];
		minmax.max=arr[0];
	}
	if (arr[0]>arr[1]){
		minmax.min=arr[1];
		minmax.max=arr[0];
	}
	else{
		minmax.min=arr[0];
		minmax.max=arr[1];
	}
	for(i=2;i<n;i++){//loop to compare min and max values and give new and min values
		if (arr[i]>minmax.max){
			minmax.max=arr[i];
		}
		if(arr[i]<minmax.min){
			minmax.min=arr[i];
		}
	}
	return minmax;
}
int main(){

	int arr[] = {10,231,32,331,22,9,8989};
	int size =sizeof(arr)/sizeof(arr[0]);
	struct Pair minmax=getMinMax(arr,size);
	cout<<"Minimum Element of array: "<<minmax.min<<"\n";
	cout<<"Maximum Element of array: "<<minmax.max;
	return 0;
	//output
	//Minimum Element of array: 9
	//Maximum Element of array: 8989
}