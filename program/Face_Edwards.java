
//requires shapes class and circle class to be packaged with 
import java.util.ArrayList;
import java.awt.*;
import java.util.Random;
import javax.swing.*;

//draws on panel
class FacePanel extends JPanel{
	private ArrayList<Face> faces; 
	public FacePanel(){
		this.faces = null;
	}
	public FacePanel(ArrayList<Face> faces){
		this.faces = faces;
	}
	//draws the faces
	public void paintComponent(Graphics g){
		super.paintComponent(g);//draws internal components if any
		if(faces!= null){
			for (Face f : faces){
				
				g.drawOval(f.getX(), f.getY(), f.getWidth(), f.getHeight());//head
				g.drawOval(f.getX()+(f.getWidth()/4), f.getY()+10, 10, 10);//eyes
				g.drawOval(f.getX()+(f.getWidth()/2), f.getY()+10, 10, 10);//eyes
				//smile, frown neutral
				if (f.getSmile()== 0)
				{
					g.drawArc(f.getX()+(f.getWidth()/4), f.getY()+ (f.getHeight()/2), (f.getWidth()/2), (f.getHeight()/100), 0, 180);//mouth
				}
				else if (f.getSmile()== 2)
				{
					g.drawArc(f.getX()+(f.getWidth()/4), f.getY()+ (f.getHeight()/2), (f.getWidth()/2), (f.getHeight()/2), 180, 180);//mouth
				}
				else if (f.getSmile()==1)
				{
				g.drawArc(f.getX()+(f.getWidth()/4), f.getY()+ (f.getHeight()/2), (f.getWidth()/2), (f.getHeight()/2), 0, 180);//mouth
				}
			}
		}
	}
}
//create frame
class FaceFrame extends JFrame{
	private FacePanel cp;
	
	public FaceFrame(){
		
	}
	
	public FaceFrame(ArrayList<Face> faces){
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100,100,300,300);
		Container c = getContentPane();
		c.setLayout(new BorderLayout());
		
		cp = new FacePanel(faces);
		c.add(cp,BorderLayout.CENTER);
		
		
	}
}

public class Face_Edwards {
	//function to print the faces
	public static void printCircles(ArrayList<Face> faces){
		for (Face f : faces){
			System.out.println(f);
		}
	}
	 
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<Face> faces = new ArrayList<Face>();
		//create random number
		Random rnd = new Random(); 
		//gives random values for x,y,height, width, smile
		int loop = rnd.nextInt(7)+ 3;
		for (int a = 0; a < loop; a++)
		{
			faces.add (new Face(rnd.nextInt(200), rnd.nextInt(200), rnd.nextInt(30)+30, rnd.nextInt(30)+30, rnd.nextInt(3)));
			
		}
		
		FaceFrame ff = new FaceFrame(faces);
		ff.setVisible(true);
		//print
		printCircles(faces);
	}

}


class Face extends Shape{
	private int width;
	private int height;
	private int smile;
	
	//width
	public int getWidth()
	{
		return width;
	}
	public void setWidth(int w)
	{
		if (w >0)
		{
			width = w;
		}
	}
	
	//smile
	public int getSmile()
	{
		return smile;
	}
	public void setSmile(int s)
	{
		if (s < 3 && s >= 0)
		{
			smile = s;
		}
	}
	//height
	public int getHeight()
	{
		return height;
	}
	public void setHeight(int h)
	{
		if (h >0)
		{
			height = h;
		}
	}
	//default constructor
	public Face()
	{
		super();// calls the super class default constructors
		width = 0;
		height = 0;
		smile = 0;
	}
	
	public Face(int x, int y, int wid, int hght, int sml)
	{
		super(x,y);
		setWidth(wid);
		setHeight(hght);
		setSmile(sml);
	}
	
	//tostring that prints the smile type
	public String toString() {
		String sml;
		if (getSmile()== 0)
		{
			sml = "neutral";
		}
		else if (getSmile()== 1)
		{
			sml = "Frown";
		}
		else 
		{
			sml = "Smile";
		}
		
		return String.format("This object is a %s", sml);
	}
	//required to satisfy shapes class
	public double area() {
		return Math.PI * width * height;//not correct formula
	}
	public double perim() {
		return 2 * Math.PI * width * height;//not correct formula
	}
}
