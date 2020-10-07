public class InsertSort {

	/**
	 * @param args
	 */
	
	public static void insertSort(int Array[]) {
		for(int j = 1; j < Array.length; j++) {
			int key = Array[j];
			int i = j - 1;
			while(i >= 0 && Array[i] > key) {
				Array[i+1] = Array[i];
				i--;
			}
			Array[i+1] = key;
		}
	}
	
	static void printArr(int Array[]) {
		for(int i = 0; i < Array.length; i++) {
			System.out.println(Array[i]);
		}
	}
	
	public static void main(String[] args) {
		int [] arr = {100,50,2,1,8,15,7,12};
		System.out.println("Before method invocation");
		printArr(arr);

		//method invocation
		insertSort(arr);

		System.out.println("After sort method invocation");
		printArr(arr);
	}

}
