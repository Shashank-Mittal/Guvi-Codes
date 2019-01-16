import java.util.Scanner;
class NaturalNumberSum
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		int Number = input.nextInt();
		int sum=0;
		for(int i=1;i<=Number;i++)
			sum=sum+i;
		System.out.println(sum);  
		
	}
}