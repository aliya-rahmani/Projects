import java.util.Random;

public class counting_sort {
    public int[] countingSort(int []a){
        int [] count,b;
        count = new int[10000];
        b = new int[10000];
        for(int i=0;i<10000;i++)
            count[a[i]]++;
        for(int i=1;i<10000;i++)
            count[i]+=count[i-1];
        for(int i=a.length-1;i>=0;i--){
            b[count[a[i]]-1] = a[i];
            count[a[i]]--;
        }
        return b;
    }
    public static void main(String[] args) {
        Random rand = new Random();
        counting_sort obj = new counting_sort();
        int[] a = new int[10000];
        for(int i=0;i<10000;i++)
            a[i]= rand.nextInt(10000);
        long startTime = System.nanoTime();
        a = obj.countingSort(a);
        long endTime = System.nanoTime();
        System.out.println("Time taken = "+(endTime-startTime)/1000);
    }
}