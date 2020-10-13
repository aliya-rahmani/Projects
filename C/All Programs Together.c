#include<stdio.h>
#include<math.h>
#include<stdlib.h>
int main()
{
	int n,ch;
	char c;
	
	printf("press 1 : leapyear\n");
	printf("press 2 : armstrong\n");
	printf("press 3 : palindrome\n");
	printf("press 4 : largest among three numbers\n");
	printf("press 5 : swap two numbers using and without using third variable\n");
	printf("press 6 : test prime or not\n");
	printf("press 7 : fibonacci series\n");
	printf("press 8 : factorial\n");
	printf("press 9 : average of n numbers using array\n");
	printf("press 10: largest element in array\n");
	printf("press 11: search element to array\n");
	printf("press 12: transpose of matix \n");
	printf("press 13: swapping using pointer\n");
	printf("press 14: gcd\n");
	printf("press 15: lcm\n");
	printf("press 16: compare two strings using lib func\n");
	printf("press 17: copy string using lib func\n");
	printf("press 18: concatenate two strings using lib func\n");
	printf("press 19: addition of two arrays\n");
	printf("press 20: bubble sort \n");
	printf("press 21: structure--student details using structure\n");
	printf("press 22: find distance using structure\n");
	printf("press 23: file operation\n");
	printf("press 24: student details using file\n");
	printf("\nenter number which you want to print: \n");
	scanf("%d",&ch);
	switch(ch)
	{
		case 1:
			leapyr();
			break;
		case 2:
			// armstrong();
			// break;
		case 3:
			palindrome();
			break;
		case 4:
			largest_among();
			break;
		case 5:
			swap();
			break;
		case 6:
			prime();
			break;
		case 7:
			fibo();
			break;
		case 8:
			fact();
			break;
		case 9:
			avg();
			break;
		case 10:
			large_elem_arr();
			break;
		case 11:
			search_arr();
			break;
		
		case 12:
			transpose_mat();
			break;
		case 13:
			swap_pointer();
			break;
		case 14:
			gcd();
			break;
		case 15:
			lcm();
			break;
		case 16:
			comp();
			break;
		case 17:
			copy();
			break;
		case 18:
			concat();
			break;
		case 19:
			addition_array();
			break;
		case 20: 
			bubble_sort();
			break;
		case 21:
			struct_student_info();
			break;
		case 22:
			distance_struct();
			break;
		case 23:
			file_operation();
			break;
		case 24:
			student_detail_file();
			break;
		default:
			printf("oops!\n");
			break;
	}
}
void leapyr()
{
	int n;
	printf("enter a year: \n");
	scanf("%d",&n);
	if(n%400==0)
		printf("%d is leapyear",n);
	else if(n%100 == 0)
		printf("%d is not leapyear",n);
	else if(n%4==0)
		printf("%d is leapyear",n);
	else
		printf("%d is not leapyear",n);
			
		
	
}
// void armstrong()
// {
// 	int rem,c,n,temp;
// 	int result = 0;
// 	printf("enter a number");
// 	scanf("%d",&n);
// 	temp = n;
// 	while(temp!=0)
// 	{
// 		temp/=10;
// 		c++;
// 	}
// 	temp = n;
// 	while(temp!=0)
// 	{
// 		rem = temp%10;
// 		result += pow(rem,c);
// 		temp/=10;
// 	}
// 	if(result == n)
// 	{
// 		printf("%d is armstrong number",n);
// 	}
// 	else
// 	{
// 		printf("%d is not armstrong number",n);
// 	}
// }
void palindrome()
{
	int rem,temp,n;
	int result=0;
	printf("enter a number: ");
	scanf("%d",&n);
	temp = n;
	while(temp!=0)
	{
		rem = temp%10;
		result = result*10 + rem;
		temp/=10;
	}
	if(result == n)
	{
		printf("%d is palindrome number",n);
	}
	else
	{
		printf("%d is not palindrome number",n);
	}
}
void largest_among()
{
	int a,b,c;
	printf("enter three numbers: ");
	scanf("%d %d %d",&a,&b,&c);
	if(a>b)
		if(a>c)
			printf("%d is greatest",a);
		else
			printf("%d is greatest",c);
	else
		printf("%d is greatest",a);
}
void swap()
{
	int ch;
	printf("how do you want to swap ?\n");
	printf("1: using third variable\n2: without using third variable\n ");
	printf("press 1 or 2 : ");
	scanf("%d",&ch);
	switch(ch)
	{
		case 1:
			using_th_v();
			break;
		case 2:
			w_using_th_v();
		default:
			printf("wroong choice!!");
			break;
	}
}
int using_th_v()
{
	int temp,a,b;
	printf("put value of a: ");
	scanf("%d",&a);
	printf("put value of b: ");
	scanf("%d",&b);
	temp = a;
	a = b;
	b = temp;
	printf("a: %d \t b: %d",a,b);
}
int w_using_th_v()
{
	int a,b;
	printf("put value of a: ");
	scanf("%d",&a);
	printf("put value of b: ");
	scanf("%d",&b);
	a = a + b;
	b = a - b;
	a = a - b;
	printf("a: %d \t b: %d",a,b);  
	
}
void prime()
{
	int n;
	char c;
	printf("enter a number: ");
	scanf("%d",&n);
	if(n%2 != 0)
	{
		printf("%d is prime no ",n);
	}
	else{
		printf("%d is not prime no",n);
	}
	printf("check again(y/n): ");
	
}
int fibo()
{
	int i,t1,t2,temp,n;
	t1 = 0;t2 = 1;
	printf("enter upto what no: ");
	scanf("%d",&n);
	for(i=0;i<=n;i++)
	{
		printf("%d ",t1);
		temp = t1 + t2;
		t1 = t2;
		t2 = temp;
	}
	
}
void fact()
{
	int n,i,res;
	res = 1;
	printf("enter number: \n");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	res = res*i;
	printf("factorial of %d is %d",n,res);
}
void avg()
{
	int n[100],sum = 0;
	int t,i;
	float avg;
	printf("how many numbers do you want to enter: ");
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		printf("n[%d]: ",i+1);
		scanf("%d",&n[i]);
	}
	for(i=0;i<t;i++)
	{
		sum += n[i]; 
	}
	avg = sum/t;
	printf("average of numbers: %.2f",avg);
}
void large_elem_arr()
{
	int n[100];
	int i,s,large;
	printf("enter numbers you want to enter: ");
	scanf("%d",&s);
	for(i=0;i<s;i++)
	{
		printf("enter number %d : ",i+1);
		scanf("%d",&n[i]);
	}
	for(i=1;i<s;i++)
	{
		if(n[0]<n[i])
			n[0] = n[i];
	}
	printf("%d is largest in array of elements",n[0]);
	
}
void search_arr()
{
	int i,a[100],n,s;
	printf("enter upto what no: ");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		printf("enter element %d: ",i+1);
		scanf("%d",&a[i]);
	}
	//search
	printf("enter number you want to search: ");
	scanf("%d",&s);
	for(i=0;i<n;i++)
	{
		if(s == a[i])
		{
			printf("%d is found at %d , ",s,i+1);
		}
	}
}

void transpose_mat()
{
	int a[100][100],transpose[100][100];
	int r,c,i,j;
	printf("enter row and column: ");
	scanf("%d %d",&r,&c);
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			printf("a[%d][%d]: ",i+1,j+1 );
			scanf("%d",a[i][j]);
		}
	}
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			printf("%d ",a[i][j]);
		}
	}
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			transpose[j][i] = a[i][j];
		}
	}
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			printf("%d ",transpose[i][j]);
		}
	}
}
void swap_pointer()
{
	int a,b;
	printf("\nenter number of a and b respectively: \n");
	scanf("%d %d",&a,&b);
	swap_p(&a,&b);
	printf("after swapping:\n");
	printf("a: %d \t b: %d",a,b);
}
void swap_p(int *p,int *q)
{
	int temp;
	temp = *p;
	*p = *q;
	*q = temp;
}
void gcd(int a,int b)
{
	int i,gc;
	printf("enter two numbers: ");
	scanf("%d %d",&a,&b);
	for(i=1;i<=a&&i<=b;i++)
	{
		if(a%i == 0 && b%i == 0 )
		{
			gc = i;
		}
	}
	printf("gcd is %d",gc);
}
void lcm(int a,int b)
{
	int i,gc,s;
	printf("enter two numbers: ");
	scanf("%d %d",&a,&b);
	for(i=1;i<=a&&i<=b;i++)
	{
		if(a%i == 0 && b%i == 0 )
		{
			gc = i;
		}
	}
	s = (a*b)/gc;
	printf("lcm is %d",s);
}
//library functions
void comp()
{
	char s1[100],s2[100];
	printf("enter string: ");
	scanf("%s",s1);
	printf("enter another string:");
	scanf("%s",s2);
	if(strcmp(s1,s2)==0)
	{
		printf("strings are same");
	}
	else
	{
		printf("strings are not same");
	}
}
void copy()
{
	char s1[100],s2[100];
	printf("enter string at [1]: ");
	scanf("%s",s1);
	strcpy(s2,s1);
	printf("copied string to [2] %s",s2);
	
}
void concat()
{
	char s1[100],s2[100];
	printf("enter string: ");
	scanf("%s",s1);
	printf("enter another string: ");
	scanf("%s",s2);
	strcat(s1,s2);
	printf("concatenation string is : %s",s1);
}
void addition_array()
{
	int n,i,arr1[100],arr2[100],arr3[100];
	//arr1 input
	printf("enter array value \n");
	scanf("%d",&n);
	printf("enter value one by one :\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&arr1[i]);
	}
	printf("array 1: \n");
	for(i=0;i<n;i++)
	{
		printf("%d ",arr1[i]);
	}
	//array 2 input
	printf("\n enter another array value \n");
	scanf("%d",&n);
	printf("enter value one by one :\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&arr2[i]);
	}
	
	for(i=0;i<n;i++)
	{
		printf("%d ",arr2[i]);
	}
	
	//sum 
	for(i=0;i<n;i++){
		arr3[i]=arr1[i]+arr2[i];
	}
	//display addition
	printf("\n addition : \n");
	for(i=0;i<n;i++)
	{
		printf("%d ",arr3[i]);
	}
}
void bubble_sort()
{
	int i,j,n,temp,arr[100];
	printf("enter value of array: ");
	scanf("%d",&n);
	printf("enter element one by one: ");
	for(i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}
	for(i=0;i<n;i++)
	{
		printf("[%d] = %d\n",i+1,arr[i]);
	}
	for(i=0;i<n-1;i++)
	{
		for(j=0;j<n-i-1;j++)
		{
			if(arr[j+1]<arr[j])
			{
				temp = arr[j+1];
				arr[j+1] = arr[j];
				arr[j] = temp;
			}
		}
	}
	printf("\nshow:");
	for(i=0;i<n;i++)
	{
		printf("%d ",arr[i]);
	}
}

//structure part

struct student 
{
	char name[100];
	char add[100];
	int marks;
	int id;
};
void struct_student_info()
{
	int i;
	struct student a[3],b[3];
	FILE *f1;
	f1 = fopen("detals.txt","w");
	for(i=0;i<3;i++)
	{
		printf("enter name: ");
		scanf("%s",a[i].name);
		printf("enter address: ");
		scanf("%s",a[i].add);
		printf("enter id: ");
		scanf("%d",&a[i].id);
		printf("enter marks: ");
		scanf("%d",&a[i].marks);
		
	}
	fwrite(a,sizeof(a),1,f1);
	fclose(f1);
	f1=fopen("details.txt","r");
	fread(a,sizeof(a),1,f1);
	printf("name\t\taddress\t\tid\t\tmarks\n");
	for(i=0;i<3;i++)
	{
		printf("%s\t\t%s\t\t%d\t\t%d\n\n",a[i].name,a[i].add,a[i].id,a[i].marks);
	}
	fclose(f1);
}
 
//find distance using structure
struct diastance
{
	int feet;
	float inch;
	
	
}d1,d2,sumOfDistances;
void distance_struct()
{
	printf("enter information of 1st distance: \n");
	printf("enter feet: \n");
	scanf("%d",&d1.feet);
	printf("enter inch : \n");
	scanf("%f",&d1.inch);
	
	printf("enter information of 2nd distance: \n");
	printf("enter feet: \n");
	scanf("%d",&d2.feet);
	printf("enter inch : \n");
	scanf("%f",&d2.inch);
	
	sumOfDistances.feet = d1.feet+d2.feet;
	sumOfDistances.inch = d1.inch+d2.inch;
	
	if(sumOfDistances.inch>12.0)
	{
		sumOfDistances.inch=sumOfDistances.inch-12.0;
		++sumOfDistances.feet;
	}
	
	printf("sum of distance is : %5d\'-%.2f\"",sumOfDistances.feet,sumOfDistances.inch);
	return 0;
	
}

void file_operation()
{
	FILE *fp;
	char c;
	fp=fopen("love.dat","r");
	if(fp==NULL)
	{
		printf("\n file can nt open");
		
	}
	while((c=getc(fp))!=EOF)
	{
		printf("%c",c);
	}
	fclose(fp);
	
}

void student_detail_file()
{
	int n,i,m;
	char s[100];
	printf("enter a no of students: ");
	scanf("%d",&n);
	FILE *f1;
	f1 = fopen("student.txt","w");
	for(i=0;i<n;i++)
	{
		printf("enter student name : ");
		scanf("%s",s);
		printf("enter marks: ");
		scanf("%d",&m);
		fprintf(f1,"name=%s \t marks=%d\n",s,m);
		
	}
	fclose(f1);
	
}



