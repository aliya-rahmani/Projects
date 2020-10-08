using System;
					
public class Program
{
	public static void Main()
	{
		Console.WriteLine("Palindrome checking program!");
		bool programIsOn = true;
		while(programIsOn){
			Console.WriteLine("Enter text to check:");
			string inputText = Console.ReadLine();

			char[] charArray = inputText.ToCharArray();
			Array.Reverse(charArray);
			string reverseText = new string(charArray);
			
			bool isPalindrome = inputText.Equals(reverseText, StringComparison.OrdinalIgnoreCase);
			if (isPalindrome) 
				Console.WriteLine( inputText + " is a Palindrome!");
			else 
				Console.WriteLine(inputText + " is not a Palindrome!");     

			Console.WriteLine("Still want to check? (y to continue, else press any key to quit)");
			string isProgramStillOn = Console.ReadLine();
			
			if(!isProgramStillOn.Equals("y", StringComparison.OrdinalIgnoreCase))
				programIsOn = false;
		}
		Console.WriteLine("Bye!");
	}
}