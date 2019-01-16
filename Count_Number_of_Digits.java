import java.util.Scanner;
class Count_Number_of_Digits
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		int Number = input.nextInt();
		int count=0;
		while(Number!=0){
			Number = Number/10;
			count++;
		}
		System.out.println(count);  
		
	}
}