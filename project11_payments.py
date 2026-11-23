# ======================================================================
# project1_payments.py
# Programming Project 1: Option 1 (Monthly budget check)
#                        Option 8 (Savings deposit check)
# ======================================================================
#
# ---------------------------- OPTION 1 ---------------------------------
# NARRATIVE: A borrower has a calculated monthly loan payment and a
#   monthly budget. Compare them and report whether the payment is below
#   the budget, exactly at the budget, or over it.
# DATA NOUNS: payment (dollars, >= 0), budget (dollars, >= 0), message
# ACTION VERBS: read, convert, validate, round, compare, display
# STRUCTURED ENGLISH:
#   1. INPUT:      READ loan amount, rate, years, budget; CONVERT to float
#   2. VALIDATION: IF amount not positive -> amount error
#                  ELSE IF rate not positive -> rate error
#                  ELSE IF years not positive/whole -> years error
#                  ELSE IF budget not nonnegative -> budget error
#                  ELSE (all passed) -> go to calculation
#   3. CALCULATION: convert years to int; payment = monthly_loan_payment
#                   message = budget_check(payment, budget)
#   4. DISPLAY:    show payment and message
# DECISION LOGIC inside budget_check (if/elif/else):
#   round both to cents
#   IF payment < budget      -> "Below budget"
#   ELIF payment == budget   -> "Exactly at budget"
#   ELSE (payment > budget)  -> "Over budget"
#
# ---------------------------- OPTION 8 ---------------------------------
# NARRATIVE: A saver has a required monthly deposit (from the savings
#   function) and a planned monthly deposit. Report a shortfall, that the
#   plan meets the requirement, or extra savings, with the dollar amount.
# DATA NOUNS: required (dollars, > 0), planned (dollars, >= 0), message
# ACTION VERBS: read, convert, validate, calculate, round, compare, display
# STRUCTURED ENGLISH:
#   1. INPUT:      READ goal, rate, years, planned deposit; CONVERT to float
#   2. VALIDATION: IF goal not positive -> goal error
#                  ELSE IF rate not positive -> rate error
#                  ELSE IF years not positive/whole -> years error
#                  ELSE IF planned not nonnegative -> planned error
#                  ELSE -> go to calculation
#   3. CALCULATION: convert years to int; required = monthly_savings_payment
#                   (required is positive because goal, rate, years are)
#                   message = savings_check(required, planned)
#   4. DISPLAY:    show required deposit and message
# DECISION LOGIC inside savings_check (if/elif/else):
#   round both to cents
#   IF planned < required     -> "Shortfall of $X.XX"
#   ELIF planned == required  -> "Meets requirement"
#   ELSE (planned > required) -> "Extra savings of $X.XX"
#
# Assumptions kept: fixed nominal annual rate, monthly compounding,
#   month-end payments/deposits, no fees, zero starting savings.
#
# COPILOT PROMPTS (replace with your actual prompts)
#   budget_check: "Implement budget_check from my header and docstring.
#     Round both values to 2 decimals, then use if/elif/else to return
#     'Below budget', 'Exactly at budget', or 'Over budget'. Assume valid
#     finite input. No print, input, loops, or exceptions."
#   savings_check: "Implement savings_check from my header and docstring.
#     Round both values to 2 decimals, then use if/elif/else to return a
#     string with the shortfall or extra amount to 2 decimals, or
#     'Meets requirement'. Assume valid input. No print, input, loops,
#     or exceptions."
#
# NOTE ON CHANGES TO GENERATED CODE (edit to match what really happened)
#   Example: "Copilot compared unrounded floats; I added round(x, 2)."
# ======================================================================


# ------------------ Base helpers and payment functions ------------------

def payment_periods(years):
    """Return the number of monthly payments for whole-number years."""
    return years * 12


def monthly_interest_rate(rate):
    """Return the monthly rate as a decimal from an annual percent."""
    return rate / 100 / 12


def monthly_loan_payment(amount, rate, years):
    """Return the monthly loan payment. Positive amount, rate, whole years."""
    r = monthly_interest_rate(rate)
    n = payment_periods(years)
    return amount * r / (1 - (1 + r) ** -n)


def monthly_savings_payment(goal, rate, years):
    """Return the monthly savings deposit. Positive goal, rate, whole years."""
    r = monthly_interest_rate(rate)
    n = payment_periods(years)
    return goal * r / ((1 + r) ** n - 1)


# ------------------ Homework validators (reused) ------------------

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


# ------------------ New validator for this project ------------------

def is_nonnegative_amount(amount):
    """Return True if a numeric amount is zero or greater (dollars)."""
    if amount >= 0:
        return True
    else:
        return False


# ------------------ Option 1: budget_check ------------------

def budget_check(payment, budget):
    """Compare a monthly loan payment to a monthly budget.

    Args:
        payment (float): Monthly payment in dollars. Must be >= 0.
        budget (float): Monthly budget in dollars. Must be >= 0.
    Returns:
        str: "Below budget", "Exactly at budget", or "Over budget".
    Boundary rules:
        - Both values are rounded to cents before comparing.
        - payment == budget after rounding is "Exactly at budget".
        - 0 is valid for both; (0, 0) is "Exactly at budget".
    The caller enforces the input contract.
    """
    payment = round(payment, 2)
    budget = round(budget, 2)
    if payment < budget:
        return "Below budget"
    elif payment == budget:
        return "Exactly at budget"
    else:
        return "Over budget"


# ------------------ Option 8: savings_check ------------------

def savings_check(required, planned):
    """Compare a planned monthly deposit to the required deposit.

    Args:
        required (float): Required deposit in dollars. Must be > 0.
        planned (float): Planned deposit in dollars. Must be >= 0.
    Returns:
        str: "Shortfall of $X.XX", "Meets requirement", or
             "Extra savings of $X.XX".
    Boundary rules:
        - Both values are rounded to cents before comparing.
        - planned == required after rounding is "Meets requirement".
        - planned == 0 is valid and gives a shortfall equal to required.
    The caller enforces the input contract.
    """
    required = round(required, 2)
    planned = round(planned, 2)
    if planned < required:
        return f"Shortfall of ${required - planned:.2f}"
    elif planned == required:
        return "Meets requirement"
    else:
        return f"Extra savings of ${planned - required:.2f}"


# ------------------ Direct tests (no loops) ------------------
# Which condition selects each outcome:
#   budget_check:   payment < budget -> Below; payment == budget -> Exactly
#                   at; the default else (payment > budget) -> Over.
#   savings_check:  planned < required -> Shortfall; planned == required ->
#                   Meets requirement; the default else -> Extra savings.
# Rounding to cents first means 249.999 vs 250 compares as 250.00 vs 250.00.

print("=== Option 1: budget_check (budget 250) ===")
print("T1  payment 200      expected: Below budget       actual:", budget_check(200, 250))
print("T2  payment 250      expected: Exactly at budget  actual:", budget_check(250, 250))
print("T3  payment 275      expected: Over budget        actual:", budget_check(275, 250))

print()
print("=== Option 8: savings_check (required 200) ===")
print("T7  planned 150      expected: Shortfall of $50.00  actual:", savings_check(200, 150))
print("T8  planned 200      expected: Meets requirement    actual:", savings_check(200, 200))
print("T9  planned 250      expected: Extra savings of $50.00  actual:", savings_check(200, 250))


# ------------------ Option 1 input section ------------------
# Why else means "all checks passed": the chain tests for failure with
# not, and Python runs only the first true branch, so the final else is
# reached only when every validator passed.

print()
print("=== Option 1: Loan payment vs. monthly budget ===")
loan_amount = float(input("Loan amount in dollars: "))
loan_rate = float(input("Annual interest rate in percent: "))
loan_years = float(input("Term in whole years: "))
budget = float(input("Monthly budget in dollars: "))

if not is_positive_amount(loan_amount):
    print("Error: the loan amount must be greater than zero.")
elif not is_positive_rate(loan_rate):
    print("Error: the annual interest rate must be greater than zero.")
elif not is_valid_years(loan_years):
    print("Error: the term must be a positive whole number of years.")
elif not is_nonnegative_amount(budget):
    print("Error: the budget cannot be negative.")
else:
    loan_years = int(loan_years)  # convert only after validation
    payment = monthly_loan_payment(loan_amount, loan_rate, loan_years)
    print(f"Monthly loan payment: ${payment:.2f}")
    print(f"Budget: ${budget:.2f} -> {budget_check(payment, budget)}")


# ------------------ Option 8 input section ------------------

print()
print("=== Option 8: Savings deposit check ===")
goal = float(input("Savings goal in dollars: "))
savings_rate = float(input("Annual interest rate in percent: "))
savings_years = float(input("Term in whole years: "))
planned = float(input("Planned monthly deposit in dollars: "))

if not is_positive_amount(goal):
    print("Error: the savings goal must be greater than zero.")
elif not is_positive_rate(savings_rate):
    print("Error: the annual interest rate must be greater than zero.")
elif not is_valid_years(savings_years):
    print("Error: the term must be a positive whole number of years.")
elif not is_nonnegative_amount(planned):
    print("Error: the planned deposit cannot be negative.")
else:
    savings_years = int(savings_years)  # convert only after validation
    required = monthly_savings_payment(goal, savings_rate, savings_years)
    print(f"Required monthly deposit: ${required:.2f}")
    print(f"Planned: ${planned:.2f} -> {savings_check(required, planned)}")
