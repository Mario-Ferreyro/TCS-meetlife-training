package Calc;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

public class CalculatorTest {

	@Test
	public void testGetSum() {
		int result = Calculator.getSum(5, 3);
		int expectedResult = 8;
		assertEquals(expectedResult, result);	
		if (result == expectedResult) {
			System.out.println("Addition OK");
		} else System.out.println("Addition has a problem");
	}

	@Test
	public void testGetDiff() {
		int result = Calculator.getDiff(5, 3);
		int expectedResult = 2;
		assertEquals(expectedResult, result);	
		if (result == expectedResult) {
			System.out.println("Substraction OK");
		} else System.out.println("Addition has a problem");
	}

}
