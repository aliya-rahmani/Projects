/**
	Description: This program takes two number and a choic to perform four operations and uses four methods to perform addition, subtraction, division and multiplication, the result is returned from the methods and is displayed.
*/

// importing java util library
import java.util.*;

public class calculator {

// add method
public static float add(float num1, float num2)
	{
		return num1+num2;
	}

// subtract method
public static float subtract(float num1, float num2)
	{
		return num1-num2;
	}

// divide method
public static float divide(float num1, float num2)
	{
		if (num2 == 0)
			return -1; // if num2 is 0
		else
			return num1/num2;
	}

// multiply method
public static float multiply(float num1, float num2)
	{
		return num1*num2;
	}

// main method
public static void main(String[] args)
	{
		float num1, num2, res = 0;
		int  op;

		Scanner sc = new Scanner(System.in);

		// input prompt
		System.out.println("Enter two numbers: ");
		num1 = sc.nextFloat();
		num2 = sc.nextFloat();

		// input operation
		System.out.println("\nChoose the operation(enter choice number): \n1. Addition \n2. Subtraction \n3. Division \n4. Multiplication");
		op = sc.nextInt();

		// checking choice
		if (op == 1)
			res = add(num1,num2);
		
		else if (op == 2)
			res = subtract(num1,num2);

		else if (op == 3)
				res = divide(num1,num2);

		else if (op == 4)
			res = multiply(num1,num2);
		
		else
			System.out.println("\nInvalid choice.");

		// result output
		if (res == -1)
			System.out.println("\nDenominator is 0, cannot perform division.");
		else
			System.out.println("The result is : " + res);
	}

}
