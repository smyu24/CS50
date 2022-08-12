#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // is the filename there?
    if(argc != 2)
    {
        printf("Usage: ./recover image \n");
        return 1;
    }

    //chek if you can open up a file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Can't open up the file %s. \n",argv[1]);
        return 1;
    }

    FILE *img;
    char filename[8];
    unsigned char *cp = malloc(512);
    int counter =0;

    while(fread(cp,512,1,file))
    {
        if ( cp[0] == 0xff && cp[1] == 0xd8 && cp[2] ==0xff)
        {
            if (counter > 0)
            {
                fclose(img);
            }
            //generate filename
            sprintf(filename, "%03d.jpg", counter);
            img = fopen(filename,"w");
            if (img == NULL)
            {
                fclose(file);
                free(cp);
                fprintf(stderr," couldn't create jpg %s.\n",filename);
                return 3;
            }
            counter++;
        }
        if(counter > 0)
        {
            fwrite(cp,512,1,img);
        }
    }
    fclose(file);
    fclose(img);
    free(cp);
    
    return 0;
}
//use free at end