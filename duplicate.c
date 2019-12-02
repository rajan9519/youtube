#include <stdio.h>

int main()
{
    int n;
    // size of the array
    scanf("%d",&n);

    int arr[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    // initialize current unique element as the 0'th index value
    // and set unique index counter to 0
    int cur_unique = arr[0], unique_index = 0;
    for(int i=1;i<n;i++)
    {
        // if current array value and current unique value are different
        // then do the following
        // update current unique value by current array element
        // increment unique index counter and replace
        // unique_index element of array by current array value
        if(arr[i] != cur_unique)
        {
            cur_unique = arr[i];
            unique_index++;
            arr[unique_index] = arr[i];
        }
        // else do nothing
    }

    // printing unique value from the array
    for(int i=0;i<=unique_index;i++)
    {
        printf("%d ",arr[i]);
    }
    return 0;
}
