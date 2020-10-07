/**
 * A class that implements Selection Sort
 */
public class SelectionSort {

    /**
     * Selection Sort Algorithm
     *
     * We keep track of minIndex whose value is less than others.
     * (In the "still unsorted")
     *
     * @param vals: int array
     */
    public static void selectionSort(int[] vals){
        int minIndex;
        for (int i = 0; i < vals.length-1; i++) {
            minIndex = i;
            for (int j = i+1; j < vals.length; j++) {
                if(vals[minIndex] > vals[j]){
                    minIndex = j;
                }
            }
            // helper method to swap values
            swap(vals, minIndex, i);
        }
    }

    private static void swap(int[] vals, int minIndex, int i){
        int temp = vals[i];
        vals[i] = vals[minIndex];
        vals[minIndex] = temp;
    }

    public static void main(String[] args) {
        int[] arr = {7,23,16,50,49,2,71,18};
        System.out.println("Before Selection Sort: ");
        for(int i : arr){
            System.out.print(i+" , ");
        }
        System.out.println("");
        System.out.println("After Selection Sort: ");
        selectionSort(arr);
        for(int i: arr){
            System.out.print(i+" , ");
        }
    }
}
