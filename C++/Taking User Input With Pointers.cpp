#include <iostream>
using namespace std;

int main()
{
float *GetValues(float *p, size_t n) 
  

    float input;
    int i = 0;

    if ((newPtr = (float *)malloc(n * sizeof(float))) == NULL) {
        cout << "Not enough memory\n";
        exit(EXIT_FAILURE);
    }
    cout << "Enter " << n << " float values separated by whitespace: \n";

    while (scanf("%f", &input) == 1) {
        p[i] = input;
        i++;
        cout << *p;
    }
    return p;
}

//But then if I do this:

float *GetValues(float *p, size_t n) 
{   
    float *newPtr;
    float input;

    if ((newPtr = (float *)malloc(n * sizeof(float))) == NULL) {
        cout << "Not enough memory\n";
        exit(EXIT_FAILURE);
    }
    cout << "Enter " << n << " float values separated by whitespace: \n";

    while (scanf("%f", &input) == 1) {
            *newPtr++ = input;
    }
    return newPtr;
}

