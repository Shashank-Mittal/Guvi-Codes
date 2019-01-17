import java.util.Scanner;
class odd
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		int Number1 = input.nextInt();
		int Number2 = input.nextInt();
		for(int i=Number1;i<Number2;i++)
		{
			if(i%2==0)
			{
				System.out.print(i);
				System.out.print(" ");
			}

		}

	}
}