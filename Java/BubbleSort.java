public class BubbleSort {

	/**
	 * @param args
	 */
	
	public static void bubbleSort(int Array[]) {
		int len = Array.length; 
        for (int i = 0; i < len-1; i++) { 
            for (int j = 0; j < len-i-1; j++) {
                if (Array[j] > Array[j+1]) { 
                    int temp = Array[j]; 
                    Array[j] = Array[j+1]; 
                    Array[j+1] = temp; 
                }
            }
        }
	}
	
	static void printArr(int Array[]) {
		for(int i = 0; i < Array.length; i++) {
			System.out.println(Array[i]);
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] arr = {100,50,2,1,8,15,7,12};
		System.out.println("Before method invocation");
		printArr(arr);
		
		//method invocation
		bubbleSort(arr);
		
		System.out.println("After sort method invocation");
		printArr(arr);
	}

}
