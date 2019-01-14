#include<stdio.h>
void main()
{
	int a;
	char check;
	if(scanf("%d ",&a) !=1)
	printf("invalid");
	else
	{
	if(a%2==0)
	{
		printf("Even");
	}
	else{
		printf("Odd");
	}
}
}
