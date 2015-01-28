/*
   Project Euler Problem 5:
   What is the smallest positive number that is evenly divisible
   by all of the numbers from 1 to 20?

   Marcus Yeagle - marcusnyeagle@gmail.com
*/

#include <iostream>

using namespace std;

bool isDiv(int n);

int main(){
	int n = 1;
	while (!isDiv(n)) ++n;
	return 0;
}

// This function checks whether an integer is divisible by all integers up to 20
// If it is divisible for all ints then it prints out the original test integer
// and returns true
//
bool isDiv(int n){
	for (int i = 1; i < 21; ++i){
		if (n % i != 0) return false;
	}
	cout << n << endl;
	return true;
}
