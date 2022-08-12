#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

//https://www.tutorialspoint.com/c_standard_library/ctype_h.htm
//ispunct
//isalpha


 int main(void)
 {
     string c = get_string("String Input: ");

     int total_a = 0;

     for(int i = 0; i<strlen(c); i++)
     {
         if( c[i] == "a")
         {
            total_a++;
         }
     }
  printf("%d",total_a);
 }
 