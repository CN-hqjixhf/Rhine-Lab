#include <stdio.h>

int main(void)
{
    int m, n, r, pos, i;
    int rem[101];      /* rem[x] = 余数 x 第一次出现时的小数位序号，0 表示还没出现 */
    int digit[101];    /* 依次存小数位上的数字 */

    for (i = 0; i <= 100; i++)
        rem[i] = 0;

    printf("please input a fraction (m/n))  (0< m< n<=100):");
    scanf("%d/%d", &m, &n);

    /* 小学竖式除法：每次余数乘 10 再取商、余数 */
    pos = 0;
    r = m;
    while (r != 0 && rem[r] == 0)
    {
        rem[r] = ++pos;          /* 记下这个余数出现在第几位 */
        r = r * 10;
        digit[pos] = r / n;      /* 本位商 */
        r = r % n;               /* 新的余数 */
    }

    printf("%d/%d it's accuracy value is:0.", m, n);
    for (i = 1; i <= pos; i++)
        printf("%d", digit[i]);

    if (r != 0)   /* 余数重复出现：无限循环小数 */
    {
        printf("\n\tand it is a infinite cyclic fraction from %d\n", rem[r]);
        printf("\tdigit to %d digit after decimal point.\n", pos);
    }
    else          /* 余数为 0：有限小数，没有循环节 */
    {
        printf("\n");
    }

    return 0;
}