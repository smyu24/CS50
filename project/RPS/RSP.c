#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>

int randGenerator(int);

int randGenerator(int MAXwords)
{
    srand(time(NULL));
    return rand() % MAXwords;
}

int main(void)
{
    char userDraw = 0;
    int totalRounds = 0;
    int compDraw = 0;
    char compDraw_CHAR;
    int MAXwords = 10000;

    printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
    printf("Welcome to Rock, Paper, Scissors\n");
    printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
    totalRounds = get_int("Pick the number of rounds you want to play :");
    int multiplier = 0;
    int scores[totalRounds];
    int scoreStreak = 0;
    for(int i = 0; i < totalRounds; i++)
    {
        userDraw = get_char("\nPick between R/P/S :");

        compDraw = 1 + randGenerator(3);

        if ( compDraw == 1)
        {
            compDraw_CHAR = 'R';
        }
        else if ( compDraw == 2)
        {
            compDraw_CHAR = 'P';
        }
        else if ( compDraw == 3)
        {
            compDraw_CHAR = 'S';
        }
        else{
            printf("Compdraw: %d", compDraw);
        }


        printf("------------------ Round #%i\n", i + 1 );
        printf("Comp : %c  ||  User : %c \n",compDraw_CHAR , userDraw);
        printf("------------------------------\n");

        if( (userDraw == 'R' && compDraw_CHAR == 'S') || ( userDraw == 'S' && compDraw_CHAR == 'P' ) || ( userDraw == 'P' && compDraw == 'R' ) )
        {
            printf("^^^^^^^^\n");
            printf("You Win\n");
            printf("^^^^^^^^\n");
            scores[i] = 1;
            scoreStreak++;
        }
        else if ((userDraw == 'R' && compDraw_CHAR == 'P') || (userDraw == 'S' && compDraw_CHAR == 'R') || (userDraw == 'P' && compDraw_CHAR == 'S'))
        {
            printf("*********\n");
            printf("You Lose \n");
            printf("*********\n");
            scores[i] = -1;
            scoreStreak = 0;
        }

        else if (userDraw == compDraw_CHAR)
        {
            printf("------- \n");
            printf("Tie\n");
            printf("------- \n");
            scores[i] = 0;
            scoreStreak = 0;
        }
        else
        {
            printf("Unknown Input; Try again with a different command\n");
            i--;
        }
        while(scoreStreak == 2)
        {
        multiplier++;
        scoreStreak = 0;
        }//For now it only does addition. For mult. needs little change

    }

    for(int i = 0 ; i < totalRounds ; i++)
    {
        printf(" # %i, %i \n ",i + 1,scores[i]);
    }
    printf("Score multiplier: %i\n", multiplier);
    int totalScore = 0;

    for(int i = 0 ; i < totalRounds ; i++)
    {
        totalScore = totalScore + scores[i];
    }
    printf("Your total score is: %i \n", totalScore + multiplier);
}