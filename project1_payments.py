# Narrative: The borrower has a monthly budget for loan payments. Compare the calculated 
# payment to that budget and report whether it is below, exactly at, or over. 
# Both values must be nonnegative, and the comparison happens in whole cents 
# so floating-point noise doesn’t cause a wrong answer.

""" Classify a monthly loan payment against a monthly budget.

    Args:
        payment (float): Monthly loan payment, in dollars. Must be >= 0.
        budget (float): Monthly budget, in dollars. Must be >= 0.

    Returns:
        str: Exactly one of "Below budget", "Exactly at budget",
            or "Over budget".

    Raises:
        ValueError: If payment or budget is negative.

    Boundary rules:
        - Both values are rounded to 2 decimals before comparing.
        - payment == budget (after rounding) is "Exactly at budget".
        - 0 is valid for both values; (0, 0) is "Exactly at budget".
    """


def budget_status(payment, budget):
    """Compare a loan payment to a monthly budget and return a message."""
    if payment < 0 or budget < 0:
        raise ValueError("Payment and budget must be nonnegative.")

    # Round to cents so floating-point error doesn't break the equality check
    payment = round(payment, 2)
    budget = round(budget, 2)

    if payment < budget:
        return "Below budget"
    elif payment == budget:
        return "Exactly at budget"
    else:
        return "Over budget"

print (budget_status(200, 250))
