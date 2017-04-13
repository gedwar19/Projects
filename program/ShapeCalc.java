import java.util.Scanner;
public class ShapeCalc {
	public double calcCircleArea(double rad) {
		return Math.PI * rad * rad;
	}
	public double calcCircleCirc(double rad) {
		return 2 * Math.PI * rad;
	}
	public double calcRectArea(double wid, double len) {
		return wid * len;
	}
	public double calcRectPerim(double wid, double len) {
		return 2 * (wid + len);
	}
	public void showMenu() {
		System.out.println("Menu");
		System.out.println("1. Circles");
		System.out.println("2. Rectangles");
		System.out.print("Enter number of your choice: ");
	}
	public void execute() {
		Scanner sc = new Scanner(System.in);
		int choice;
		double area;
		double perim;
		double radius;
		double width;
		double height;
		do {
			showMenu();
			System.out.print("Enter you choice: ");
			choice = sc.nextInt();
			switch (choice) {
				case 1:
					System.out.print("Enter radius: ");
					radius = sc.nextDouble();
					area = calcCircleArea(radius);
					perim = calcCircleCirc(radius);
					System.out.printf("Area = %.2f\tCirc = %.2f\n",area,perim);
					break;
				case 2:
					System.out.print("Enter width and height: ");
					width = sc.nextDouble();
					height = sc.nextDouble();
					area = calcRectArea(width,height);
					perim = calcRectPerim(width,height);
					System.out.printf("Area = %.2f\tPerim = %.2f\n", area,perim);
					break;
			}
		} while (choice != 3);
	}
	public static void main(String[] args) {
		ShapeCalc me = new ShapeCalc();
		me.execute();
	}
}
