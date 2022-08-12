#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
int main(int key, string argv[])//you can void this if you want
{
    if (key == 2)
    {
        // positive
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            if (isdigit(argv[1][i]) == false)
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
        int k = atoi(argv[1]);
        string plaintxt = get_string("plaintext: ");
        printf("ciphertext: ");

        for (int i = 0; i < strlen(plaintxt); i++) //ci = (pi + k) % 26
        {
            //lower
            if (plaintxt[i] >= 'a' && plaintxt[i] <= 'z')
            {printf("%c", ((((plaintxt[i] - 'a') + k) % 26) + 'a'));
            }
            //upper
            else if (plaintxt[i] >= 'A' && plaintxt[i] <= 'Z')
            {
                printf("%c", ((((plaintxt[i] - 'A') + k) % 26) + 'A'));
            }

            else
            {
                printf("%c", plaintxt[i]);
            }
        }
        printf("\n");
        return 0;
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}