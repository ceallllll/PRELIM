import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int num1 = input.nextInt();

        System.out.print("Enter second number: ");
        int num2 = input.nextInt();

        System.out.print("Enter third number: ");
        int num3 = input.nextInt();

        int highest = num1;

        if (num2 > highest) {
            highest = num2;
        }

        if (num3 > highest) {
            highest = num3;
        }

        System.out.println("The highest number is " + highest);
    }
}
