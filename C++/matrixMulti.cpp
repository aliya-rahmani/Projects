#include <iostream>
using namespace std;

int main() {
	const int column1(2), column2(2), row1(2), row2(2);

	int arraya[row1][column1] = { {1,2},
										  {3,4} };
	int arrayb[row2][column2] = { {5,6},
										  {7,8} };

	int arrayc[2][2];

	if (column1 != row2) {
		cout << "Matrices cannot be multipled together";

	}
	else {


		for (int i = 0; i < row1; ++i) {
			for (int j = 0; j < column2; ++j) {
				arrayc[i][j] = 0;
				//populates product 2d array with correct number of zeros
			}
		}

		for (int i = 0; i < row1; ++i) {
			for (int j = 0; j < column2; ++j) {
				for (int k = 0; k < column1; ++k) {
					arrayc[i][j] += arraya[i][k] * arrayb[k][j];
					//multiplies element from array a with element from array b and adds into arrayc

					//i and k for a are the top two numbers 
					// k and j for b are the down two number				

				}


			}
		}


			for (int i = 0; i < row1; ++i) {
				for (int j = 0; j < column2; ++j) {
					cout << arrayc[i][j] << "\t";
				}
				//prints out new array c
			}
		//i am testing the merge function


	}

	
	return 0;
}