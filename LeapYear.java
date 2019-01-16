import java.util.Scanner;
class LeapYear {
	public static void main(String[] args) {
	Scanner input = new Scanner(System.in);
	int Year=input.nextInt();
	if(Year%4==0)
	{
		if(Year %100==0)
		{
			if(Year%400==0)
				System.out.println("yes");
			else
				System.out.println("no");

		}
		else
			System.out.println("yes");
	}
	else {
		System.out.println("no");
	}
}

}