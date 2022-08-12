#include <stdio.h>
#include <cs50.h>

int main (void)
{

    int g = get_int("Height: ");
    while(g > 8 || g <= 0)
    {
      g = get_int("Height: ");
    }

      for(int row = 0; row < g; row++)
      {
        for(int column = 0; column < g; ++column++)
        {
          if(row + column >= g - 1)
          {
            printf("#");
          }
          else
          printf(" ");
        }
        printf("\n");
      }

}