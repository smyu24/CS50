#include <stdio.h>
#include <cs50.h>


 int main(void)
 {
    int total = get_int("How many students? ");
    int scores[total];
    int temp = 0;
    int i = 0;
    
    for (i = 0 ; i < total ; i++ )
    {
        temp = get_int("Scores? ");
        scores[i] = temp;        
    }
    
    int sum_scores = 0;
    
    for (i = 0 ; i < total ; i++ )
    {
        //printf(" score[%i] = %i\n", i, scores[i]);
        sum_scores = sum_scores + scores[i];
        printf("scores[%i] = %i, sumscores= %i \n",i,scores[i],sum_scores);
    }

     printf("Average: %i\n", sum_scores / total);
 }