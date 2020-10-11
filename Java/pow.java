import java.util.*;


public class pow {
    public static long mod = (long) 1_000_000_007;
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println(find(a*1l, b*1l));
    }
    
    public static int find(long a, long b){
        long res = 1;
        // a pow b.
        while(b>0){
            if( (b&1) !=0)
                res = (res * a )%mod;
        
            a = (a % mod * a % mod) % mod ;
            b = b >> 1;
        }
        return (int) res;
    }
}