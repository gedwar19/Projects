import java.util.ArrayList;
import java.util.Random;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class Tile{
	private String type;
	private int red;
	private int green;
	private int blue;
	private String letter;
	private int x;
	private int y;
	
	//default constructor sets tile information to 0
	public Tile ()
	{
		this("",0,0,0,"",0,0);
	}
	//constructor sets tile information
	public Tile (String type, int red, int green, int blue, String letter, int x, int y)
	{
		this.type = type;
		this.type = type;
		this.red = red; 
		this.green = green;
		this.blue = blue;
		this.letter = letter;
		this.x = x;
		this.y = y;
	}
	//get and set methods for the tiles information
	public String getType(){
		return type;
	}
	public void setType(String type){
		this.type = type;
	}
	
	public void setColor(int r, int g, int b)
	{
		red = r;
		green = g;
		blue = b;
	}
	public int getRed(){
		return red;
	}
	public void setRed(int red){
		this.red = red;
	}
	
	public int getGreen(){
		return green;
	}
	public void setGreen(int green){
		this.green = green;
	}
	
	public int getBlue(){
		return blue;
	}
	public void setBlue(int blue){
		this.blue = blue;
	}
	
	public String getLetter(){
		return letter;
	}
	public void setLetter(String letter){
		this.letter = letter;
	}
	
	public int getX(){
		return x;
	}
	public void setX(int x){
		this.x = x;
	}
	public int getY(){
		return y;
	}
	public void setY(int y){
		this.y = y;
	}
	//ToString method to print the Tiles inforamtion
	public String toString(){
		return String.format("The shape is a %s, the cordinates of the tile are %d %d, the letter is %s, the color combination is (red,green, blue) (%d,%d,%d)",type, x,y, letter, red,green,blue);
	}
}

class TilePanel extends JPanel
{
	private ArrayList<Tile> tiles;
	public void setTiles(ArrayList<Tile> tiles){
		this.tiles = tiles;
	}
	public ArrayList<Tile> getTiles(){
		return tiles;
	}
	
	public TilePanel(){
		this(null);
	}
	//constructor to receive tiles list
	public TilePanel (ArrayList<Tile> tiles){
		this.tiles = tiles;
	}
	
	//paints the tiles to the frame
	public void paintComponent(Graphics g){
		super.paintComponent(g); //any lightweight components contained inside TilePanel will be rendered
		//color object to create a color using integer values
		Color c;
		
		if(tiles != null){
			for (Tile t : tiles){
				//color object to create a color using integer values (Red, Green, Blue)
				c = new Color(t.getRed(),t.getGreen(),t.getBlue());
				//sets the color of the tile
				g.setColor(c);
				//draws shape depending on if it is a circle or rectangle
				if (t.getType() == "Circle")
				{
				g.fillOval(t.getX(), t.getY(), 30, 30);
				}
				else
				{
					g.fillRect(t.getX(), t.getY(), 30, 30);
				}
				//changed the color to view the Letter
				g.setColor(new Color(255,255,255));
				g.drawString(t.getLetter(), t.getX()+12, t.getY()+20);
			}
			
		}
	}
	
}
class TileFrame extends JFrame 
{
	private TilePanel pan;
	private ArrayList<Tile> tiles;
	private TileRandomizer randomTiles = new TileRandomizer();
	public TileFrame(){
		this(null);
	}
	public TileFrame(ArrayList<Tile> tiles){
		this.tiles = tiles;
		setupUI();
	}
	//creates the frame
	public void setupUI(){
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(10,10,400,400);
		//create panel object
		pan =  new TilePanel(tiles);
		//container
		Container c = getContentPane();
		c.setLayout(new BorderLayout());
		c.add(pan, BorderLayout.CENTER);
		JPanel entryPanel = new JPanel();
		entryPanel.setLayout(new FlowLayout());
		//create Random button
		JButton btnRandom = new JButton("Randomize");
		//action listener to randomize the tiles information and display it when button is clicked
		btnRandom.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e){
				pan.setTiles(randomTiles.changeTiles(tiles));
				repaint();
			}
		});
		//adds the random button to the panel
		entryPanel.add(btnRandom);
		c.add(entryPanel, BorderLayout.SOUTH);
	}
}

class TileRandomizer 
{
	//create random object
	private Random rnd = new Random();
	
	//constructors
	TileRandomizer()
	{
		buildTile(0,0);
	}
	
	TileRandomizer(int x, int y)
	{
		buildTile(x,y);
	}
	//creates new tiles, while taking x and y position as parameters
	public Tile buildTile(int x, int y)
	{
		String type;
		String letter;
		//ramdomly generates shape (circle or rectangle)
		int shape = rnd.nextInt(2);
		if (shape == 1)
		{
			type = "Circle";
		}
		else
		{
			type = "Square";
		}
		//creates a letter from the ascii value from 25-65
		letter = new Character((char)(rnd.nextInt(25)+65)).toString();
		
		//uses Tile constructor to create a new tile
		Tile oneTile = new Tile(type,rnd.nextInt(255),rnd.nextInt(255),rnd.nextInt(255),letter,x,y);
		return oneTile;
	}
	
	//changes the shape, letter and color of the tile
	public Tile changeTile(Tile t)
	{
		String type;
		//ramdomly generates shape (circle or rectangle)
		String letter;
		int shape = rnd.nextInt(2);
		if (shape == 1)
		{
			type = "Circle";
		}
		else
		{
			type = "Square";
		}
		
		//creates a letter from the ascii value from 25-65
		letter = new Character((char)(rnd.nextInt(25)+65)).toString();
		
		//sets the new shape, color, and letter 
		t.setType(type);
		t.setColor(rnd.nextInt(255),rnd.nextInt(255),rnd.nextInt(255));
		t.setLetter(letter);
		
		return t;
	}
	
	//Takes in an Arraylist of Tiles and calls the function changeTile
	//to change the values for each individual tile
	public ArrayList<Tile> changeTiles (ArrayList<Tile> Tiles)
	{
		
		for (Tile t : Tiles)
		{
			changeTile(t);
		}
		return Tiles;
	}
}

//class to print the tiles information
class TilePrinter
{
	public static ArrayList<Tile> print (ArrayList<Tile> Tiles)
	{
		for (Tile t : Tiles)
		{
			System.out.println(t.toString());
			
		}
		return Tiles;
	}
}

public class Tiles_Edwards {

	public static void main(String[] args) {
		//array list of tiles
		ArrayList<Tile> tiles = new ArrayList<Tile>();
		TileRandomizer rndTile = new TileRandomizer();
		
		//gives the position for each tile
		for (int x = 0; x <300; x=x+30)
		{
			for (int y = 0; y <300; y=y+30)
			{
				//adds each tile to the list
				tiles.add(rndTile.buildTile(x, y));
			}
		}
		
		//calls function to print tiles
		TilePrinter.print(tiles);
		//makes the frame visible
		TileFrame tf = new TileFrame(tiles);
		tf.setVisible(true);
	}

}
