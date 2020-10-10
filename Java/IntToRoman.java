/**
 * Class that contains the method for converting an Integer number to a Roman
 * numeral.
 * 
 * @author José Igor de Farias Gomes
 *
 */
public class IntToRoman {

	/**
	 * Final array that storages the numbers less than or equal to 1000 which have a
	 * fixed equivalent in the roman numerals.
	 */
	private final int[] NUMBERS = { 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000 };

	/**
	 * Final array that storages the fixed roman numerals less than or equal to
	 * 1000.
	 */
	private final String[] ROMANS = { "I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM" };

	/**
	 * Converts a specified number to its roman equivalent
	 * 
	 * @param number the number that will be converted
	 * @return the roman equivalent for the integer received as parameter 
	 */
	public String convert(int number) {
		return convert(number, NUMBERS.length - 1);
	}

	private String convert(int number, int currentIndex) {
		if (number == 0)
			return "";

		if (number >= NUMBERS[currentIndex])
			return ROMANS[currentIndex] + convert(NUMBERS[currentIndex] - number, currentIndex - 1);

		return "";
	}

}
