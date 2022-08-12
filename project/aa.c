#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <ctype.h>
int main (void)
{
  int userInput = 0, position = 0;
  int i = get_int("Input the size of the array: ");
  int element[i];
  printf("Input %i elements in the array in ascending order:\n", i);
for(int loop = 0; loop < i; loop++)
{
  printf("element - %i : ", loop);
  userInput = get_int("");
  element[loop] = userInput;
}
  position = get_int("Input the position where to delete: ");
  //position = position - 1;


  for(int loop = position - 1; loop <  i - 1; loop++)
  {
    element[loop] = element[loop + 1 ];
  }

  printf("\nThe new list is: ");
  for(int loop = 0; loop < i - 1; loop++)
  {
    printf("%i ", element[loop]);
  }
}