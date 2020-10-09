//		Write a menu–driven program to perform the following matrix operation
//		Menu Driven Program
//		1. Addition
//		2. Subtraction
//		3. Multiplication
//		4. Find Greatest Number from Each Row
//		5. Addition of Major Diagonal Elements
//		6. Sparse matrix representation for given matrix


#include <stdio.h>																			//Used for standard input and output

void input_mat(int m[][10],int row,int col);												//Function declaration
void output_mat(int m[][10],int row,int col);												//Function declaration
void add(int m1[][10],int m2[][10],int m3[][10],int row,int col);							//Function declaration
void sub(int m1[][10],int m2[][10],int m3[][10],int row,int col);							//Function declaration
void multiply(int m1[][10],int m2[][10],int m3[][10],int rowA,int colA,int colB);			//Function declaration
void greatest(int m1[][10],int row,int col);												//Function declaration
void diagonal_sum(int m1[][10],int row,int col);											//Function declaration
void sparse(int m1[][10],int row,int col);													//Function declaration


int main()
{
	int ch,choice,matA[10][10],matB[10][10],result[10][10],i,j,rowA,colA,rowB,colB;
	
    printf("Enter number of rows for matrix A:");
    scanf("%d",&rowA);
    printf("Enter number of columns for matrix A:");
    scanf("%d",&colA);
    
    input_mat(matA,rowA,colA);
    output_mat(matA,rowA,colA);
    
    printf("\nEnter number of rows for matrix B:");
    scanf("%d",&rowB);
    printf("Enter number of columns for matrix B:");
    scanf("%d",&colB);
    
    input_mat(matB,rowB,colB);
    output_mat(matB,rowB,colB);

    do{
    printf("\n\nM.E.N.U\n");											//Menu driven 
    printf("1.Addition\n");
    printf("2.Subtraction\n");
    printf("3.Multiplication\n");
    printf("4.Find Greatest Number from Each Row\n");
    printf("5.Addition of Major Diagonal Elementsl\n");
    printf("6.Sparse matrix representation for given matrix\n");
    printf("7.Exit\n");
    printf("Enter choice:");
    scanf("%d", &ch);
    printf("\n");
	
	switch(ch){
		case 1:	if(rowA == rowB && colA == colB)
				{
					printf("Matrix can be added\n");
					add(matA,matB,result,rowA,colA);
					printf("Matrix after addition is:\n");
					output_mat(result,rowA,colA);	
				}
				else
				{
					printf("Dimensions are not equal, matrix cannot be added\n");
				}
				break;
				
		case 2:	if(rowA == rowB && colA == colB)
				{
					printf("Matrix can be subtracted\n");
					sub(matA,matB,result,rowA,colA);
					printf("Matrix after subtraction is:\n");
					output_mat(result,rowA,colA);
				}
				else
				{
					printf("Dimensions are not equal, matrix cannot be subtracted\n");
				}
				break;
				
		case 3: if(colA == rowB)
				{
					printf("Matrix can be multiplied\n");
					multiply(matA,matB,result,rowA,colA,colB);
					output_mat(result,rowA,colA);
				}
				else
				{
					printf("Dimensions are not equal, matrix cannot be multiplied\n");
				}
				break;
				
		case 4:	printf("For matrix A or matrix B?(1/2):");
				scanf("%d",&choice);
				if(choice == 1)
				{
					greatest(matA,rowA,colA);
				}
				else if(choice == 2)
				{
					greatest(matB,rowB,colB);
				}
				break;
				
		case 5:	printf("For matrix A or matrix B?(1/2):");
				scanf("%d",&choice);
				if(choice == 1)
				{
					diagonal_sum(matA,rowA,colA);
				}
				else if(choice == 2)
				{
						diagonal_sum(matB,rowB,colB);
				}
				break;

		case 6: printf("For matrix A or matrix B?(1/2):");
				scanf("%d",&choice);
				if(choice == 1)
				{
					sparse(matA,rowA,colA);
				}
				else if(choice == 2)
				{
					sparse(matB,rowB,colB);
				}
				break;
		case 7:exit(0);
		default:
			printf("Sorry,Wrong choice\n");
			break;
	}
}while(ch<7);
return 0;
}


void input_mat(int m[][10],int row,int col)					//To input a matrix from the user
{
	int i,j;
	
	printf("\nEnter the elements: \n");
	for(i=0;i<row;i++)
	{
		for(j=0;j<col;j++)
		{
			scanf("%d",&m[i][j]);
		}
		
	}
}

void output_mat(int m[][10],int row,int col)				//To output a matrix
{
	int i,j;
	
	printf("\nMATRIX:\n");
	for(i=0;i<row;i++)
	{
		for(j=0;j<col;j++)
		{
			printf("%d ",m[i][j]);
		}
		printf("\n");
	}	
}

void add(int m1[][10],int m2[][10],int m3[][10],int row,int col)			//To add two matrix
{
	int i,j;
	
	for(i=0;i<row;i++)
	{
		for(j=0;j<col;j++)
		{
			m3[i][j] = m1[i][j] + m2[i][j];
		}
	}
	
	
}
void sub(int m1[][10],int m2[][10],int m3[][10],int row,int col)			//To subtract two matrix
{
	int i,j;
	
	for(i=0;i<row;i++)
	{
		for(j=0;j<col;j++)
		{
			m3[i][j] = m1[i][j] - m2[i][j];
		}
	}

}

void multiply(int m1[][10],int m2[][10],int m3[][10],int rowA,int colA,int colB)		//To multiply two matrix
{
	int i,j,k;
	
	for (i=0;i<rowA;i++) 
    { 
        for (j=0;j<colB;j++) 
        { 
            m3[i][j] = 0; 
            for (k=0;k<colA;k++) 
                m3[i][j] += m1[i][k] * m2[k][j]; 
        } 
    }
}

void greatest(int m1[][10],int row,int col)												//To find the greatest number from each row
{
	int i,j,max=0;
	int res[row];

	for(i=0;i<row;i++)
	{ 
        for(j=0;j<col;j++) 
		{ 
        	if(m1[i][j]>max) 
			{ 
                max = m1[i][j]; 
            } 
        } 
        res[i] = max; 
        max = 0; 
    } 
    
    for(i=0;i<row;i++)
    {
    	printf("In row %d:%d\n",i,res[i]);
	}  
}

void diagonal_sum(int m1[][10],int row,int col)											//To find the addition of major diagonal elements
{
	int i,j,sum=0;
	
    for(i=0;i<row;i++){
        sum += m1[i][i];
    }
    printf("Sum of the Major Diagonal is %d ",sum);
	
}

void sparse(int m1[][10],int row,int col)												//To find the sparse matrix for given matrix
{
	int i,j,k=0,size=0,res_matrix[3][size];
	
	for(i=0;i<row;i++)
	{
		for(j=0;j<col;j++)
		{
			if(m1[i][j] != 0)
                size++;
		}
            
	}
        
    for(i=0;i<row;i++)
	{
    	for(j=0;j<col;j++)
    	{
    		if(m1[i][j] != 0)
            {	
                res_matrix[0][k]=i;
                res_matrix[1][k]=j;
                res_matrix[2][k]=m1[i][j];
                k++;
            }
		}
	}
        

    printf("\nTriplet Representation:\n");
    for(i=0;i<3;i++)
    {
        for(j=0;j<size;j++)
        {
        	printf("%d ",res_matrix[i][j]);
		}
		printf("\n");
    }
}



