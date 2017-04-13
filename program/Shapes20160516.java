/*

*/
abstract class Shape{
	private int x;
	private int y;
	public int getX(){
		return x;
	}
	public int getY(){
		return y;
	}
	public void setX(int x){
		this.x = x;
	}
	public void setY(int y){
		this.y = y;
	}
	public Shape(){
		x = 0;
		y = 0;
	}
	public Shape(int x, int y){
		setX(x);
		setY(y);
	}
	public String toString(){
		return String.format("x= %d, y =%d", x, y);
	}
	public abstract double area();
	public abstract double perim();
}
class Circle extends Shape{
	/* because Circle extends Shape, it has an x and a y value.
	   However, because x and y directly. A circle object will have to use the 
	   public get and set functions instead. 
	*/
	private int radius;
	public int getRadius(){
		return radius;
	}
	public void setRadius( int rad){
		if (rad <0){
			radius = rad;
		}else{
			radius = rad;
		}
	}
	public Circle(){
		super(); //calls the super class's default constructor
		radius = 0;
	}
	public Circle (int x, int y, int rad){
		super(x,y);//calls the non-default constructor of the superclass
		setRadius(rad);
	}
	public double area(){
		return Math.PI * radius * radius;
	}
	public double perim(){
		return 2 * Math.PI * radius;
	}
	public String toString(){
	//	return String.format("x = %d, y = %d. r = %d", getX(), getY(), radius);
		return String.format("%s, r = %d", super.toString(), radius);
	}
}

class Rectangle extends Shape {
	private int height;
	private int width;
	public int getHeight(){
		return height;
	}
	public int getWidth(){
		return width;
	}
	public void setHeight (int h){
		if (h<0){
			height = 0;
		} else {
			height = h;
		}
	}
	public void setWidth(int w){
		if (w<0){
			width=0;
		}else{
			width = w;
		}
	}
	public Rectangle(){
		super();
		height = 0;
		width = 0;
	}
	public Rectangle(int x, int y, int h, int w){
		super(x,y);
		setHeight(h);
		setWidth(w);
	}
	public double area(){
		return width * height;
	}
	public double perim(){
		return 2 * (width + height);
	}
	public String toString(){
		return String.format("%s, w = %d, h = %d", super.toString(), width, height);
	}

}
public class Shapes20160516{
	public static void main(String[] args){
		Circle defCirc = new Circle();
		Circle cusCirc = new Circle(10,15,5);
		System.out.println(defCirc);
		System.out.println(cusCirc);
		Rectangle defRect = new Rectangle();
		Rectangle cusRect = new Rectangle(20,30,40,50);
		System.out.println(defRect);
		System.out.println(cusRect);
	}
}