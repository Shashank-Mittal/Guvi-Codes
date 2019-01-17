import java.util.Scanner;
class PrimeSeries{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		int Number1 = input.nextInt();
		int Number2 = input.nextInt();
		int flag=0;
		if(Number2==2)
			System.out.print("1");
		else
		{
		for(int i=Number1;i<Number2;i++)
		{
			flag=0;
			for(int j=2;j<i/2;j++)
			{
			if(i%j==0)
				flag=1;
			}
			if(flag==0){
				System.out.print(i);
				System.out.print(" ");
			}

		}
	}

	}
}