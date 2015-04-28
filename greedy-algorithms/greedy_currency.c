/* 
 * Greedy algorithm which determines the minimum # of coins to give while 
 * making change.
 * http://everythingcomputerscience.com/algorithms/Greedy_Algorithm.html
 * 
 * Candidate Set: {1, 5, 10, 20}
 * Selection function: Choose the largest coin value first (20)
 * Feasability function: Check if the largest coin value can be used for change
 *     amount, if true then remember the coin value & update the change amount.
 * Objective function: Remember the coins being used
 * Solution function: When the change amount reaches 0, we have found our 
 *     solution.
 */

#include <stdio.h>

#define SET_SIZE 4

/* Prints the coins returned. */
void print_coins(int *coin_values, int size)
{
    int amt_remaining;
    int solution[100];
    int coins_returned = 0; // solution idx
    int coin_idx = 0; 

    printf("Input change amount: ");
    scanf("%d", &amt_remaining);

    while (amt_remaining > 0) {
        if (coin_values[coin_idx] <= amt_remaining) {
            amt_remaining -= coin_values[coin_idx];     
            solution[coins_returned++] = coin_values[coin_idx];
        } else if (amt_remaining < 0) {
            printf("No solution. \n");
        } else {
            coin_idx++;
            continue;
        }
    }
    printf("The minimum number of coins is %d\n", coins_returned);
    printf("Solution: ");
    for (int i = 0; i < coins_returned; i++) {
        printf(" %d ", solution[i]);
    }
    printf("\n");
}



/* Selection function - unnecessary, assume coin_values sorted high to low */



/* Driver */
int main(void)
{
    int coin_values[SET_SIZE] = {20, 10, 5, 1};
    int n = sizeof(coin_values)/sizeof(coin_values[0]);
    print_coins(coin_values, n);
}