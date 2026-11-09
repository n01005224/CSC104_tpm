# ---------------------------------------------------------------------------
# DATA NOUNS
#   loan_amount           dollars borrowed (positive)
#   annual_rate_percent   nominal annual rate as a percentage (positive)
#   years                 term in whole years (positive)
#   monthly_rate          monthly interest rate as a decimal
#   periods               number of monthly payments
#   payment               monthly payment in dollars
#
# ACTION VERBS
#   convert   annual percentage -> monthly decimal rate
#   count     years -> monthly periods
#   calculate the monthly payment
#   request   (input) the three values from the borrower
#   display   the payment in dollars and cents
#
#
#   HELPERS
#     monthly_interest_rate(annual_rate_percent)
#         divide annual_rate_percent by 100 to get a decimal
#         divide that decimal by 12
#         RETURN the monthly rate
#
#     payment_periods(years)
#         multiply years by 12
#         RETURN the number of periods
#
#   PAYMENT CALCULATION
#     monthly_payment(loan_amount, annual_rate_percent, years)
#         obtain the monthly rate from monthly_interest_rate
#         obtain the number of periods from payment_periods
#         compute payment = loan_amount * rate / (1 - (1 + rate) ** -periods)
#         RETURN the payment
#
#   INPUT AND DISPLAY (calling code)
#         REQUEST loan_amount
#         REQUEST annual_rate_percent
#         REQUEST years
#         CALL monthly_payment with those three values
#         DISPLAY the payment as dollars and cents
#
# ---------------------------------------------------------------------------


def monthly_interest_rate(annual_rate_percent):
    return annual_rate_percent / 100 / 12


def payment_periods(years):
    return years * 12


def monthly_loan_payment(loan_amount, annual_rate_percent, years):
    rate = monthly_interest_rate(annual_rate_percent)
    periods = payment_periods(years)
    return loan_amount * rate / (1 - (1 + rate) ** -periods)



loan_amount = float(input("Loan amount ($): "))
annual_rate_percent = float(input("Annual interest rate (%): "))
years = int(input("Term (years): "))

payment = monthly_loan_payment(loan_amount, annual_rate_percent, years)
print(f"Monthly payment: ${payment:,.2f}")


# ---------------------------------------------------------------------------
# TRACE OF THE FIRST CASE (12000, 6, 5)
#
# 1. Input strings
#    The borrower types 12000, 6, and 5. input() returns each one as a
#    string: "12000", "6", "5".
#
# 2. Numeric conversion (in main)
#    loan_amount         = float("12000") -> 12000.0
#    annual_rate_percent = float("6")     -> 6.0
#    years               = int("5")       -> 5
#
# 3. Coordinating function
#    main() calls monthly_payment(12000.0, 6.0, 5). The three values become
#    the parameters loan_amount, annual_rate_percent, and years.
#
# 4. Helper: monthly_interest_rate(6.0)
#    6.0 / 100 = 0.06
#    0.06 / 12 = 0.005
#    Returns 0.005, stored in rate.
#
# 5. Helper: payment_periods(5)
#    5 * 12 = 60
#    Returns 60, stored in periods.
#
# 6. Payment calculation (still inside monthly_payment)
#    (1 + rate) ** -periods = (1.005) ** -60, about 0.741372
#    1 - 0.741372 = about 0.258628
#    numerator: 12000.0 * 0.005 = 60.0
#    payment = 60.0 / 0.258628, about 231.9934
#    The function returns the unrounded float (about 231.9934).
#
# 7. Return to main
#    The returned float is stored in the variable payment.
#
# 8. Print
#    The f-string format spec :,.2f rounds to two decimals and adds a
#    thousands separator (none needed here), so the line printed is:
#    Monthly payment: $231.99
#    Rounding happens only here, at display time. The stored value is not

