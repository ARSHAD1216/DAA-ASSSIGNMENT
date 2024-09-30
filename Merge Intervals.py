def merge(intervals):
    if not intervals:
        return []

    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If merged is empty or there is no overlap with the last interval in merged, append it
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # If there is an overlap, merge the intervals by updating the end time
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Driver code to test the function
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# Function call
result = merge(intervals)
print(f"Merged intervals: {result}")
