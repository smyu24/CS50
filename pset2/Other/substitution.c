#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
int main(int argc, string argv[])//you can void this if you want
{
    if( strlen(argv[1]) != 26 || argc != 2 )
    {
        printf("Usage: ./substitution key\n");
        return 1;
    } // validates user inputs

    char KEY[26];      // VCHPRZGJNTLSKFBDQWAXEUYMOI
    char lowerKEY[26]; // vchprzgjn
    char ANSWER[26];


    //store user input to KEYS

    for (int i = 0; i < 26; i++)
    {
        KEY[i] = argv[1][i];
        lowerKEY[i] = tolower(argv[1][i]);
    }

    // validate keys -- if the user input the numbers inside of the key
    string plaintxt = get_string("plaintext: ");

    int temp;

    for(int i = 0, n = strlen(plaintxt); i < n; i++)
    {
        temp = plaintxt[i];
        if( temp >= 65 && temp <= 90) // lower case so - 65
        {
            ANSWER[i] = KEY[temp-65];
        }
        else if( temp >= 97 && temp <= 122) // upper case, so -97
        {
            ANSWER[i] = lowerKEY[temp-97];
        }
        else if( temp >= 48 && temp <= 57) // #
        {
            ANSWER[i] = temp;
        }
        else if( temp == 32)
        {
            ANSWER[i] = temp;
        }
    }

    printf("ciphertext: %s\n",ANSWER);
/*
hi
thihs
is
multiline
comment
*/

}