#include <stdio.h>

int main() {
    int i, j;
    int isPrime;

    printf("1000以内的质数：\n");

    for (i = 2; i < 1000; i++) {
        isPrime = 1;  // 先假设 i 是质数

        for (j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                isPrime = 0;  // 找到因子，不是质数
                break;
            }
        }

        if (isPrime) {
            printf("%d ", i);
        }
    }

    printf("\n");
    return 0;
}
