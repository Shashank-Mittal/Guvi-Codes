import java.util.Scanner;
class PowerOfNumber
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		int Number1 = input.nextInt();
		int Number2 = input.nextInt();
		int CopyOfNumber1=Number1;
		while(Number2>1){
			Number1 = Number1*CopyOfNumber1;
			Number2--;
		}
		System.out.println(Number1);  
		
	}
}