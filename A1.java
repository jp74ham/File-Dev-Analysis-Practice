/*  Purpose: This program takes a non-negative integer number as input and displays the first n Fibonacci numbers.
    Started: 11:30 AM
    Set up: 11:37 AM
        - haven't practiced coding in Java for a while, had to look up imports and syntax for class files and methods
    Finished: 11:55 AM
    Total development time: 25 minutes
*/

import java.io.*;
import java.util.*;

public class A1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a non-negative integer number: ");
        int n = input.nextInt();
        if(n < 0){
            System.out.println("Invalid input: Enter a Non-negative integer number.");
        } else {
            for (int i = 1; i <= n; i++) {
                System.out.print(fibonacci_display(i) + " ");
            }
            System.out.println();
        }
    }

    public static int fibonacci_display(int n){
        if (n==1){
            return 0;
        }
        if (n==2){
            return 1;
        }
        return fibonacci_display(n-1) + fibonacci_display(n-2);
    }
}