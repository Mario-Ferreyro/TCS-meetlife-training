package Calc;

import java.util.Scanner;

public class Calculator {

        public static void main(String[] args) {

            System.out.println("please input two numbers");
            try (Scanner scanner = new Scanner(System.in)) {
				System.out.println("Number 1: ");
				int n1 = scanner.nextInt();
				System.out.println("Number 2: ");
				int n2 = scanner.nextInt();

				System.out.println("What Operation do you want to make? [S]Sum or [D]Difference: ");
				String operation = scanner.next();
				operation = operation.toLowerCase();

				System.out.println("The result is: " );

				if (operation.equals("s")) {
				    int sum = getSum(n1, n2);
				    System.out.println(sum);
				} else if (operation.equals("d")) {
				    int diff = getDiff(n1, n2);
				    System.out.println(diff);
				} else  System.out.println("invalid option" );
			}

        }
        static int getSum(int n1, int n2) {
            return n1 + n2;
        }

        static int getDiff(int n1, int n2) {
            return n1 - n2;
        }
    }
