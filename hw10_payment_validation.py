# ======================================================================
# hw10_payment_validation.py
# Validate inputs before calculating a loan payment or savings deposit.
# ======================================================================
#
# NARRATIVE PARSING
#   Data nouns:
#     amount / goal   dollars borrowed, or dollars to save (must be > 0)
#     annual_rate     yearly interest rate in percent; 6 means 6% (must be > 0)
#     years           term in years (must be > 0 and whole)
#     months          years * 12 (computed only after validation)
#     monthly_rate    annual_rate / 100 / 12
#     payment         monthly loan payment, in dollars
#     deposit         monthly savings deposit, in dollars
#     error message   text naming the first failed check
#   Action verbs:
#     read, convert, check (validate), display an error, skip,
#     calculate, display the result
#
# STRUCTURED ENGLISH (same shape for the loan and savings sections)
#   1. INPUT CONVERSION
#        READ amount (or goal), rate, years as text with input()
#        CONVERT each to float
#   2. VALIDATION (checked in order; only the first failure is reported)
#        IF amount is not positive      -> DISPLAY amount error
#        ELSE IF rate is not positive   -> DISPLAY rate error
#        ELSE IF years not positive/whole -> DISPLAY years error
#        ELSE (all checks passed)       -> go to calculation
#   3. CALCULATION (only in the final ELSE)
#        CONVERT years to int
#        CALL the loan or savings payment function
#   4. DISPLAY
#        DISPLAY the result with two decimal places
#   Invalid path: neither the payment function nor its helpers run.
#
# Assumptions kept from the original formulas: fixed nominal annual rate,
# monthly compounding, month-end payments or deposits, no fees, zero
# starting savings. Zero interest is invalid for these formulas.
#
# COPILOT PROMPTS (replace with the prompts you actually used)
#   is_positive_amount:
#     "Implement is_positive_amount from my header and docstring. Use
#      if/else and return a real Boolean True only when amount is greater
#      than zero. Assume finite numeric input. Do not print, request
#      input, use loops, or raise exceptions. Explain each path."
#   is_positive_rate:
#     "Implement is_positive_rate from my header and docstring. Use
#      if/else and return True only when the annual percentage is above
#      zero. Assume finite numeric input. Do not print, request input,
#      use loops, or raise exceptions. Explain each path."
#   is_valid_years:
#     "Implement is_valid_years from my header and docstring. Use
#      if/elif/else to reject nonpositive years, then fractional years
#      (use years % 1), and return True only when both requirements
#      pass. Assume finite numeric input. Do not print, request input,
#      use loops, or raise exceptions. Explain each path."
#
# NOTE ON CHANGES TO GENERATED CODE (edit to match what really happened)
#   Example: "Copilot returned the strings 'True'/'False' in one
#   validator; I changed them to the Booleans True/False." If you changed
#   nothing, say so.
# ======================================================================


# ---------------- Existing helpers and payment functions ----------------

def payment_periods(years):
    """Return the number of monthly payments for whole-number years."""
    return years * 12


def monthly_interest_rate(rate):
    """Return the monthly rate as a decimal from an annual percent."""
    return rate / 100 / 12


def monthly_loan_payment(amount, rate, years):
    """Return the monthly payment that repays a loan.

    Contract: positive amount and rate; positive whole years.
    The caller enforces this contract.
    """
    r = monthly_interest_rate(rate)
    n = payment_periods(years)
    return amount * r / (1 - (1 + r) ** -n)


def monthly_savings_payment(goal, rate, years):
    """Return the monthly deposit needed to reach a savings goal.

    Contract: positive goal and rate; positive whole years.
    The caller enforces this contract.
    """
    r = monthly_interest_rate(rate)
    n = payment_periods(years)
    return goal * r / ((1 + r) ** n - 1)


# ---------------- New validators ----------------

def is_positive_amount(amount):
    """Return True if a numeric amount is greater than zero."""
    if amount > 0:
        return True
    else:
        return False


def is_positive_rate(annual_rate_percent):
    """Return True if a numeric annual percentage is above zero."""
    if annual_rate_percent > 0:
        return True
    else:
        return False


def is_valid_years(years):
    """Return True if numeric years are positive and whole."""
    if years <= 0:
        return False
    elif years % 1 != 0:
        return False
    else:
        return True


# ---------------- Direct validator tests (ten labeled calls) ----------------
# Why positive 2.5 years still fails: the formulas count payments as
# years * 12 and the contract requires WHOLE years. 2.5 % 1 is 0.5, a
# nonzero remainder, so the value is not whole and is rejected even
# though it is positive.

print("=== Direct validator tests ===")

print("Test 1  is_positive_amount(12000)  expected: True   actual:", is_positive_amount(12000))
print("Test 2  is_positive_amount(0)      expected: False  actual:", is_positive_amount(0))
print("Test 3  is_positive_amount(-100)   expected: False  actual:", is_positive_amount(-100))

print("Test 4  is_positive_rate(6)        expected: True   actual:", is_positive_rate(6))
print("Test 5  is_positive_rate(0)        expected: False  actual:", is_positive_rate(0))
print("Test 6  is_positive_rate(-1)       expected: False  actual:", is_positive_rate(-1))

print("Test 7  is_valid_years(5)          expected: True   actual:", is_valid_years(5))
print("Test 8  is_valid_years(0)          expected: False  actual:", is_valid_years(0))
print("Test 9  is_valid_years(-2)         expected: False  actual:", is_valid_years(-2))
print("Test 10 is_valid_years(2.5)        expected: False  actual:", is_valid_years(2.5))


# ---------------- Protected loan input section ----------------
# Why "else" means "all checks passed": the if/elif chain tests for
# failure using "not". Python runs the first branch whose condition is
# true and skips the rest, so the final else is reached only when no
# validator failed. That makes it the only safe place for the calculation.
#
# Why zero years is unsafe: months would be 0, so (1 + r) ** -0 is 1 and
# the loan denominator 1 - 1 is 0. In the savings formula (1 + r) ** 0 - 1
# is also 0. Both divide by zero.

print()
print("=== Loan calculator ===")
loan_amount = float(input("Loan amount in dollars: "))
loan_rate = float(input("Annual interest rate in percent: "))
loan_years = float(input("Term in whole years: "))

if not is_positive_amount(loan_amount):
    print("Error: the loan amount must be greater than zero.")
elif not is_positive_rate(loan_rate):
    print("Error: the annual interest rate must be greater than zero.")
elif not is_valid_years(loan_years):
    print("Error: the term must be a positive whole number of years.")
else:
    loan_years = int(loan_years)  # convert only after validation succeeds
    payment = monthly_loan_payment(loan_amount, loan_rate, loan_years)
    print(f"Monthly loan payment: ${payment:.2f}")


# ---------------- Protected savings input section ----------------

print()
print("=== Savings calculator ===")
savings_goal = float(input("Savings goal in dollars: "))
savings_rate = float(input("Annual interest rate in percent: "))
savings_years = float(input("Term in whole years: "))

if not is_positive_amount(savings_goal):
    print("Error: the savings goal must be greater than zero.")
elif not is_positive_rate(savings_rate):
    print("Error: the annual interest rate must be greater than zero.")
elif not is_valid_years(savings_years):
    print("Error: the term must be a positive whole number of years.")
else:
    savings_years = int(savings_years)  # convert only after validation
    deposit = monthly_savings_payment(savings_goal, savings_rate, savings_years)
    print(f"Monthly savings deposit: ${deposit:.2f}")
