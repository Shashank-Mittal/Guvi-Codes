#include<stdio.h>
void main()
{
	char a;
	scanf("%c",&a);
	if((('a'<=a)&&(a<='z'))||(('A'<=a)&&(a<='Z')))
	printf("Alphabet");
	else
	printf("NO");
}
