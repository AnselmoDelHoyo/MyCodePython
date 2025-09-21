def calculate_tax(bill, tax_rate):
    """
    Calculate the total amount including tax.

    Parameters:
    bill (float): The original bill amount.
    tax_rate (float): The tax rate as a decimal (e.g., 0.07 for 7%).

    Returns:
    float: The total amount including tax.
    """
    if bill < 0 or tax_rate < 0:
        raise ValueError("Bill and tax rate must be non-negative.")
    
    return round((bill * tax_rate) / 100.00)

print("Total tax: ", calculate_tax(2050.75, 22))