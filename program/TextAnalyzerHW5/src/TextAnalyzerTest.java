import org.junit.Test;
import static org.junit.Assert.*;
public class TextAnalyzerTest {

	@Test
	public void countVowelsShouldReturnCorrectValue() {
		
		TextAnalyzer text = new TextAnalyzer();
		assertEquals(3, text.countVowels("Elephant"));
	}
	@Test
	public void countWordsShouldReturnCorrectValue() {
		TextAnalyzer text = new TextAnalyzer();
		assertEquals(6,text.countWords("See spot run, run spot run"));
	
	}
}
