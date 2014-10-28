#include <iostream>

using namespace std;

bool isMult(int n);

int main(){
	int i;
	int sum;

	for (i = 1; i < 1000; ++i){
		if (isMult(i)){
			cout << i << " is a multiple of 3 or 5" << endl;
			sum = sum + i;
		}
	}

	cout << "The sum of all the multiples of 3 or 5 below 1000 is " << sum;
	cout << endl;
	return 0;
}

bool isMult(int n){
	if (n % 3 == 0 || n % 5 == 0) return true;
	else return false;
}
