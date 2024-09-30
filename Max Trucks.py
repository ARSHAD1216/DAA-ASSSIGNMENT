def maximum_units(boxTypes, truckSize):
    # Sort boxTypes by number of units per box in decreasing order
    boxTypes.sort(key=lambda x: x[1], reverse=True)

    total_units = 0  # To store the total units loaded
    for numberOfBoxes, numberOfUnitsPerBox in boxTypes:
        # If the truck can carry all boxes of this type
        if truckSize >= numberOfBoxes:
            total_units += numberOfBoxes * numberOfUnitsPerBox
            truckSize -= numberOfBoxes
        else:
            # If the truck can only carry some of the boxes, take as many as it can carry
            total_units += truckSize * numberOfUnitsPerBox
            break  # The truck is full

    return total_units

# Driver code to test the function
boxTypes = [[1, 3], [2, 2], [3, 1]]  # [numberOfBoxes, numberOfUnitsPerBox]
truckSize = 4

# Function call
result = maximum_units(boxTypes, truckSize)
print(f"Maximum number of units that can be loaded on the truck: {result}")
