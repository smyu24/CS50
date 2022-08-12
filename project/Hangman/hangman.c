#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>
#include <math.h>
#include <ctype.h>
#include <time.h>


void line1(void)
{
    printf("|\n");
    printf("|\n");
    printf("|\n");
    printf("_\n");
}
void line2(void)
{
    printf("|-\n");
    printf("|\n");
    printf("|\n");
    printf("_\n");
}
void line3(void)
{
    printf("|--\n");
    printf("|\n");
    printf("|\n");
    printf("_\n");
}
void line4(void)
{
    printf("|--|\n");
    printf("|\n");
    printf("|\n");
    printf("_\n");
}
void line5(void)
{
    printf("|--|\n");
    printf("|  o\n");
    printf("|\n");
    printf("_\n");
}
void line6(void)
{
    printf("|--|\n");
    printf("|  o\n");
    printf("|  |\n");
    printf("_\n");
}
void line7(void)
{
    printf("|--|\n");
    printf("|  o\n");
    printf("| -|\n");
    printf("_\n");
}
void line8(void)
{
    printf("|--|\n");
    printf("|  o\n");
    printf("| -|-\n");
    printf("_\n");
}
void line9(void)
{
    printf("|--|\n");
    printf("|  o\n");
    printf("| -|-\n");
    printf("_ | \n");
}
void line10(void)
{
    printf("|--|\n");
    printf("|  o\n");
    printf("| -|-\n");
    printf("_ | |\n");
}

int randGenerator(int MAXwords)
{
    srand(time(NULL));
    return rand() % MAXwords;
}

void numberofchance(int chances)
{
    printf("Total number of chances is %i\n", chances);

}

int main (void)
{
    int i = 0;
    char* words[69903];
    FILE *file_handle = fopen("wordlist.txt","r");
    int MAXwords = 10000;

    for( i = 0 ; i < MAXwords ; i++ )
    {
        words[i] = malloc(128);
        fscanf(file_handle,"%127s",words[i]);
    }

/* If you want to take a look at the list of words, then activate this comment to see whats in there.
    for(i=0;i<1000;i++)
    {
        printf("%d : %s \n", i, words[i]);
    }*/
        printf("Welcome to Hangman\n");
        printf("----------------------\n");

        int difficulty = 0;
        printf("Enter 1 if you want EASY mode\n");
        printf("Enter 2 if you want MEDIUM mode\n");
        printf("Enter 3 if you want Hard mode\n");
        printf("Enter 0 if you want to exit the game\n");

        difficulty = get_int("What level of difficult would you like to have? ");
        if(difficulty == 1)
        {
            printf("Selected mode: Easy\n");
        }
        else if(difficulty == 2)
        {
            printf("Selected mode: Medium\n");
        }
        else if(difficulty == 3)
        {
            printf("Selected mode: Hard\n");
        }
        else if(difficulty == 0)
        {
            return 0;
        }

    // selec a woord from wordlist[]

    int randomNumber = 0;
    int chances = 10;

    randomNumber = randGenerator(MAXwords);        // this line will pick the random #
    char selectedWord[strlen(words[randomNumber] + 1)]; // this line will set array size
    strcpy(selectedWord, words[randomNumber]); // this copy the seleccted word

/* If you need too take a look at the wod the activate this
    for (i = 0; i < strlen(selectedWord); i++)
    }
        printf("%c",selectedWord[i]);
    }
    printf("\n");
*/

    char displayWord[strlen(words[randomNumber] + 1)];
    for (i = 0; i < strlen(selectedWord); i++)
    {
        displayWord[i] = '_';
    }
    char newWord[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    while(chances > 0)
    {
        char userInput = 0;
        // ---- display starts here
        //printf("******************\n\n");
        // --- section #1
        //line1();
        //---section #2
        //printf("******************\n\n");
        numberofchance(chances);
        int lowercase = 0;
        userInput = get_char("Insert a letter to try: ");
        lowercase = tolower(userInput);
        for(int t = 0; t < 26; t++)
        {
            if(newWord[t] == userInput)
            {
                newWord[t] = '_';
                chances--;
            }
        }

        printf("Words left: ");
        for(i = 0; i < strlen(newWord); i++)
        {
            printf("%c ", newWord[i]);
        }//new word list
        printf("\n");
        for (i = 0; i < strlen(selectedWord); i++)
        {
            if(userInput == selectedWord[i])
            {
              displayWord[i] = userInput;
              chances++;
              if(chances > 10)
              {
                  chances = 10;
              }
            }
        }
        printf("\n");
        for (i = 0; i < strlen(selectedWord); i++)
        {
            printf("%c ",displayWord[i]);
        }
        printf("\n");
    }
    printf("Last guess: ");
    string lastguess = get_string("");

    if(lastguess == selectedWord)//not working needs work to fix the int to upper
    {
        printf("Correct Guess!");
    }
    else if(lastguess != selectedWord)
{
    printf("\nThe correct answer was:\n%s\n", selectedWord);
}

    // we need to release memory at the end so keep this.
    for(i=0;i<MAXwords;i++)
    {
        free(words[i]);
    }

}