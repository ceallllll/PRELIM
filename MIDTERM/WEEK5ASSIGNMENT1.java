import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter first word: ");
        String word1 = input.next();

        System.out.print("Enter second word: ");
        String word2 = input.next();

        System.out.print("Enter third word: ");
        String word3 = input.next();

        System.out.println(word1 + " " + word2 + " " + word3);
    }
}
