#include <iostream>

using namespace std; 

int main(){
	int d,n;
	for (int i = 100; i < 999; ++i){
		for (int j = 100; j < 999; ++j){
			n = i * j;
			int a[6];
			for (int m = 0; m < 6; ++m){
				d = n % 10;
				a[m] = d;
				n = n - d;
				n = n / 10; 
			}	
			if (a[0] == a[5] && a[1] == a[4] && a[2] == a[3]){
				cout << i * j << " is a palindrome" << endl; 
			}
		}
	}
	return 0;
}

