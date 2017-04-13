import java.util.ArrayList;
import java.io.*;
import java.util.Scanner;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
class Point {
	private int x;
	private int y;
	
	public Point(int x, int y){
		this.x = x;
		this.y = y;
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
	public String toString(){
		return String.format("%d %d",x,y);
	}
	

}

class PointIO{
	public boolean writeFile(ArrayList<Point> points, String fname){
		return writeFile(points, new File(fname));
	}
	public boolean writeFile(ArrayList<Point> points, File file){
		try{
			FileWriter fw = new FileWriter(file);
			BufferedWriter bw = new BufferedWriter(fw);
			for (Point p : points){
				bw.write(p.toString());
				bw.newLine();
			}
			bw.close();
			return true;
		} catch (Exception ex){
			return false;
		}
	}
	public ArrayList<Point> readFile(String fname){
		return readFile(new File(fname));
	}
	public ArrayList<Point> readFile(File file){
		try{
			ArrayList<Point> result;
			Scanner sc = new Scanner(file);
			result = new ArrayList<Point>();
			String line;
			String[] parts;
			Point p;
			while (sc.hasNextLine()){
				line = sc.nextLine();
				parts = line.split(" ");
				p = new Point(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]));
				result.add(p);
			}
			sc.close();
			return result;	
		} catch (Exception ex){
			return null; //no point were read from file
		}
	}
}
class LinePanel extends JPanel implements MouseListener, MouseMotionListener, ActionListener{
	private ArrayList<Point> points;
	private int pointSize;
	private int xpos;
	private int ypos;
	private Timer tim;
	public void setPoints(ArrayList<Point> points){
		this.points = points;
	}
	public ArrayList<Point> getpoints(){
		return points;
	}
	public int getPointSize(){
		return pointSize;
	}
	public void setPointSize(int ps){
		if (ps < 0 ){
			pointSize = 5;
		}else{
			pointSize = ps;
		}
	}
	public LinePanel(){
		this(null);
	}
	public LinePanel (ArrayList<Point> points){
		this.points = points;
		pointSize = 5;
		xpos = 0;
		ypos = 0;
		addMouseListener(this);
		addMouseMotionListener(this);
		tim = new Timer(1000, this);
		tim.start();
	}
	public void actionPerformed(ActionEvent e){
		if (points != null){
			for (Point p : points){
				p.setX(p.getX() + 5);
				p.setY(p.getY() + 5);
			}
			repaint();
		}
	}
	public void mouseEntered(MouseEvent e){}
	public void mouseExited(MouseEvent e){}
	public void mouseClicked(MouseEvent e){}
	public void mouseReleased(MouseEvent e){}
	public void mousePressed(MouseEvent e){
		Point p = new Point(e.getX(), e.getY());
		points.add(p);
		repaint();
	}
	public void mouseDragged(MouseEvent e){}
	public void mouseMoved(MouseEvent e){
		xpos = e.getX();
		ypos = e.getY();
		repaint();
	}
	public void paintComponent(Graphics g){
		super.paintComponent(g); //any lightweight compents contained inside LinePanel will be rendered
		Point prevPoint = null;
		if(points != null){
			for (Point p : points){
				g.fillOval(p.getX(), p.getY(), pointSize, pointSize);
				if (prevPoint != null){
					g.drawLine(prevPoint.getX(), prevPoint.getY(), p.getX(), p.getY());
				}
				prevPoint = p;
			}			
		}
		String locationString;
		locationString = String.format("Mouse at (%d, %d)", xpos, ypos);
		g.drawString(locationString, 20, 300);
	}
}

class LineFrame extends JFrame implements KeyListener{
	private LinePanel pan;
	private ArrayList<Point> points;
	private JTextField txtSize;
	private PointIO pio;

	public LineFrame(){
		this(null);
	}
	public LineFrame(ArrayList<Point> points){
		this.points = points;
		pio = new PointIO();
		setupUI();
	}
	public void setupUI(){
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(10,10,400,400);
		pan = new LinePanel(points);
		Container c = getContentPane();
		c.setLayout(new BorderLayout());
		c.add(pan, BorderLayout.CENTER);
		JPanel entryPanel = new JPanel();
		entryPanel.setLayout(new FlowLayout());
		JLabel lblSize = new JLabel("Point size");
		txtSize = new JTextField(5);
		txtSize.addKeyListener(this);
		JButton btnSize = new JButton("Set");
		btnSize.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e){
				int size = Integer.parseInt(txtSize.getText());
				pan.setPointSize(size);
				repaint();
			}
		});
		entryPanel.add(lblSize);
		entryPanel.add(txtSize);
		entryPanel.add(btnSize);
		c.add(entryPanel, BorderLayout.SOUTH);
		setupMenu();	
	}
	public void setupMenu(){
		JMenuBar mbar = new JMenuBar();
		JMenu mnuFile = new JMenu("File");
		JMenuItem miOpen = new JMenuItem("Open");
		miOpen.addActionListener (new ActionListener(){
			public void actionPerformed(ActionEvent e){
				points.clear();
				points = pio.readFile("points.txt");
				pan.setPoints(points);
				repaint();
			}
		});
		mnuFile.add(miOpen);
		JMenuItem miSave = new JMenuItem("Save");
		miSave.addActionListener (new ActionListener(){
			public void actionPerformed(ActionEvent e){
				pio.writeFile(points, "points.txt");
			}
		});
		mnuFile.add(miSave);
		JMenuItem miExit = new JMenuItem("Exit");
		miExit.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e){
				System.exit(0);
			}
		});
		mnuFile.add(miExit);
		mbar.add(mnuFile);
		JMenu mnuEdit = new JMenu("Edit");
		JMenuItem miClear = new JMenuItem("Clear");
		miClear.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e){
				points.clear();
				repaint();
			}
		
		});
		mnuEdit.add(miClear);
		mbar.add(mnuEdit);
		setJMenuBar(mbar);
	}
	public void keyTyped(KeyEvent e){
	}
	public void keyReleased(KeyEvent e){
	}
	public void keyPressed( KeyEvent e){
		if (e.getKeyCode() == KeyEvent.VK_ENTER){
			pan.setPointSize(Integer.parseInt(txtSize.getText()));
			repaint();
		}
	}	
}
public class LineDrawer20160530{
	public static void printPoints(ArrayList<Point> points){
		for (Point p : points){
			System.out.println(p);
		}
	}
	public static void main(String[] args){
		ArrayList<Point> points = new ArrayList<Point>();
		points.add(new Point(17,43));
		points.add(new Point(27,14));
		points.add(new Point(53,42));
		printPoints(points);
		PointIO pio = new PointIO();
		if (pio.writeFile(points, "points.txt")){
			System.out.println("The point were written to the file points.txt.");
		}else {
			System.out.println("An error occurred while trying to write the points to disk.");
		}
		ArrayList<Point> readFromFile;
		System.out.println("Now I'm going to read the points from the file.");
		readFromFile = pio.readFile("points.txt");
		if (readFromFile != null){
			printPoints(readFromFile);
		}else {
			System.out.println("I could not read the points from the file.");
		}
		LineFrame lf = new LineFrame(points);
		lf.setVisible(true);		
	}
}