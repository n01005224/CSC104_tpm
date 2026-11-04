def payment_periods(years):
    """Return the number of monthly payment periods for a term in years."""
    return years * 12
def monthly_interest_rate(annual_rate_percent): 
  """Convert an annual rate in percent (e.g. 6.5) to a monthly decimal rate."""
  return annual_rate_percent / 100 / 12

