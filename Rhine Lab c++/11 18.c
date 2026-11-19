#include <stdio.h>

int main()
{
    int N;
    printf("Input n:");
    scanf("%d",&N);
    int a[N];
    for(int i=0;i<=(N-1);i++){
    scanf("%d",&a[i]);
    }
    for(int i=0;i<=(N-1);i++){
        for(int j=0;j<=(N-1-i);j++){
            int temp;
            if(a[j]>a[j+1])
            {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
    }
    printf("Input %d numbers:",N);
    printf("Sorting results:");
    for(int i=0;i<=(N-1);i++){
        printf("%4d",a[i]);
    }
	return 0;
}