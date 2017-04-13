import java.util.Scanner;
/**
This class ask the user for two integers, adds them together and shows the result.
@author Gilbert Edwards
*/
public class Test20160516{

	/**
	This function takes two integers, adds them together, and returns the result.
	@param n1 The first number
	@param n2 The second number
	@return The sum n1+n2
	*/

	public static int add(int n1, int n2){
		return n1+ n2;
	}
	/**
	This function takes an integer that represents a sum and prints
	it as part of a sentence that explains what it is.
	@param result The value we want to show 
	*/
	public static void showResult(int result){
		System.out.printf("The sum is %d. \n", result);
	}
	public static void main(String[] args){
		int num1;
		int num2;
		int ans;
		System.out.println("this program will ask the user for two numbers and");
		System.out.println("will add them together.");
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter the first number: ");
		num1 = Integer.parseInt(sc.nextLine());
		System.out.print("Enter the second number: ");
		num2 = Integer.parseInt(sc.nextLine());
		ans = add(num1, num2);
		showResult(ans);
	}
}