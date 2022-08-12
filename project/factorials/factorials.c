#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <ctype.h>
int main (void)
{
    int userInput = 0;
    int storage = 1;
    int userStorage = 0;
    
    userInput = get_int("Input the number: ");
    userStorage = userInput;
    
    for(int factorial = 0; factorial < userInput; factorial++)
    {
        storage = userStorage * storage;
        userStorage = userStorage - 1;
    }
    printf("The factorial of %i: %i\n", userInput,storage);
}