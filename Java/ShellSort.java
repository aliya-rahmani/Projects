import java.util.Scanner;

public class ShellSort {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");

        int length = sc.nextInt();
        int[] intArray = new int[length];

        System.out.print("Enter the array elements: ");

        for (int i = 0; i < intArray.length; i++) {
            intArray[i] = sc.nextInt();
        }

        for (int firstUnsortedIndex = 1; firstUnsortedIndex < intArray.length; firstUnsortedIndex++) {
            int newElement = intArray[firstUnsortedIndex];
            int i;

            for (i = firstUnsortedIndex; i > 0 && intArray[i - 1] > newElement; i--) {
                intArray[i] = intArray[i - 1];
            }
            intArray[i] = newElement;

        }

        System.out.print("Sorted array: ");
        for (int i = 0; i < intArray.length; i++) {
            System.out.print(intArray[i] + " ");
        }

    }

}
