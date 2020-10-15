import java.util.Arrays;
import java.util.Scanner;

public class PigeonHoleSort {
	
	public static void pigeonHoleSort(int[] arr, int n)
	{
        // Find the min and max values in the given array
		int min = Integer.MAX_VALUE;
		int max = Integer.MIN_VALUE;
		for(int i = 0; i < n; i++)
		{
			if(arr[i] > max)
				max = arr[i];
			else if(arr[i] < min)
				min = arr[i];
		}
		
        // Find the range of numbers and create pigeonHoles accordingly
		int numRange = max - min + 1;
		int[] pigeonHoles = new int[numRange];
		Arrays.fill(pigeonHoles, 0);
    
        // Iterate through the array and increment the counter in appropriate pigeonHoles
		for(int i = 0; i < n; i++)
			pigeonHoles[arr[i] - min]++;
		
		int j = 0;
		for(int i = 0; i < numRange; i++)
		{
			while(pigeonHoles[i]-- > 0)
				arr[j++] = min + i;
		}
	}
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter size of array...");
		int n = sc.nextInt();
		int arr[] = new int[n];
		System.out.println("Enter the array elements...");
		for(int i = 0; i < n; i++)
		{
			arr[i] = sc.nextInt();
		}
		System.out.println("Unsorted Array: " + Arrays.toString(arr));
		
		pigeonHoleSort(arr, n);
		System.out.println("Sorted Array: " + Arrays.toString(arr));
		
		/* Sample Output
		Enter size of array...
		7
		Enter the array elements...
		5 25 39 11 13 39 5
		Unsorted Array: [5, 25, 39, 11, 13, 39, 5]
		Sorted Array: [5, 5, 11, 13, 25, 39, 39]
		*/
	}
}
