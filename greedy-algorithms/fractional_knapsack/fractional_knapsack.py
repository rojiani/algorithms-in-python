"""
FRACTIONAL KNAPSACK PROBLEM - GREEDY ALGORITHM
# v_i: value ($) of item i
# w_i: weight (lbs) of item i
# u_i: density (value per unit weight) of item i. u = v/w
# x_i: fraction of item selected and put into knapsack
# W: Maximum knapsack weight
# Maximize value by taking fractions of items so that knapsack weighs < W
"""

v_i = 1
w_i = 2
u_i = 3
x_i = 4
name = 5   # item name

def fractional_knapsack():


    # Set 1
    v1 = [ 4, 2, 2, 1, 10]
    w1 = [12, 1, 2, 1,  4]
    max_weight_1 = 15.0
    print("Set 1:")
    print_knapsack(fractional_knapsack_selector(v1, w1, max_weight_1))

    # Set 2
    names2 = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    v2 =     [175,      90,         20,     50,     10,     200]
    w2 =     [10,       9,          4,      2,      1,      20]
    max_weight_2 = 20.0
    print("Set 2:")
    print_knapsack_w_names(fknap_selector_with_names(v2, w2, names2, max_weight_2))


def fractional_knapsack_selector(v, w, W):
    # Items represented in list as sublist [i, v_i, w_i, u_i, x_i] 
    items = [[-1, 0.0, 0.0, 0.0, 0.0]] * len(w)
    for i in range(len(v)):
        items[i] = [i, float(v[i]), float(w[i]), density(v[i], w[i]), 0.0]
    # Sort by decreasing density
    items = sorted(items, key=density_key_fn, reverse=True)
    load = 0.0      # knapsack weight
    for i in range(len(items)):
        remaining_wt = W - load
        item_wt = items[i][w_i]
        if load < W:
            if items[i][w_i] <= remaining_wt:
                load += item_wt
                items[i][x_i] = 1.0
            else:
                part = remaining_wt / item_wt
                items[i][x_i] = part
                load += item_wt * part
        else:
            return items
    return items

# def fknap_selector_with_names(v, w, names, W):
#     # Items represented in list as sublist [i, v_i, w_i, u_i, x_i, name] 
#     items = [[-1, 0.0, 0.0, 0.0, 0.0]] * len(w)
#     for i in range(len(v)):
#         items[i] = [i, float(v[i]), float(w[i]), density(v[i], w[i]), 0.0, names[i]]
#     # Sort by decreasing density
#     items = sorted(items, key=density_key_fn, reverse=True)
#     load = 0.0      # knapsack weight
#     for i in range(len(items)):
#         remaining_wt = (W - load)
#         item_wt = items[i][w_i]
#         if load < W:
#             if items[i][w_i] <= remaining_wt:
#                 load += item_wt
#                 items[i][x_i] = 1.0
#             else:
#                 part = remaining_wt / item_wt
#                 items[i][x_i] = part
#                 load += item_wt * part
#         else:
#             return items
#     return items

def fknap_selector_with_names(v, w, names, W):
    # Items represented in list as sublist [i, v_i, w_i, u_i, x_i, name] 
    items = [[-1, 0.0, 0.0, 0.0, 0.0]] * len(w)
    for i in range(len(v)):
        items[i] = [i, float(v[i]), float(w[i]), density(v[i], w[i]), 0.0, names[i]]
    # Sort by decreasing density
    items = sorted(items, key=density_key_fn, reverse=True)
    load = 0.0      # knapsack weight
    for i in range(len(items)):
        remaining_wt = (W - load)
        item_wt = items[i][w_i]
        if load == W:
            items[i][x_i] = 0.0
        else:
            if W -load >= items[i][w_i]:
                items[i][x_i] = 1.0
            else:
                items[i][x_i] = ((W - load) / items[i][w_i])
        load += items[i][x_i] * items[i][w_i]
    return items

def print_knapsack(items):
    total_val = total_weight = 0.0    
    #items = sorted(items, key=lambda x: x[0])
    for i in range(len(items)):
        if items[i][x_i] > 0.0:
            print("Item %d:" % i)
            print("     Fraction taken    =  %.4f" % (items[i][x_i]))
            print("     Value added       =  (%.2f)(%.2f) = %.2f" % (items[i][x_i], items[i][v_i], (items[i][x_i] * items[i][v_i])))
            print("     Weight added      =  (%.2f)" % (items[i][w_i] * items[i][x_i]))
            print("     Density           =  %.2f" % items[i][u_i])
            total_weight += items[i][w_i] * items[i][x_i]            
            total_val += (items[i][x_i] * items[i][v_i])
            print("     Cumulative Value  =  %.2f" % total_val)
            print("     Cumulative Weight =  %.2f" % (total_weight))            
    print("\nTotal Value: %.2f\n\n" % total_val)

def print_knapsack_w_names(items):
    total_val = total_weight = 0.0    
    #items = sorted(items, key=lambda x: x[0])
    for i in range(len(items)):
        if items[i][x_i] > 0.0:
            print("Item %d: %s" % (i, items[i][name]))
            print("     Fraction taken    = %.4f" % (items[i][x_i]))
            print("     Value added       = (%.2f)(%.2f) = %.2f" % (items[i][x_i], items[i][v_i], (items[i][x_i] * items[i][v_i])))
            print("     Weight added      = (%.2f)" % (items[i][w_i] * items[i][x_i]))
            print("     Density           = %.2f" % items[i][u_i])
            total_weight += items[i][w_i] * items[i][x_i]            
            total_val += (items[i][x_i] * items[i][v_i])
            print("     Cumulative Value  = %.2f" % total_val)
            print("     Cumulative Weight = %.2f" % (total_weight))            
    print("\nTotal Value: %.2f\n\n" % total_val)

# Calculate density (u = v/w) for item
# items represented as tuples in list as: (i, v_i, w_i, u_i, x_i)
def density(v, w): return v / w
def density_key_fn(item): return item[v_i] / item[w_i]





fractional_knapsack()


"""
Output

Set 1:
Item 0:
     Fraction taken    =  1.0000
     Value added       =  (1.00)(10.00) = 10.00
     Weight added      =  (4.00)
     Density           =  2.50
     Cumulative Value  =  10.00
     Cumulative Weight =  4.00
Item 1:
     Fraction taken    =  1.0000
     Value added       =  (1.00)(2.00) = 2.00
     Weight added      =  (1.00)
     Density           =  2.00
     Cumulative Value  =  12.00
     Cumulative Weight =  5.00
Item 2:
     Fraction taken    =  1.0000
     Value added       =  (1.00)(2.00) = 2.00
     Weight added      =  (2.00)
     Density           =  1.00
     Cumulative Value  =  14.00
     Cumulative Weight =  7.00
Item 3:
     Fraction taken    =  1.0000
     Value added       =  (1.00)(1.00) = 1.00
     Weight added      =  (1.00)
     Density           =  1.00
     Cumulative Value  =  15.00
     Cumulative Weight =  8.00
Item 4:
     Fraction taken    =  0.5833
     Value added       =  (0.58)(4.00) = 2.33
     Weight added      =  (7.00)
     Density           =  0.33
     Cumulative Value  =  17.33
     Cumulative Weight =  15.00

Total Value: 17.33


Set 2:
Item 0: vase
     Fraction taken    = 1.0000
     Value added       = (1.00)(50.00) = 50.00
     Weight added      = (2.00)
     Density           = 25.00
     Cumulative Value  = 50.00
     Cumulative Weight = 2.00
Item 1: clock
     Fraction taken    = 1.0000
     Value added       = (1.00)(175.00) = 175.00
     Weight added      = (10.00)
     Density           = 17.50
     Cumulative Value  = 225.00
     Cumulative Weight = 12.00
Item 2: painting
     Fraction taken    = 0.8889
     Value added       = (0.89)(90.00) = 80.00
     Weight added      = (8.00)
     Density           = 10.00
     Cumulative Value  = 305.00
     Cumulative Weight = 20.00

Total Value: 305.00


"""