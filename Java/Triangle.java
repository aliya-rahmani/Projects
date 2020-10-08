import java.util.Scanner;

public class Triangle {

    public static void triangle(){
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the value side A: ");
        double a = input.nextDouble();
        System.out.print("Enter the value side A: ");
        double b = input.nextDouble();
        System.out.print("Enter the value side C: ");
        double c = input.nextDouble();

        if(checkSides(a, b, c)){
            if(a == b && b == c)
                System.out.println("Equilateral");
            else if(a == b || a == c || b == c)
                System.out.println("Isosceles");
            else
                System.out.println("Scalene");
        }else{
            System.out.println("These values are not from a triangle!");
        }
    }

    protected static boolean checkSides(double a, double b, double c){

        if(a < b+c && b < a+c && c < a+b)
            return true;
        else
            return false;
    }
}
