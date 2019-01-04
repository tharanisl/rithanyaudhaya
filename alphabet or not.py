#include <stdio.h>
int main()
{
    char v;
    printf("Enter a character: ");
    scanf("%c",&c);

    if( (v>='a' && v<='z') || (v>='A' && v<='Z'))
        printf("%c is an alphabet.",v);
    else
        printf("%c is not an alphabet.",v);

    return 0;
}
