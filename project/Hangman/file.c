#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>
#include <math.h>
#include <ctype.h>

int main (void)
{
    int i;
    char* words[69903];
    FILE *file_handle = fopen("wordlist.txt","r");
    for(i=0;i<1000;i++)
    {
        words[i] = malloc(128);
        fscanf(file_handle,"%127s",words[i]);
    }

    for(i=0;i<1000;i++)
    {
        printf("%d : %s \n", i, words[i]);
    }

    for(i=0;i<1000;i++)
    {
        free(words[i]);
    }

}