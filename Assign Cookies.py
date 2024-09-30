def find_content_children(g, s):
    # Sort both greed factors and cookie sizes
    g.sort()
    s.sort()

    child_i = 0  # Pointer for children
    cookie_i = 0  # Pointer for cookies
    satisfied_children = 0

    # Assign cookies to children greedily
    while child_i < len(g) and cookie_i < len(s):
        if s[cookie_i] >= g[child_i]:  # If the cookie can satisfy the child
            satisfied_children += 1
            child_i += 1  # Move to the next child
        cookie_i += 1  # Move to the next cookie

    return satisfied_children

# Driver code to test the function
g = [1, 2, 3]  # Greed factors of children
s = [1, 1]  # Sizes of cookies

# Function call
result = find_content_children(g, s)
print(f"Maximum number of children that can be satisfied: {result}")
