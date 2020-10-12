import java.util.*;

// Print 1 to N, whether it is Prime or not.
public class IsPrime{
    public static boolean isPrime[];
    public static void main(String args[]){
        // Prints True for Prime numbers and false for non prime numbers.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        boolean ans[] = SeiveOfEratoSthenes(n);
        for(int i =1; i<=n; i++)
            System.out.println(i + " isPrime ? " + ans[i]);
    }

    static boolean[] SeiveOfEratoSthenes(int n){
        boolean isPrime[] = new boolean[n+1];
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;

        for(int i =2;i*i<=n;i++){
            for(int j = i+i; j<=n; j+=i){
                isPrime[j] = false;
            }
        }
        return isPrime;
    }
}