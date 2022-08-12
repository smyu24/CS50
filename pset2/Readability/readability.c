#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

////http://www.asciitable.com/
int main(void)
{
    int avgLetters = 0;// avgLetters is the average number of letters per 100 words in the text,
    int avgSentences = 0;// avgSentences is the average number of sentences per 100 words in the text.
    int wordcount = 1;//word count of the writing
    float index = 0 ;

    string Sentence = get_string("Text: "); //getting user input

    for (int i = 0, n = strlen(Sentence); i<n ; i++)
    {
     if(Sentence[i] >= 65 && Sentence[i] <=122)
     {
      avgLetters++;
     }
     else if(Sentence[i] == 32) 
     {
      wordcount++; 
     }
     else if(Sentence[i] == 46 || Sentence[i] == 63 || Sentence[i] == 33)  //period and ? and !
     {
      avgSentences++;
     }
    }

    printf("Letter(s): %i\n Word(s): %i\n Sentence(s): %i\n", avgLetters, wordcount, avgSentences);

    index = 0.0588 * (100 * (float) avgLetters / (float) wordcount) - 0.296 * (100 * (float) avgSentences / (float) wordcount) - 15.8;
    if (index < 16 && index >= 0)
    {
        printf("Grade %.0f\n",round(index));
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Before Grade 1\n");
    }
}
//samples
//Text: In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.
//       In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.

//Text: It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.
//250 letter(s)
//55 word(s)

//Text: When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.
//295 letter(s)
//70 word(s)
//3 sentence(s)