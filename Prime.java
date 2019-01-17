import java.util.Scanner;
class Prime
{
	public static void main(String[] args) 
	{
		int flag = 0;
		Scanner input = new Scanner(System.in);
		int Number1 = input.nextInt();
		if(Number1!=1 || Number1!=2)
		{
		for(int i=2;i<Number1;i++)
		{
				if(Number1%i==0)
				 flag=1;
		}
	}
		if(flag==0)
			System.out.println("yes");
		else
			System.out.println("No");

	}
}