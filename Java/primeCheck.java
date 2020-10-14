/**
	Description: check if a input number is prime or not
*/

import java.util.Scanner;

public class primeCheck {
	

	// prime method, checks for prime and output result, takes n as input
	public static int primecheck(int n)
	{
		int flag = 0;
			
		// checking for prime
		for (int i = 2; i <= n/2; i++)
		{
			if(n%i == 0)
			{
				flag = 1;
				break;
			}
			
		}
		 return flag;
	}


	// main method
	public static void main(String[] args)
	{
		int num, flag;
		Scanner sc = new Scanner(System.in);

		System.out.println("Enter a number to check: ");
		num = sc.nextInt();

		// calling primecheck method with num as argument
		flag = primecheck(num);

		if (flag == 0)
			System.out.println(num + " is prime.");
		else
			System.out.println(num + " is not prime.");				
	}
}
