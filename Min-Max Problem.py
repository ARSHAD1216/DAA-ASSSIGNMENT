def find_max_min(arr, low, high):
    # Base case: If the array has only one element
    if low == high:
        return arr[low], arr[low]
    
    # Base case: If the array has two elements
    elif high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Recursive case: Divide the array into two halves
    else:
        mid = (low + high) // 2
        
        min1, max1 = find_max_min(arr, low, mid)
        min2, max2 = find_max_min(arr, mid + 1, high)

        # Combine step: Return the minimum and maximum of both halves
        return min(min1, min2), max(max1, max2)

# Driver code to test the function
arr = [12, 11, 45, 7, 56, 98, 3, 22]
low = 0
high = len(arr) - 1
minimum, maximum = find_max_min(arr, low, high)

print(f"Minimum element is {minimum}")
print(f"Maximum element is {maximum}")
