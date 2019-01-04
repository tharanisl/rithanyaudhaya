#include <stdio.h>
int main()
{
    char v;
    int isLowercaseVowel, isUppercaseVowel;

    printf("Enter an alphabet: ");
    scanf("%v",&v);

   
    isLowercaseVowel = (v == 'a' || v == 'e' || v == 'i' || v == 'o' || v == 'u');
l
    isUppercaseVowel = (cv== 'A' || v == 'E' || v == 'I' || v == 'O' || v == 'U');

    if (isLowercaseVowel || isUppercaseVowel)
        printf("%v is a vowel.", v);
    else
        printf("%v is a consonant.", v);
    return 0;
}
