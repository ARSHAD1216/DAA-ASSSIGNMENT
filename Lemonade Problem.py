def lemonade_change(bills):
    five_count = 0  # Count of $5 bills
    ten_count = 0   # Count of $10 bills

    for bill in bills:
        if bill == 5:
            five_count += 1  # No change needed, just take the $5 bill
        elif bill == 10:
            if five_count == 0:  # Can't give $5 as change
                return False
            five_count -= 1
            ten_count += 1
        elif bill == 20:
            if ten_count > 0 and five_count > 0:  # Give $10 and $5 as change
                ten_count -= 1
                five_count -= 1
            elif five_count >= 3:  # Otherwise, give three $5 bills as change
                five_count -= 3
            else:  # Can't give the correct change
                return False

    return True

# Driver code to test the function
bills = [5, 5, 5, 10, 20]  # Example input
result = lemonade_change(bills)
print(f"Can provide change for all customers: {result}")