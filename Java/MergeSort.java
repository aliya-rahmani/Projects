import java.io.*;
public class MergeSort 
{
 
   public static void merge(int a[],int l,int m,int h)
   {  
       int i, j,c=l;
       int b[]=new int[h+1];
 
	for(i = l,j = m+1; i<=m && j<=h; c++)
             {
 
                  if(a[i] <= a[j])
                  b[c] = a[i++];
                 else
                 b[c] = a[j++];
      	}
	 while(i <= m )    
                 b[c++] = a[i++];
 
               while(j<=h)   
                 b[c++] = a[j++];
          
   	 for(i = l ; i <= h; i++)
                        a[i] = b[i];
   } 
  
   public static void Sort(int a[],int l,int h)
   {  
         if(l<h)
        {
           int m=(l+h)/2;
           Sort(a,l,m);
           Sort(a,m+1,h);
           merge(a,l,m,h);
 
         } 
          
   
   }  
 
 public static void printarray(int a[])
{
       for(int i=0; i < a.length; i++)
        {
        
        System.out.print(a[i]+"  ");
        }
       
}
public static void main(String[] args) throws IOException
{
 
    int n,i;
     BufferedReader b=new BufferedReader(new InputStreamReader(System.in));
 
  
   System.out.println("enter N: ");
 n=Integer.parseInt(b.readLine());
int a[] = new int[n];  
  System.out.println("enter "+n+" elements ");
 for(i= 0; i< n; i++)
 
  a[i] = Integer.parseInt(b.readLine()); 
 
  System.out.println("elements in array ");
        printarray(a);
        Sort(a,0,n-1);
         System.out.println("\nelements after sorting");
         printarray(a);
       
  }
}