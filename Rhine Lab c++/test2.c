#include <stdio.h>
#include <string.h>

int main(void)
{
    char input[10];

    printf("Are you wining son?: ");
    scanf("%9s", input);

    if (strcmp(input, "no") == 0)
    {
        printf("哎呀");
    }
    else if (strcmp(input, "yes") == 0)
    {
        printf("牛不牛逼");
    }

    return 0;
}