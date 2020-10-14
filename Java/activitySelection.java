import java.util.*;

public class activitySelection {
    public static void maxActivity(int s[], int f[], int n) 
    { 
    int i=0; 
    System.out.print("\nSelected activities are ("+ s[i]+","+f[i]+") "); 
    for (int j = 1; j < n; j++) 
        { 
        if (s[j] >= f[i]) 
            { 
                System.out.print("("+ s[j]+","+f[j]+") "); 
              i = j; 
            } 
        } 
    } 
    public static void sortArrayByFinishTime(int arr[][], int j) 
    { 
        Arrays.sort(arr, new Comparator<int[]>() { 
          public int compare( int[] array1, int[] array2) { 
            if (array1[j] > array2[j]) 
                return 1; 
            else
                return -1; 
          } 
        });
    }
    public static void main(String[] args) 
    {
    Random rand = new Random();
    int s[] = new int[50+rand.nextInt(50)]; 
    int n = s.length;
    int f[] = new int[n];
    int arr[][]= new int[n][2];
    for(int i=0;i<n;i++){
                arr[i][0]=1+rand.nextInt(95);
                arr[i][1]=arr[i][0]+1+rand.nextInt(5);
    }
    sortArrayByFinishTime(arr,1); 
    for(int i=0;i<n;i++)
        for(int j=0;j<2;j++){
            if(j==0)
                s[i]=arr[i][j];
            else
                f[i]=arr[i][j];
    }
    System.out.println("Starting Time : ");
    for(int i=0;i<n;i++)
        System.out.print(s[i]+" ");
    System.out.println("\nFinish Time   : ");
    for(int i=0;i<n;i++)
        System.out.print(f[i]+" ");
    maxActivity(s, f, n); 
    } 
}
