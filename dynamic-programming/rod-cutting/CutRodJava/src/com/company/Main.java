package com.company;


import java.util.Arrays;
import java.util.Scanner;

/*
 * CLRS Rod Cutting (15.1)
 * Top-down approach, recursive
 */
public class Main {

    /** Number of entries in prices */
    private static final int NUM_PRICES = 11;

    /** Cash-in value p_i, where i = length of rod */
    private static final int[] prices = { 0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30 };

    /** Array storing the optimal value for length i, r_i in book */
    private static int[] optimals = new int[NUM_PRICES + 1];


    public static void main(String[] args) throws Exception {
        System.out.print("Enter the length of the rod: ");
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        if (n <= 0 || n >= NUM_PRICES) {
            throw new Exception("Invalid input. Rod size must be integer between 1 and " + (NUM_PRICES - 1));
        }
        Arrays.fill(optimals, Integer.MIN_VALUE);
        int optimal = cutRod(n);
        System.out.println("Maximum Value of rod of length " + n + " is " + optimal);
    }

    public static int cutRod(int n) {

        if (optimals[n] != Integer.MIN_VALUE) {    // Already computed
            return optimals[n];
        }
        int q;
        if (n == 0) {
            q = 0;
        } else {
            q = Integer.MIN_VALUE;   // q = optimal for n
            for (int i = 1; i <= n; i++) {
                q = Math.max(q, prices[i] + cutRod(n - i));
            }
        }
        optimals[n] = q;
        return q;
    }




}
