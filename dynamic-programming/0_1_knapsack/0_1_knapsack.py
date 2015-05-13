

class Item(object):
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    def get_name(self):   return self.name
    def get_value(self):  return self.value 
    def get_weight(self):  return self.weight 

    def __str__(self):
        return '[Item %s: value = %.2f, weight = %.2f]' \
                  % (self.name, self.value, self.weight)

class KSDecision(object):
    def __init__(self, taken, undecided, total_value, rem_capac):
        self.taken = taken
        self.undecided = undecided
        self.total_value = total_value
        self.capacity = rem_capac

    def get_taken_items(self):
        return list(self.taken)
    def get_undecided_items(self):
        return list(self.undecided)
    def get_total_value(self):
        return self.total_value
    def get_capacity(self):
        return self.capacity

    def take_item(self):
        item = self.undecided[0]
        self.taken.append(item)
        self.undecided = self.undecided[1:]
        self.total_value += item.get_value()
        self.capacity -= item.get_weight()
    def deciding_completed(self):
        return len(self.undecided) == 0
    def overloaded(self):
        return self.capacity < 0
    def filled(self):
        return self.capacity == 0


def recursive_01_knapsack(items, max_weight):
    ksd = KSDecision(list([]), items, 0, max_weight)
    result = decide(ksd)
    ks = result.get_taken_items()
    # print(ks)
    print("Items in knapsack:")
    for item in ks:
         print(item)

    print("Total Value: %.2f" % result.get_total_value())
    print("Total Weight: %.2f" % (max_weight - result.get_capacity()))



def decide(ksd):
    taken = ksd.get_taken_items()

    undecided = ksd.get_undecided_items()
    total_value = ksd.get_total_value()
    rem_capac = ksd.get_capacity()

    if ksd.overloaded() or ksd.filled() or ksd.deciding_completed():
        return ksd
    else:
        skip_ksd = KSDecision(taken, undecided[1:], total_value, rem_capac)
        skip = decide(skip_ksd)

        take_ksd = ksd 
        take_ksd.take_item()
        take = decide(take_ksd)

        if take.overloaded() and skip.overloaded():
            return take
        elif take.overloaded() and not skip.overloaded():
            return skip
        elif not take.overloaded() and skip.overloaded():
            return take
        else:
            if take.get_total_value() >= skip.get_total_value():
                return take
            else:
                return skip

def demo_01_knapsack():
    items = [Item('a', 6, 3), \
             Item('b', 7, 3), \
             Item('c', 8, 2), \
             Item('d', 9, 5)]
    recursive_01_knapsack(items, 5)
    # Correct output


    items2 = [Item("map", 9, 150), \
              Item("compass", 13, 35), \
              Item("water", 153, 200), \
              Item("sandwich", 50, 160), \
              Item("glucose", 15, 60), \
              Item("tin", 68, 45), \
              Item("banana", 27, 60), \
              Item("apple", 39, 40), \
              Item("cheese", 23, 30), \
              Item("beer", 52, 10), \
              Item("suntan cream", 11, 70), \
              Item("camera", 32, 30), \
              Item("t-shirt", 24, 15), \
              Item("trousers", 48, 10), 
              Item("umbrella", 73, 40), \
              Item("waterproof trousers", 42, 70), \
              Item("waterproof overclothes", 43, 75), \
              Item("note-case", 22, 80), \
              Item("sunglasses", 7, 20), \
              Item("towel", 18, 12), \
              Item("socks", 4, 50), \
              Item("book", 30, 10)]
    recursive_01_knapsack(items2, 400)
    # Incorrect output

demo_01_knapsack()