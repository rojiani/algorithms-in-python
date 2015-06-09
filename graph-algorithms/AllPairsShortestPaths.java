package com.company;


/**
 * HW7 & All-Pairs Shortest Paths
 */
public class Main {

    public static void main(String[] args) {
        Double inf = Double.POSITIVE_INFINITY;
        Double[][] W = {
                {  0.0, -6.0,   inf,  1.0,  inf,  inf },
                { 11.0,  0.0,  -4.0,  inf,  inf,  inf },
                {  inf,  inf,   0.0,  inf,  inf, 20.0 },
                {  inf,  inf, -11.0,  0.0,  2.0,  inf },
                {  inf,  3.0,   inf, -1.0,  0.0,  7.0 },
                {  5.0,  inf,   inf,  inf, -3.0,  0.0 }
        };

        slowAllPairsShortestPaths(W);
        fasterAllPairsShortestPaths(W);

        Double[][] W2, W3, W6;
        W2 = computeW2(W);
        W3 = computeW3(W, W2);
        W6 = computeW6(W3);
    }

    public static Double[][] extendShortestPaths(Double[][] L, Double[][] W) {
        Double inf = Double.POSITIVE_INFINITY;
        int n = L.length;
        Double[][] Lx = new Double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                Lx[i][j] = inf;
                for (int k = 0; k < n; k++) {
                    Lx[i][j] = Math.min(Lx[i][j], L[i][k] + W[k][j]);
                }
            }
        }
        return Lx;
    }

    public static void printMatrix(Double[][] matrix, String name) {
        System.out.println("------------------------------------" + name +
                           "------------------------------------");
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j].equals(Double.POSITIVE_INFINITY)) {
                    System.out.print("       inf");
                } else {
                    System.out.format("%10.0f", matrix[i][j]);
                }
            }
            System.out.println();
        }
    }

    public static Double[][] slowAllPairsShortestPaths(Double[][] W) {
        printMatrix(W, "W");
        int n = W.length;
        Double[][] L1, LPrev;
        L1 = LPrev = W;
        printMatrix(L1, "L(1)");
        Double[][] Lm = new Double[n][n];
        for (int m = 1; m < n-1; m++, LPrev = Lm) {
            Lm = extendShortestPaths(LPrev, W);
            printMatrix(Lm, "L(" + (m + 1) + ")");
        }
        return Lm;
    }

    public static Double[][] fasterAllPairsShortestPaths(Double[][] W) {
        printMatrix(W, "W");
        int n = W.length;
        Double[][] Lm = W;
        Double[][] L2m;
        printMatrix(Lm, "L(1)");
        int m = 1;
        while (m < n-1) {
            L2m = new Double[n][n];
            L2m = extendShortestPaths(Lm, Lm);
            m *= 2;
            printMatrix(L2m, "L(" + m + ")");
            Lm = L2m;
        }
        return Lm;
    }

    public static Double[][] computeW2(Double[][] W) {
        Double[][] W2 = extendShortestPaths(W, W);
        printMatrix(W2, "W^2");
        return W2;
    }

    public static Double[][] computeW3(Double[][] W, Double[][] W2) {
        Double[][] W3 = extendShortestPaths(W, W2);
        printMatrix(W3, "W^3");
        return W3;
    }

    public static Double[][] computeW6(Double[][] W3) {
        Double[][] W6 = extendShortestPaths(W3, W3);
        printMatrix(W6, "W^6");
        return W6;
    }
}

/* OUTPUT
------------------------------------W------------------------------------
         0        -6       inf         1       inf       inf
        11         0        -4       inf       inf       inf
       inf       inf         0       inf       inf        20
       inf       inf       -11         0         2       inf
       inf         3       inf        -1         0         7
         5       inf       inf       inf        -3         0
------------------------------------L(1)------------------------------------
         0        -6       inf         1       inf       inf
        11         0        -4       inf       inf       inf
       inf       inf         0       inf       inf        20
       inf       inf       -11         0         2       inf
       inf         3       inf        -1         0         7
         5       inf       inf       inf        -3         0
------------------------------------L(2)------------------------------------
         0        -6       -10         1         3       inf
        11         0        -4        12       inf        16
        25       inf         0       inf        17        20
       inf         5       -11         0         2         9
        12         3       -12        -1         0         7
         5        -1       inf        -4        -3         0
------------------------------------L(3)------------------------------------
         0        -6       -10         1         3        10
        11         0        -4        12        13        16
        25        19         0        16        17        20
        14         5       -11         0         2         9
        12         3       -12        -1         0         7
         5        -1       -15        -4        -3         0
------------------------------------L(4)------------------------------------
         0        -6       -10         1         3        10
        11         0        -4        12        13        16
        25        19         0        16        17        20
        14         5       -11         0         2         9
        12         3       -12        -1         0         7
         5        -1       -15        -4        -3         0
------------------------------------L(5)------------------------------------
         0        -6       -10         1         3        10
        11         0        -4        12        13        16
        25        19         0        16        17        20
        14         5       -11         0         2         9
        12         3       -12        -1         0         7
         5        -1       -15        -4        -3         0
------------------------------------W------------------------------------
         0        -6       inf         1       inf       inf
        11         0        -4       inf       inf       inf
       inf       inf         0       inf       inf        20
       inf       inf       -11         0         2       inf
       inf         3       inf        -1         0         7
         5       inf       inf       inf        -3         0
------------------------------------L(1)------------------------------------
         0        -6       inf         1       inf       inf
        11         0        -4       inf       inf       inf
       inf       inf         0       inf       inf        20
       inf       inf       -11         0         2       inf
       inf         3       inf        -1         0         7
         5       inf       inf       inf        -3         0
------------------------------------L(2)------------------------------------
         0        -6       -10         1         3       inf
        11         0        -4        12       inf        16
        25       inf         0       inf        17        20
       inf         5       -11         0         2         9
        12         3       -12        -1         0         7
         5        -1       inf        -4        -3         0
------------------------------------L(4)------------------------------------
         0        -6       -10         1         3        10
        11         0        -4        12        13        16
        25        19         0        16        17        20
        14         5       -11         0         2         9
        12         3       -12        -1         0         7
         5        -1       -15        -4        -3         0
------------------------------------L(8)------------------------------------
         0        -6       -10         1         3        10
        11         0        -4        12        13        16
        25        19         0        16        17        20
        14         5       -11         0         2         9
        12         3       -12        -1         0         7
         5        -1       -15        -4        -3         0
------------------------------------W^2------------------------------------
         0        -6       -10         1         3       inf
        11         0        -4        12       inf        16
        25       inf         0       inf        17        20
       inf         5       -11         0         2         9
        12         3       -12        -1         0         7
         5        -1       inf        -4        -3         0
------------------------------------W^3------------------------------------
         0        -6       -10         1         3        10
        11         0        -4        12        13        16
        25        19         0        16        17        20
        14         5       -11         0         2         9
        12         3       -12        -1         0         7
         5        -1       -15        -4        -3         0
------------------------------------W^6------------------------------------
         0        -6       -10         1         3        10
        11         0        -4        12        13        16
        25        19         0        16        17        20
        14         5       -11         0         2         9
        12         3       -12        -1         0         7
         5        -1       -15        -4        -3         0

Process finished with exit code 0
*/