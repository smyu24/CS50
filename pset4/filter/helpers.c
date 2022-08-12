#include "helpers.h"
#include <math.h>


//after everything, use noise detection (gaussian) to find shapes and opjects

/*
void Sobels_Operator(int height, int width, RGBTRIPLE image[height][width])
{
    int red = 0;
    int green = 0;
    int blue = 0;
    float avg = 0;

    for(int r = 0; r < height; r++) // row
    {
        for(int c = 0; c < width; c++) // column
        {
            red = image[r][c].rgbRed;
            green = image[r][c].rgbGreen;
            blue = image[r][c].rgbBlue;

            // image[r][c]
            image[r][c].rgbRed =
            image[r][c].rgbBGreen =
            image[r][c].rgbBlue =
        }
    }

    return;
}

// Allow image to locate balls and identify their color
void Ball_locate_differenciate(int height, int width, RGBTRIPLE image[height][width])
{
    int red = 0;
    int green = 0;
    int blue = 0;
    float avg = 0;

    for(int r = 0; r < height; r++) // row
    {
        for(int c = 0; c < width; c++) // column
        {
            //https://en.wikipedia.org/wiki/Sobel_operator

            // for every columns in a row, instanciate here and increment the appropriate values (r or c)
            /*
            Gaussian filter
            Compute image gradient
            Non-maximum suppression
            Edge tracking

            The simplest way to approximate the gradient image is to compute, for each point:

            magx = intensity[x + 1, y] - intensity[x - 1, y]
            magy = intensity[x, y + 1] - intensity[x, y - 1]
            mag = sqrt(magx ** 2 + magy ** 2)
            Where intensity[x, y] is the luminosity of the pixel situated at (x, y).
            */
            red = image[r][c].rgbRed;
            green = image[r][c].rgbGreen;
            blue = image[r][c].rgbBlue;

            // image[r][c]
            image[r][c].rgbRed =
            image[r][c].rgbBGreen =
            image[r][c].rgbBlue =


            //apply edge detection and then inside of the circumference of the circle, get the average color of the pixels, then determine the color
            // of the ball. Keep in mind of the hue, saturation, and diaflection of the image
            // Think of something for light glare, light reflection of the ball surface

        }
    }

return;
}
*/

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int red = 0;
    int green = 0;
    int blue = 0;
    float avg = 0;
    for (int i = 0; i < height; i++)
    {
        for (int t = 0; t < width; t++)
        {
            red = image[i][t].rgbtRed;
            green = image[i][t].rgbtGreen;
            blue = image[i][t].rgbtBlue;

            avg = round(((float)red + (float)blue + (float)green) / 3);
            avg = (round(red) + round(blue) + round(green)) / 3;
            avg = round(avg);

            image[i][t].rgbtRed = avg;
            image[i][t].rgbtGreen = avg;
            image[i][t].rgbtBlue = avg;
        }
    }
return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int red = 0;
    int green = 0;
    int blue = 0;
    float avg = 0;
    for (int i = 0; i < height; i++)
    {
        for (int t = 0; t < width; t++)
        {
            red = image[i][t].rgbtRed;
            green = image[i][t].rgbtGreen;
            blue = image[i][t].rgbtBlue;

            avg = round(((float)red + (float)blue + (float)green) / 3);
            avg = (round(red) + round(blue) + round(green)) / 3;
            avg = round(avg);

            image[i][t].rgbtRed = avg;
            image[i][t].rgbtGreen = avg;
            image[i][t].rgbtBlue = avg;

            int sepiaRed = round(0.393 * red + 0.769 * green + 0.189 * blue);
            if(sepiaRed > 255 || sepiaRed < 0)
            {
                image[i][t].rgbtRed = 255;
            }
            else
            {
                image[i][t].rgbtRed = sepiaRed;
            }
            int sepiaGreen = round(0.349 * red + 0.686 * green + 0.168 * blue);
            if(sepiaGreen > 255 || sepiaGreen < 0)
            {
                image[i][t].rgbtGreen = 255;
            }
            else
            {
                image[i][t].rgbtGreen = sepiaGreen;
            }
            int sepiaBlue = round(0.272 * red + 0.534 * green + 0.131 * blue);
            if(sepiaBlue > 255 || sepiaBlue < 0)
            {
                image[i][t].rgbtBlue = 255;
            }
            else
            {
                image[i][t].rgbtBlue = sepiaBlue;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int red = 0;
    int green = 0;
    int blue = 0;
    float avg = 0;
    for (int i = 0; i < height; i++)
    {
        for (int t = 0; t < width / 2; t++)
        {
            RGBTRIPLE filler = image[i][t];
            image[i][t] = image[i][width - (t + 1)];
            image[i][width - (t + 1)] = filler;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    int red, green, blue = 0;
    RGBTRIPLE filler[height][width];
    for(int i = 0; i < height; i++)
    {
        for(int t = 0; t < width; t++)
        {
            filler[i][t] = image[i][t];
        }
    }

    for(int i = 0; i < height; i++)
    {
        for(int t = 0; t < width; t++)
        {
            red = image[i][t].rgbtRed;
            green = image[i][t].rgbtGreen;
            blue = image[i][t].rgbtBlue;

            int sumRed = 0; int sumGreen = 0; int sumBlue = 0;
            float ticker = 0;
            if (i >= 0 && t >= 0)
            {
                sumRed += filler[i][t].rgbtRed;
                sumGreen += filler[i][t].rgbtGreen;
                sumBlue += filler[i][t].rgbtBlue;
                ticker++;
            }
            if (i >= 0 && t - 1 >= 0)
            {
                sumRed += filler[i][t - 1].rgbtRed;
                sumGreen += filler[i][t - 1].rgbtGreen;
                sumBlue += filler[i][t - 1].rgbtBlue;
                ticker++;
            }

            if (i - 1 >= 0 && t >= 0)
            {
                sumRed += filler[i - 1][t].rgbtRed;
                sumGreen += filler[i - 1][t].rgbtGreen;
                sumBlue += filler[i - 1][t].rgbtBlue;
                ticker++;
            }
            if (i - 1 >= 0 && t - 1 >= 0)
            {
                sumRed += filler[i - 1][t - 1].rgbtRed;
                sumGreen += filler[i - 1][t - 1].rgbtGreen;
                sumBlue += filler[i - 1][t - 1].rgbtBlue;
                ticker++;
            }
            if ((i >= 0 && t + 1 >= 0) && (i >= 0 && t + 1 < width))
            {
                sumRed += filler[i][t + 1].rgbtRed;
                sumGreen += filler[i][t + 1].rgbtGreen;
                sumBlue += filler[i][t + 1].rgbtBlue;
                ticker++;
            }
            if ((i - 1 >= 0 && t + 1 >= 0) && (i - 1 >= 0 && t + 1 < width))
            {
                sumRed += filler[i - 1][t + 1].rgbtRed;
                sumGreen += filler[i - 1][t + 1].rgbtGreen;
                sumBlue += filler[i - 1][t + 1].rgbtBlue;
                ticker++;
            }
            if ((i + 1 >= 0 && t >= 0) && (i + 1 < height && t >= 0))
            {
                sumRed += filler[i + 1][t].rgbtRed;
                sumGreen += filler[i + 1][t].rgbtGreen;
                sumBlue += filler[i + 1][t].rgbtBlue;
                ticker++;
            }
            if ((i + 1 >= 0 && t - 1 >= 0) && (i + 1 < height && t - 1 >= 0))
            {
                sumRed += filler[i + 1][t - 1].rgbtRed;
                sumGreen += filler[i + 1][t - 1].rgbtGreen;
                sumBlue += filler[i + 1][t - 1].rgbtBlue;
                ticker++;
            }
            if ((i + 1 >= 0 && t + 1 >= 0) && (i + 1 < height && t + 1 < width))
            {
                sumRed += filler[i + 1][t + 1].rgbtRed;
                sumGreen += filler[i + 1][t + 1].rgbtGreen;
                sumBlue += filler[i + 1][t + 1].rgbtBlue;
                ticker++;
            }
            //find average colour value
            image[i][t].rgbtRed = round(sumRed / ticker);
            image[i][t].rgbtGreen = round(sumGreen / ticker);
            image[i][t].rgbtBlue = round(sumBlue / ticker);
        }
    }
    return;
}
