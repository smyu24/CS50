#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <ctype.h>
int main (void)
{
    int i = 0;
        i = get_int("Input the number of elements to be stored in the array: ");
    int number = 0;
    int element[i];
    for(int loop = 0; loop < i; loop++)
    {
        printf("element - %i : ", loop);
        element[loop] = get_int("");
    }
    int copyElement[i];
    for(int loop = 0; loop < i; loop++)
    {
        copyElement[loop] = element[loop];
    }
    for(int t = 0; t < i; t++)
    {
        for(int d = t + 1; d < i; d++)
        {
            if(element[t] == copyElement[d])
            {
                number++;
            }
        }
    }
    int unique = 0;
    unique = i - number;
    
    printf("The unique elements found in the array are: %i\n", unique);
}
