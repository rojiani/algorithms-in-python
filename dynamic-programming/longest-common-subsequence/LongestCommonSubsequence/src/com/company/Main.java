package com.company;

/**
 * Longest Common Subsequence
 * See CLRS Algorithms
 */
public class Main {


    public static void main(String[] args) {
	    String[][] arrows1 = lcs("aaaa", "xaxaxaax");
        backtrack(arrows1, "aaaa", "xaxaxaax");
        String[][] arrows2 = lcs("human", "ghostman");
        backtrack(arrows2, "human", "ghostman");

    }

    public static String[][] lcs(String x, String y) {
        int m = x.length();
        int n = y.length();
        int[][] c = new int[m][n];
        String[][] b = new String[m][n];

        // initialize i = 0 and j = 0 cells of c
        for (int i = 0; i < m; i++) {
            c[i][0] = 0;
        }
        for (int j = 0; j < n; j++) {
            c[0][j] = 0;
        }
        // initialize all cells in b to be "X"
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                b[i][j] = "X";
            }
        }


        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (x.charAt(i) == y.charAt(j)) {
                    c[i][j] = c[i - 1][j - 1] + 1;
                    b[i][j] = "D";  // diagonal, was having issues with comparing "\\"
                }
                else if (c[i - 1][j] >= c[i][j - 1]) {
                    c[i][j] = c[i - 1][j];
                    b[i][j] = "^";
                }
                else {
                    c[i][j] = c[i][j - 1];
                    b[i][j] = "<";
                }
            }
        }

        System.out.println("Values:");
        print2dArrayInt(c, m, n);
        System.out.println("\nArrows:");
        print2dArrayStr(b, m, n);
        return b;
    }


    public static String backtrack(String[][] b, String x, String y) {
        int i = x.length() - 1;
        int j = y.length() - 1;
        StringBuilder lcsRev = new StringBuilder();
        while (i > 0 && j > 0) {
            //System.out.println("b[" + i + "][" + j + "] = " + b[i][j]);
            if (b[i][j].equals("D")) {
                //System.out.println("D");
                i--;
                j--;
                assert x.charAt(i) == y.charAt(j);
                lcsRev.append(x.charAt(i));
                //System.out.println(lcsRev.toString());
            }
            else if (b[i][j].equals("<")) {
                //System.out.println("<");
                j--;
            }
            else { // (b[i][j].equals("^")) {
                //System.out.println("^");
                i--;
            }
        }
        String lcs = lcsRev.reverse().toString();
        System.out.println("\nLCS: " + lcs);
        return lcs;
    }


    public static void print2dArrayInt(int[][] matrix, int rows, int cols) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }


    public static void print2dArrayStr(String[][] matrix, int rows, int cols) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
