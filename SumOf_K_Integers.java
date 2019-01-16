import java.util.Scanner;
class SumOf_K_Integers
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		int Number1 = input.nextInt();
		int Number2 = input.nextInt();
		int[] arr = new int[Number1];
		for(int i=0;i<Number1;i++)
			arr[i] = input.nextInt(); 
		int sum=0;
		for(int i=0;i<Number2;i++)
			sum=sum+arr[i];
		System.out.println(sum);  
		
	}
}