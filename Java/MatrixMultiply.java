import java.util.*;
public class MatrixMultiply
{
    public static void main(String args[])
    {
        Scanner in=new Scanner(System.in);
        int a[][]=new int[3][3];
        int b[][]=new int[3][3];
        int res[][]=new int[3][3];
        System.out.println("Enter elements in Matrix 1");
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
                a[i][j]=in.nextInt();
        }
        System.out.println("Enter elements in Matrix 2");
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
                b[i][j]=in.nextInt();
        }

        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                int sum=0;
                for(int k=0;k<3;k++)
                    sum+=a[k][j]*a[i][k];
                res[i][j]=sum;
            }
        }
        System.out.println("Multiplication of above Matrix are");
        for(int i=0;i<3;i++)
        {
            for (int j = 0; j < 3; j++)
                System.out.print(res[i][j] + " ");
            System.out.println();
        }
    }
}
