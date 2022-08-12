#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <ctype.h>
int main()   
{   
 int i = 0;
 int Sum = 0 ;  
 
 int Number = 0;
 Number = get_int("Please enter any number: ");  
 
 for(i = 1 ; i < Number ; i++)   
  {   
   if(Number % i == 0)   
     Sum = Sum + i ;   
  }    

 if (Sum == Number)   
 {
    printf("\n %d is a Perfect Number", Number) ;   
 }
 else
    printf("\n%d is not the Perfect Number", Number) ;   
}