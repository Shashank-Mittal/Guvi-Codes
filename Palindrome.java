import java.util.Scanner;
class Palindrome
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		int Number1 = input.nextInt();
		int CopyOfNumber1=Number1;
		int CopyOfNumber2=Number1;
		int count=0;
		while(CopyOfNumber2>0){
			CopyOfNumber2=CopyOfNumber2/10;
			count++;
		}
		int power=1;
		int copyOfCount=count;
		while(count>1)
		{
			power=power*10;
			count--;

		}
		int sum=0;
		while(power>0)
		{
			int mod =Number1%10;
			int Number4=power*mod;
			sum= sum+Number4;
			Number1=Number1/10;
			power=power/10;
		}
		if(sum==CopyOfNumber1)
		System.out.println("Yes");
	else
		System.out.println("NO");

	}
}