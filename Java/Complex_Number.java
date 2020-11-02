import java.io.*;
class Complex_Number
{
	double x,y;
	Complex_Number(int x1,int y1)
	{
		x=x1;
		y=y1;
	}
	Complex_Number add(Complex_Number c1)
	{
		Comple_Number c2=new Complex_Number();
		c2.x=x+c1.x;
		c2.y=y+c1.y;
		return c2;
	}
	Complex_Number sub(Complex_Number c1)
	{
		Comple_Number c2=new Complex_Number();
		if(x>c1.x)
		{
			c2.x=x-c1.x;
			c2.y=y-c1.y;
		}
		else
		{
			c2.x=c1.x-x;
			c2.y=c1.y-y;
		}
		return c2;	
	}
	Complex_Number mul(Complex_Number c1)
	{
		Comple_Number c2=new Complex_Number();
		c2.x=x*y-c1.x*c1.y;
		c2.y=x*c1.y+c1.x*y;
		return c2;
	}
	void display()
	{
		if(y!=0)
		{
			if(y>0)
				System.out.println(x+"+"+y+"i");
			else
				System.out.println(x+y+"i");
		}
		else
			System.out.println(x);
	}
	public static void main(String[] args)
	{
		try
		{
		double x1,y1,x2,y2;
		BufferReader br= new BufferReader( new InputStreamReader(System.in));
		System.out.println("Enter the real and imaginary part of 1st no.");
		x1=Double.parseDouble(br.readLine());
		y1=Double.parseDouble(br.readLine());
		System.out.println("Enter the real and imaginary part of 2nd no.");
		x2=Double.parseDouble(br.readLine());
		y2=Double.parseDouble(br.readLine());
		Complex_Number obj1=Complex_Number(x1,y1);
		Complex_Number obj2=Complex_Number(x2,y2);
		Complex_Number obj3=Complex_Number();
		obj3=obj1.add(obj2);
		obj3.display();
		obj3=obj1.sub(obj2);
		obj3.display();
		obj3=obj1.mul(obj2);
		obj3.display();
		}catch(Exception e){System.out.println(e);}
	}
}	
		
		