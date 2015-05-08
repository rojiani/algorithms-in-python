# FRACTIONAL KNAPSACK PROBLEM - GREEDY
# v_i: value ($) of item i
# w_i: weight (lbs) of item i
# u_i = (v_i/w_i) = value/weight
# Assume sorted by decreasing u
# Maximize $, max weight MAX_WEIGHT

def driver():
    # n = 5
    # v = [4, 2, 2, 1, 10]
    # w = [12, 1, 2, 1, 4]
    # items: (v, w, u)
    items = [(4.0, 12.0, 0.33), (2.0, 1.0, 2.0), (2.0, 2.0, 1.0), (1.0, 1.0, 1.0), (10.0, 4.0, 2.5)]
    MAX_WEIGHT = 15.0
    value = fractional_knapsack(items, MAX_WEIGHT)
    print("Solution: " + str(items))
    print("Value = $%.2f" % (value))

    v2 =     [175,      90,         20,     50,     10,     200]
    w2 =     [10,       9,          4,      2,      1,      20]
    items2 = []
    for i in range(len(v2)):
        items2.append((v2[i], w2[i], v2[i]/w2[i]))
    MAX_WEIGHT_2 = 20.0
    value2 = fractional_knapsack(items2, MAX_WEIGHT_2)
    print("Solution: " + str(items2))
    print("Value = $%.2f" % (value2))

def fractional_knapsack(items, wmax):
    knapsack = []
    load = 0.0
    value = 0.0
    # Sort items by cost/weight ratio in decreasing order
    items.sort(key=lambda x: x[2], reverse=True)
    print("Sorted items: " + str(items))
    
    for i in items:
        print("-----------")
        print("load: %.2f" % (load))
        print("value: $%.2f" % (value))
        print("Remaining Capacity: %.2f" % (wmax - load))

        # if weight <= max, add all of it
        if load < wmax:
            print("load < wmax")
            if i[1] <= (wmax - load):
                value += i[0]
                load += i[1]
                print("Adding $%.2f from %.2f lbs" % (i[0], i[1]))
            else:
                print("Adding part")
                part = (wmax - load) / i[1]
                print("part = %.2f" % (part))
                print("partial value = %.2f" % (part * i[0]))
                print("partial load = %.2f" % (part * i[1]))

                value += part * i[0]
                print("value = %.2f" % (value))
                load += part * i[1]
                print("load = %.2f" % (load))
                return value
        else:
            return value

driver()