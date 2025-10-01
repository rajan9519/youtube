#include <stdio.h>

int main()
{
    float sinx , pterm , x ;
    int sign = -1 , n ;

    scanf("%f",&x) ;

    sinx = x;
    pterm = x;

    float term = x , sin = x ;
    for(int i = 1 ; i < 15 ; i++ )
    {
        sinx = sinx + sign * pterm * x * x / ( 2* i * ( 2*i + 1 ) ) ;
        pterm = pterm * x * x / ( 2 * i * ( 2 * i + 1 ) ) ;
        sign = -1 * sign;
    }
    printf("%f",sinx);

}

