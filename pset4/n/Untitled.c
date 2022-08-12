#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
int main (void)
{
  string userInput = get_string("Input a string: ");
  int num = strlen(userInput);
  int vowel = 0;
  int constant = 0;
  for(char *i = &userInput[0]; i < &userInput[num]; i++)
  {
    if(*i == 'a' || *i == 'e' || *i == 'i' || *i == 'o' || *i == 'u' || *i == 'A' || *i == 'E' || *i == 'I' || *i == 'O' || *i == 'U')
    {
      vowel++;
    }
    else if((*i >= 'a' && *i <= 'z') || (*i >='A' && *i <= 'Z'))
    {
      constant++;
    }
  }
  printf("number of vowel: %i\n", vowel);
  printf("number of constant: %i\n", constant);
}

/*
Write a program in C to count the number of vowels and consonants in a string using a pointer.


Test Data :
Input a string: string
Expected Output :
Number of vowels : 1
Number of constant : 5

*/