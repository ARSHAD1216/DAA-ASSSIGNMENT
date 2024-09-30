# Class to store an item with its value and weight
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Function to calculate maximum value we can get
def fractional_knapsack(W, arr):
    # Sorting items by value/weight ratio in decreasing order
    arr.sort(key=lambda x: (x.value / x.weight), reverse=True)
    
    total_value = 0.0  # Result (maximum value)

    # Loop through all items
    for item in arr:
        # If adding the whole item doesn't exceed the capacity, add it
        if item.weight <= W:
            W -= item.weight
            total_value += item.value
        # If we can't add the whole item, add the fractional part of it
        else:
            total_value += item.value * (W / item.weight)
            break
    
    return total_value

# Driver code to test the function
if __name__ == "__main__":
    # List of items (value, weight)
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    
    # Capacity of the knapsack
    W = 50
    
    # Function call
    max_value = fractional_knapsack(W, arr)
    
    print(f"Maximum value we can obtain = {max_value}")
