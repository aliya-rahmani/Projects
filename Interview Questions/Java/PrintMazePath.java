package com.opensource.interview;

public class PrintMazePath {

	public static void main(String[] args) {

		
		int endrow = 2, endcol = 2, currentrow = 0, currentcol = 0;
		String result = "";

		printGrid(endrow, endcol, currentrow, currentcol, result);
	}

	public static void printGrid(int er, int ec, int cr, int cc, String result) {

		/* This method prints all possible maze path
		 * @param er, ec denotes last box in grid
		 * @param cr, cc denotes current position
		 * @param result to store traversed maze path
		 */
		if (cr > er | cc > ec) {
			return;
		}
		if (cr == er && cc == ec) {
			System.out.println(result);
			return;
		}

		printGrid(er, ec, cr, cc + 1, result + "H ");
		printGrid(er, ec, cr + 1, cc, result + "V ");
	}
}



/* output:
H H V V 
H V H V 
H V V H 
V H H V 
V H V H 
V V H H 
*/

/* explanation:
* Here HHVV represent, traversing in maze in Horizontal direction twice
* then Vertical direction twice to reach the end of the grid/maze
*/