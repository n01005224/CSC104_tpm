def monthly_interest_rate(annual_rate_percent):
    """Convert an annual rate in percent (e.g. 6.5) to a monthly decimal rate."""
    return annual_rate_percent / 100 / 12


def payment_periods(years):
    """Return the number of monthly payment periods for a term in years."""
    return years * 12


def monthly_payment(loan_amount, annual_rate_percent, years):
    """Return the monthly payment needed to fully repay a loan."""
    r = monthly_interest_rate(annual_rate_percent)
    n = payment_periods(years)

    if r == 0:
        return loan_amount / n

    return loan_amount * r / (1 - (1 + r) ** -n)
    
