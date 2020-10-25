#include<stdio.h>
#include<stdlib.h>
#include<string.h>
 
# define MAX 20
 
char str[MAX], stack[MAX];
int top = -1;
 
char pop()
{
      return stack[top--];
}
 
void push(char ch)
{
      stack[++top] = ch;
}
 
void postfix_to_infix(char expression[])
{
      int count, length;
      char element, operator;
      length = strlen(expression);
      for(count = 0; count < MAX; count++)
      {
            stack[count] = 0;
      }
      printf("\nInfix Expression:\t");
      printf("%c", expression[0]);
      for(count = 1; count < length; count++)
      {
            if(expression[count] == '-' || expression[count] == '/' || expression[count] == '*'|| expression[count] == '+')
            {
                  element = pop();
                  operator = expression[count];
                  printf(" %c %c", operator, element);
            }
            else
            {
                  push(expression[count]);
            }
      }
      printf("%c", expression[top--]);
}
 
int main()
{
      char postfix_expression[50];
      printf("\nEnter Postfix Expression:\t");
      scanf("%s", postfix_expression);
      postfix_to_infix(postfix_expression);
      printf("\n");
      return 0;
}
