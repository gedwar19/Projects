
public class TextAnalyzer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
	}

	public int countVowels(String word)
	{
		int vowels = 0;
		word = word.toUpperCase();
		for (int a = 0 ; a < word.length(); a++)
		{
			if ((word.charAt(a)== 'A')||(word.charAt(a)== 'E')||(word.charAt(a)== 'I')||(word.charAt(a)== 'O')||(word.charAt(a)== 'U')||(word.charAt(a)== 'Y'))
			{vowels++;}
		}
		
		return vowels;
	}
	public int countWords(String sentence)
	{
		int words = 0;
		
		String [] sen =sentence.split(" ");
		words = sen.length;
		
		return words;
	}
}
