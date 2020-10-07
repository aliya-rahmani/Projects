package com.opensource.interview;

public class Move_All_X_At_End {

	public static void main(String[] args) {

		String str = "axbdxxgfxxbcd";

		System.out.println(moveAllXatEnd(str));
	}

	public static String moveAllXatEnd(String str) {
		
		/* 
		 * This method will move all "x" character in given String to last
		 * @param str input string value
		 * @return output string with all "x" moved to end of string
		 */
		
		if (str.length() == 0) {
			return "";
		}

		// this will get first character in string
		char firstChar = str.charAt(0);
		String answer = "";

		String restAnswer = moveAllXatEnd(str.substring(1));
		
		if (firstChar == 'x') {
			answer = restAnswer + 'x';
		} else {
			answer = firstChar + restAnswer;
		}

		return answer;
	}
}



// output: abdgfbcdxxxxx
