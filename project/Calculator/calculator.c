#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>

void addition (void)
{
    float input1 = 0;
    float input2 = 0;

    printf("\nAddition\n");

    input1 = get_float("Input value one: ");
    input2 = get_float("Input value two: ");

    printf("Result: %0.3f\n", input1 + input2);
}

void subtraction (void)
{
    float input1 = 0;
    float input2 = 0;

    printf("\nSubtraction\n");

    input1 = get_float("Input value one: ");
    input2 = get_float("Input value two: ");

    printf("Result: %0.3f\n", input1 - input2);
}
void multiplication (void)
{
    float input1 = 0;
    float input2 = 0;

    printf("\nMultiplication\n");

    input1 = get_float("Input value one: ");
    input2 = get_float("Input value two: ");

    printf("Result: %0.3f\n", input1 * input2);
}
void division (void)
{
    float input1 = 0;
    float input2 = 0;

    printf("\nDivision\n");

    input1 = get_float("Input value one: ");
    input2 = get_float("Input value two: ");

    printf("Result: %0.3f\n", input1 / input2);
}
void quadratic (void)
{
    float a = 0;
    float b = 0;
    float c = 0;

    a = get_float("Input the first number(a): ");
    b = get_float("Input the second number(b): ");
    c = get_float("Input the third number(c): ");

    float top1;
    float bottom;
    float inside = (b * b) - 4 * a * c;

    top1 = -b + sqrt(inside);
    bottom = 2 * a;
    top1 = top1 / bottom;

    float top2;

    top2 = -b - sqrt(inside);
    top2 = top2 / bottom;

    printf("Root 1 = %0.4f\n", top1);
    printf("Root 2 = %0.4f\n", top2);
}
void average (void)
{
    int numberofterms = 0;

    numberofterms = get_int("How many values are there?\n");

    int userInput = 0;
    int sumNumber = 0;
    printf("Input %i numbers to add up and get the average of\n", numberofterms);
    for(int g = 0; g < numberofterms; g++)
    {
    userInput = get_int("Number: ");
    sumNumber = userInput + sumNumber;
    }
    printf("The sum of the %i is: %i\n", numberofterms, sumNumber);
    printf("The average of the %i is %i\n", numberofterms, sumNumber / numberofterms);
}


int main(void)
{
    int menuSelector = 0;
    float input1 = 0;
    float input2 = 0;
    do
    {
    printf("*-*-*-*-*-*-*-*-*\n");
    printf("  Calculator\n");
    printf("*-*-*-*-*-*-*-*-*\n");

    printf("1: Addition\n");
    printf("2: Subtraction\n");
    printf("3: Multplication\n");
    printf("4: Division\n");
    printf("5. Quadratic formula\n");
    printf("6. Average\n");
    printf("0: Exit\n");

    menuSelector = get_int("Choose a number: ");
    printf("\n");

    if(menuSelector == 1)
    {
        addition();
    }
    else if(menuSelector == 2)
    {
        subtraction();
    }
    else if(menuSelector == 3)
    {
        multiplication();
    }
    else if(menuSelector == 4)
    {
        division();
    }
    else if(menuSelector == 5)
    {
        quadratic();
    }
    else if(menuSelector == 6)
    {
        average();
    }

    }while(menuSelector != 0);
        printf("Exited\n");
}