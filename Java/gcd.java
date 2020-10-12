import java.util.*;

// Find the gcd of Two numbers.
public class gcd {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println(find(a,b));
    }
    public static int find(int a, int b){
        return a%b == 0 ? b : find( b, a%b );
    }
}