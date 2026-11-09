# ---------------------------------------------------------------------------
# HW09 PART B: SAVINGS DEPOSIT
#
# NARRATIVE PARSED
#   A saver starts with no money, wants to reach a savings goal, and makes
#   equal deposits at the end of each month for a whole number of years.
#
# DATA NOUNS
#   savings_goal          dollars wanted at the end of the term (positive)
#   annual_rate_percent   nominal annual rate as a percentage (positive)
#   years                 term in whole years (positive)
#   monthly_rate          monthly interest rate as a decimal
#   periods               number of monthly deposits
#   deposit               equal monthly deposit in dollars
#
# ACTION VERBS
#   convert    annual percentage -> monthly decimal rate
#   count      years -> monthly periods
#   calculate  the monthly deposit that builds the goal
#   request    (input) the three values from the saver
#   display    the deposit in dollars and cents
#
# STRUCTURED ENGLISH
#
#   HELPERS (copied unchanged from the loan program)
#     monthly_interest_rate(annual_rate_percent)
#         divide annual_rate_percent by 100 to get a decimal
#         divide that decimal by 12
#         RETURN the monthly rate
#
#     payment_periods(years)
#         multiply years by 12
#         RETURN the number of periods
#
#   DEPOSIT CALCULATION
#     monthly_savings_payment(savings_goal, annual_rate_percent, years)
#         obtain the monthly rate from monthly_interest_rate
#         obtain the number of periods from payment_periods
#         compute deposit = savings_goal * rate / ((1 + rate) ** periods - 1)
#         RETURN the deposit (unrounded)
#
#   INPUT AND DISPLAY (calling code)
#     main()
#         REQUEST savings_goal
#         REQUEST annual_rate_percent
#         REQUEST years
#         CALL monthly_savings_payment with those three values
#         DISPLAY the deposit as dollars and cents
#
# ASSUMPTIONS
#   Positive inputs, fixed nominal annual rate, monthly compounding,
#   deposits at the end of each month, zero starting balance, no fees and
#   no withdrawals. No input validation.
#
# HOW THIS DIFFERS FROM THE LOAN CALCULATION
#   Loan:    payment = loan_amount * r / (1 - (1 + r) ** -n)
#            The money exists now and is repaid over time, so the formula
#            discounts the payments back to today's balance (present value).
#   Savings: deposit = savings_goal * r / ((1 + r) ** n - 1)
#            The money does not exist yet and is built over time, so the
#            formula grows the deposits forward to the goal (future value).
#   The helpers stay the same because the units and the time conversion
#   (percent to monthly decimal, years to months) are the same. Only the
#   main calculation changes because the question changes.
#
# PROMPT MODEL (for asking an AI assistant to implement the function)
#   "Implement monthly_savings_payment from my docstring using the existing
#   helpers and the supplied savings formula. Assume zero starting balance
#   and deposits at month end. Return an unrounded number. Keep input and
#   printing outside the function. Explain how this calculation differs from
#   the loan calculation."
# ---------------------------------------------------------------------------


def monthly_interest_rate(annual_rate_percent):
    return annual_rate_percent / 100 / 12


def payment_periods(years):
    return years * 12


def monthly_savings_payment(savings_goal, annual_rate_percent, years):
    """Return the equal monthly deposit needed to reach a savings goal.

    Parameters:
        savings_goal: dollars wanted at the end of the term (positive number).
        annual_rate_percent: nominal annual interest rate as a percentage,
            for example 6 for 6% (positive number).
        years: term in whole years (positive integer).

    Returns:
        The monthly deposit in dollars as an unrounded float. Rounding to
        dollars and cents is left to the calling code.

    Assumptions:
        Zero starting balance, deposits at the end of each month, a fixed
        nominal annual rate compounded monthly, and no fees or withdrawals.

    Calculation:
        deposit = G * r / ((1 + r) ** n - 1), where G is the savings goal,
        r is the monthly decimal rate from monthly_interest_rate, and n is
        the number of monthly periods from payment_periods.
    """
  
    rate = monthly_interest_rate(annual_rate_percent)
    periods = payment_periods(years)
    return savings_goal * rate / ((1 + rate) ** periods - 1)


def main():
    savings_goal = float(input("Savings goal ($): "))
    annual_rate_percent = float(input("Annual interest rate (%): "))
    years = int(input("Term (years): "))

    deposit = monthly_savings_payment(savings_goal, annual_rate_percent, years)
    print(f"Monthly deposit: ${deposit:,.2f}")

main()
