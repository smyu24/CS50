#include <stdio.h>

void sobel_list_rotation(int saved[3][3])
{
    //Most optimal way to rotate a sobel operator list. From Gx to Gy
    int temp = 0;

    temp = saved[0][1];
    saved[0][1] = saved[1][0]; saved[1][0] = temp;

    temp = saved[0][2];
    saved[0][2] = saved[2][0]; saved[2][0] = temp;

    temp = saved[1][2];
    saved[1][2] = saved[2][1]; saved[2][1] = temp;
            //first swap 2 and 4
            // [0][1]  [1][0]

            //second, swap 3 and 7
            // [0][2]   [2][0]

            //third, swap 6 and 8
            // [1][2]  [2][1]
            /*
            problem:
            [1,2,3]
            [4,5,6]
            [7,8,9]
            answer:
            [1,4,7]
            [2,5,8]
            [9,6,3]
            */
    return;
}


void Sobels_Operator(int height, int width, RGBTRIPLE image[height][width])
{

    int gX = 0;
    int gY = 0;

    int position_rgbtriple = 0; // 0 is red, 1 is green, 2 is blue

    int saved[3][3] = {{-1,0,1},{-2,0,2},{-1,0,1}}; // for vertical, rotate clockwise (rotation function needed)
    int saved_2[3][3] = sobel_list_rotation(saved);

    for(int r = 0; r < height; r++) // row
    {
        for(int c = 0; c < width; c++) // column
        {
            //create a nested for loop that iterates one index before 0 and after the maximum index of the list (for both of the for loops)


            

            //int result = round( sqrt((sumX * sumX) + (sumY * sumY)) );



            //calculate here
            //remember about the individual red, green, blue calculations


            //apply here
            // image[r][c]
            image[r][c].rgbRed =  //square root of Gx^2 + Gy^2
            image[r][c].rgbBGreen = // square root of Gx^2 + Gy^2
            image[r][c].rgbBlue = // square root of Gx^2 + Gy^2
        }
    }
    return;
}


//for ball recognition, no edges should constitute a ball
// for getting color recognition for balls, first find the edges of a ball
//then black out its background, only leaving its color, then process inside oft he edges
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

// compute G of x and G of y for each channel of red, green, and blue

// for pixels at the border, treat any pixel past the border as having all 0 values

// compute the new channel value as the square root of Gx^2 + Gy^2