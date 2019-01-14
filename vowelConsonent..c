#include<stdio.h>
void main()
{
	char a;
	if(scanf("%c",&a)!=1)
	printf("Invalid");
	else{
	if(a=='A'||a=='a'||a=='E'||a=='e'||a=='I'||a=='i'||a=='o'||a=='O'||a=='u'||a=='U')
	printf("Vowel");
	else if((('a'<=a)&&(a<='z'))||(('A'<=a)&&(a<='Z')))
	printf("Consonant");
	else
	printf("Invalid");
}
}
