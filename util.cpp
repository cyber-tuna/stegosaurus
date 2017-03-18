#include <fstream>
#include "util.h"

void print_char_array(char* c, int n)
{
    for(int i = 0; i < n; i++)
    {
        printf("%c", c[i]);
    }

    printf("\n");
}