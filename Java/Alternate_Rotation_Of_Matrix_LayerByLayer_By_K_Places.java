import java.io.*;
import java.util.*;

public class  Alternate_Rotation_Of_Matrix_LayerByLayer_By_K_Places{
	public static void main(String args[]) throws IOException{
     	Scanner sc = new Scanner(System.in);
     	int m = sc.nextInt();
     	int n = sc.nextInt();
     	int ar[][] = new int[m][n];
     	
     	for(int i =0;i<m;i++) {
     		for(int j =0;j<n;j++) {
     			ar[i][j] = sc.nextInt();
     		}
     	}
     	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
     	String[] s = br.readLine().split(" ");
     	int size = s.length;
     	int l[] = new int[s.length];
     	for(int i=0;i<s.length;i++) {
     		l[i] = Integer.parseInt(s[i]);
     		int[] temp = new int[(m-1-i*2)*2 + (n-1-i*2)*2];
     		int val =0;
     		for(int j =0+i;j<m-i; j++) {
     			temp[val++] = ar[j][i];
     		}
     		for(int j =1+i; j<n-i-1;j++) {
     			temp[val++] = ar[m-1-i][j];
     		}
     		for(int j =m-i-1;j>=0+i; j--) {
     			temp[val++] = ar[j][n-i-1];
     		}
     		for(int j =n-i-2; j>=i+1;j--) {
     			temp[val++] = ar[i][j];
     		}
     		if(i%2==0) {
     			rotateRight(temp, l[i]%temp.length);
     		}else {
     			rotateLeft(temp, l[i]%temp.length);
     		}
     		val =0;
     		for(int j =0+i;j<m-i; j++) {
     			ar[j][i] = temp[val++] ;
     		}
     		for(int j =1+i; j<n-i-1;j++) {
     			ar[m-1-i][j] = temp[val++];
     		}
     		for(int j =m-i-1;j>=0+i; j--) {
     			ar[j][n-i-1] = temp[val++];
     		}
     		for(int j =n-i-2; j>=i+1;j--) {
     			ar[i][j] = temp[val++];
     		}
     		
  
     	}
     	
     	for(int i =0;i<m;i++) {
     		for(int j =0;j<n;j++) {
     			System.out.print(ar[i][j]+" ");
     		}
     		System.out.println();
     	}
     	
     	
     	
	}
	public static void rotateRight(int[] nums, int k) {
	        int[] array = Arrays.copyOf(nums, nums.length);
	        for (int i = 0; i < nums.length; i++)
	            nums[(i + k) % nums.length] = array[i];
	}
	public static void rotateLeft(int[] nums, int k) {
        int[] array = Arrays.copyOf(nums, nums.length);
        for (int i = 0; i < nums.length; i++)
            nums[i] = array[(i+k) % nums.length];
	}
}
