#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <ctype.h>
int main (void)
{
 int m = 300;
 float fx = 300.600006;
 char cht = 'z';

 printf("Pointer : Demonstrate the use of & and * operator :\n");
 printf("--------------------------------------------------------\n");
 printf("m = 300\n");
 printf("fx = 300.600006\n");
 printf("cht = z \n\n");

 printf("Using & operator :\n");
 printf("-----------------------\n");
 printf("address of m = %p\n", &m);
 printf("address of fx = %p\n", &fx);
 printf("address of cht = %p\n\n", &cht);

 printf("Using & and * operator : \n");
 printf("-----------------------------\n");
 printf("value at address of m = %i\n", *(&m));
 printf("value at address of fx = %f\n", *(&fx));
 printf("value at address of cht = %c\n\n", *(&cht));
 int *m2 = &m;
 float *fx2 = &fx;
 char *cht2 = &cht;

 printf("Using only pointer variable :\n");
 printf("----------------------------------\n");
 printf("value of m = %i\n", *m2);
 printf("value of fx = %f\n", *fx2);
 printf("value of cht = %c\n", *cht2);
 printf("\n");
}