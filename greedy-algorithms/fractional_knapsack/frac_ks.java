/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package knapsack;

/**
 *
 * @author ACHCHUTHAN
 */
public class GreedyKnapsack  {

    double[] profit;
    double[] weight;
    double[] take;

    public GreedyKnapsack(int n) {

        profit = new double[n];
        weight = new double[n];
        take = new double[n];
        for (int i = 0; i < n; i++) {
            profit[i] = (int) Math.round(Math.random() * 96 + 44);
            weight[i] = (int) Math.round(Math.random() * 89 + 15);
        }
    }

    public void unitPriceOrder() {
        for (int i = 0; i < profit.length; i++) {
            for (int j = 1; j < (profit.length - i); j++) {
                double x=profit[j - 1] / weight[j - 1];
                double y=profit[j] / weight[j];
                if (x <=y) {
                    double temp = profit[j - 1];
                    profit[j - 1] = profit[j];
                    profit[j] = temp;

                    double temp1 = weight[j - 1];
                    weight[j - 1] = weight[j];
                    weight[j] = temp1;
                }
            }
        }
    }

    public void Knapsack(int m) {
        unitPriceOrder();
        int j;
        for (j = 0; j < profit.length; j++) {
            take[j] = 0;
        }
        double total = m;
        for (j = 0; j < profit.length; j++) {
            if (weight[j] <= total) {
                take[j] = 1.00;
                total = total - weight[j];
            } else {
                break;// to exit the for-loop
            }
        }
        if (j < profit.length) {
            take[j] = (double)(total / weight[j]);
        }       
    }

    public void print() {

        System.out.println("item" + " |  " + "profit" + "  |   " + "weight" +
                "   |     " + "Unit Price" + "      |" + "  Take weight");
        for (int n = 0; n < profit.length; n++) {
            System.out.println(n + "\t" + profit[n] + "\t" + weight[n] + "\t"
                    + (profit[n] / weight[n]) + "\t" + take[n]);
        }
    }

    public static void main(String args[]) {
        GreedyKnapsack G = new GreedyKnapsack(10);
        System.out.println("Optimal soluation to knapsack instance "
                + "with values given as follows : m=35");
        G.Knapsack(35);
        G.print();
        System.out.println("=======+============+=======+============+="
                + "===========");
        System.out.println("Optimal soluation to knapsack instance with "
                + "values given as follows : m=120");
        G.Knapsack(120);
        G.print();
    }
}
