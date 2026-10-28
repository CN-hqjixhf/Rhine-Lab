#include <stdio.h>

int main(void)
{
    double b;
    unsigned short a = 65535;
    unsigned short k = a;
    char c, d, f, g;
    b = (1234.0 - 1) / 10;
    if (scanf(" %c %c %c %c", &c, &d, &f, &g) != 4) {
        return 1;
    }
    printf("%c,%c,%c,%c,%f,%d\n", c, d, f, g, b, k);
    return 0;
}