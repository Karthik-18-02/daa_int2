class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(W, arr):
    arr.sort(key=lambda x: (x.value/x.weight), reverse=True)
    final_val = 0.0

    for i in arr:
        if i.weight <= W:
            W -= i.weight
            final_val += i.value
        else:
            final_val += i.value * W / i.weight

    return final_val

W = 50
arr = [Item(60, 10), Item(100, 30), Item(140, 30)]
print(fractional_knapsack(W, arr))
