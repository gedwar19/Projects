import org.junit.Test;
import static org.junit.Assert.*;

public class ShapeCalcTest {
	@Test
	public void calcCircleAreaShouldReturnCorrectValue() {
		ShapeCalc scalc = new ShapeCalc();
		assertEquals(78.54,scalc.calcCircleArea(5.0),0.01);
	}
	@Test
	public void calcCircleCircShouldReturnCorrectValue() {
		ShapeCalc scalc = new ShapeCalc();
		assertEquals(31.42,scalc.calcCircleCirc(5.0),0.01);
	}
	@Test
	public void calcRectAreaShouldReturnCorrectValue() {
		ShapeCalc scalc = new ShapeCalc();
		assertEquals(30,scalc.calcRectArea(5.0, 6.0),0.01);
	}
	@Test
	public void calcRectPerimShouldReturnCorrectValue() {
		ShapeCalc scalc = new ShapeCalc();
		assertEquals(22,scalc.calcRectPerim(5.0, 6.0),0.01);
	}
}
