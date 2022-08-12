#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    double real;
    double imaginary;
}complex;



int main(void)
{
    complex c1;

    c1.real = 0;
    c1.imaginary = 1.0;

    complex c2;
    c2.real = 0;
    c2.imaginary = 1.0;
    complex c3;

    printf("c1 real Number: %f", c2.real);
    printf("c1 IMG Number: %f", c2.imaginary);

}