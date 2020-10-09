//Java program to check whether a number is harshad number or not
import java.util.Scanner;
public class harshad_number_or_not
{	
	public static void main(String[] args)
	{
		//scanner class declaration
		Scanner sc = new Scanner(System.in);
		//input from user
		System.out.print("Enter a number : ");				
		int number = sc.nextInt();
		//make a copy of original number
		int n = number;
		//declare a variable to store sum of digits
		int result = 0;
		//perform logic for calculating sum of digits of a number
		while(n != 0)
		{
			int pick_last = n % 10;
			result = result + pick_last;
			n = n / 10;
		}
		/*use condition to check whether the number entered by  
		user is completely divisible by its sum of digits or not*/
		
		if(number % result == 0)
			System.out.println("Harshad Number");
		else
			System.out.println("Not a Harshad Number");
		//closing scanner class(not compulsory, but good practice)
		sc.close();													
	}
}
