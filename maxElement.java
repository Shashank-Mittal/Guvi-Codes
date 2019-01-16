import java.util.Scanner;
class maxElement{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String p= input.nextLine();
		String[] numbers_string = p.split(" ");
		int[] number=new int[numbers_string.length];
		for(int i=0;i<numbers_string.length;i++)
		{
			number[i]=Integer.parseInt(numbers_string[i]);
		}
		int max=number[0];
		for(int i=1;i<number.length;i++)
		{
			if(max<number[i])
			max=number[i];	
		}
		System.out.println(max);
	}
		
}