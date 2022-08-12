#include <stdio.h>
#include <cs50.h>
#include <math.h>
int main(void)
{
    float e;
    do
    {
    e = get_float("Change owed: ");
    }
    while(e < 0);
    int cents = round(e * 100);
    int coins = 0;

    while(cents >= 25)
    {
        cents -= 25;
        coins++;
    }
    while(cents >= 10)
    {
        cents -= 10;
        coins++;
    }
    while(cents >= 5)
    {
        cents -= 5;
        coins++;
    }
    while(cents >= 1)
    {
        cents -= 1;
        coins++;
    }
    printf("%i\n", coins);
}