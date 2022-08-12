#include "bmp.h"

//convolutional Matrix using sobels operator
void Sobels_Operator(int height, int width, RGBTRIPLE image[height][width]);
// Allow image to locate balls and identify their color
void Ball_locate_differenciate(int height, int width, RGBTRIPLE image[height][width]);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width]);

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width]);

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width]);

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width]);
