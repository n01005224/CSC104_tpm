""" Narrative: A borrower provides a loan term in whole years and an annual interest rate written as a percentage.
Create one function that converts the years into the number of monthly payment periods. Create a second
function that converts the annual percentage into a monthly decimal interest rate. Each function must return its
result so another function can use it."""

def payment_periods(years):
    """Return the number of monthly payment periods for a term in years."""
    return years * 12
def monthly_interest_rate(annual_rate_percent): 
  """Convert an annual rate in percent (e.g. 6.5) to a monthly decimal rate."""
  return annual_rate_percent / 100 / 12

print("1 year   | expected: 12  | actual:", payment_periods(1))
print("5 years  | expected: 60  | actual:", payment_periods(5))
print("10 years | expected: 120 | actual:", payment_periods(10))
print("6% interest | expected: 0.005 | actual:", monthly_interest_rate(6))
print("12% interest | expected: 0.01 | actual:", monthly_interest_rate(12))
print("3% interest | expected: 0.0025 | actual:", monthly_interest_rate(3))

# ---------------------------------------------------------------------------
# Q1. Why is 0.005 the monthly rate for 6% annually?
#
# A percent is "per hundred", so 6% becomes the decimal 6 / 100 = 0.06.
# Loans charge interest monthly, and a year has 12 months, so the quoted
# annual rate is divided by 12: 0.06 / 12 = 0.005 (that is, 0.5% per month).
# This is the nominal (APR) convention that lenders use. It is not the rate
# that compounds to exactly 6% over a year; that would be about 0.004868.
#
# Q2. Parameter vs. argument in payment_periods(5)?
#
# A parameter is the variable name in the function definition. In
# "def payment_periods(years):" the parameter is "years". It is a placeholder
# for whatever value the caller supplies.
# An argument is the actual value passed in a call. In "payment_periods(5)"
# the argument is 5. When the call runs, the argument 5 is assigned to the
# parameter "years", so years == 5 inside the function.
#
# Q3. Why must these helpers return rather than only print?
#
# print() shows text on the screen but hands nothing back; the call
# evaluates to None. monthly_payment() needs the numbers r and n to do
# arithmetic, so the helpers must return them. Returning also keeps
# calculation separate from display: main() decides how to show the result
# (dollars and cents), and the same functions can be reused in a schedule,
# a test, or a web page without any unwanted output.
# ---------------------------------------------------------------------------
 

