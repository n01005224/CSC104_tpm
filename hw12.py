# ======================================================================
# loan_menu.py
# Loan Calculator: a repeating menu that uses while and for loops.
# ======================================================================
#
# PLAN (where the menu repeats, how a choice selects an action, how it stops)
#   START
#   LOOP (while choice != "3"):
#       DISPLAY menu
#       READ choice as text
#       IF choice == "1":
#           READ amount   -> repeat until amount > 0
#           READ rate     -> repeat until rate > 0
#           READ years    -> repeat until years > 0 and whole
#           CONVERT years to int, CALL monthly_loan_payment, DISPLAY result
#       ELIF choice == "2":
#           READ years    -> repeat until years > 0 and whole
#           number_of_payments = years * 12
#           FOR payment_number from 1 to number_of_payments: DISPLAY label
#       ELIF choice == "3":
#           DISPLAY goodbye (loop condition now ends the program)
#       ELSE:
#           EXPLAIN the choice is unknown (menu is shown again)
#       (after any branch, control returns to the top of the loop)
#   END
#
#   Retry path for invalid input: each prompt sits in its own while loop.
#   An invalid value prints a message and loops back to the same prompt.
#   A valid value ends that inner loop and the program moves on.
#
# COPILOT USE (edit to match what really happened)
#   Example: "I wrote the function descriptions first, then prompted
#   Copilot for the validation loops. I changed it to keep years as a
#   float until validation passed." Or: "I did not use Copilot."
#
# EXPLANATIONS
#   Why while for the menu? We do not know in advance how many actions the
#   user will want. while repeats until a condition (choice is "3") is met.
#   Why for for payment labels? We know exactly how many labels to print
#   (years * 12), so a counted for loop over range() fits.
#   Why is the range() stop one greater than the final payment number?
#   range() excludes its stop value. To include payment 12 the stop must
#   be 13, which is why the code uses number_of_payments + 1.
# ======================================================================


def payment_periods(years):
    """Return the number of monthly payments for whole-number years."""
    return years * 12


def monthly_interest_rate(rate):
    """Return the monthly rate as a decimal from an annual percent."""
    return rate / 100 / 12


def monthly_loan_payment(amount, rate, years):
    """Return the monthly loan payment.

    Contract: positive amount and rate; positive whole years.
    The caller enforces this contract.
    """
    r = monthly_interest_rate(rate)
    n = payment_periods(years)
    return amount * r / (1 - (1 + r) ** -n)


def show_menu():
    """Display the menu. Printing only; returns nothing."""
    print()
    print("Loan Calculator")
    print("1. Calculate a monthly loan payment")
    print("2. Display payment numbers for a loan term")
    print("3. Quit")


def read_positive(prompt, error_message):
    """Ask until the user enters a number greater than zero; return it."""
    value = float(input(prompt))
    while value <= 0:
        print(error_message)
        value = float(input(prompt))
    return value


def read_whole_years():
    """Ask until the user enters positive whole-valued years.

    Years stay a float while checked, so 2.5 is caught before any int
    conversion. Returns an int only after validation succeeds.
    """
    years = float(input("Term in whole years: "))
    while years <= 0 or years % 1 != 0:
        if years <= 0:
            print("Years must be greater than zero.")
        else:
            print("Years must be a whole number.")
        years = float(input("Term in whole years: "))
    return int(years)


# ---------------- Main menu loop ----------------

choice = ""
while choice != "3":
    show_menu()
    choice = input("Choose 1, 2, or 3: ").strip()

    if choice == "1":
        amount = read_positive("Loan amount in dollars: ",
                               "Amount must be greater than zero.")
        rate = read_positive("Annual interest rate in percent (6 means 6%): ",
                             "Rate must be greater than zero.")
        years = read_whole_years()
        payment = monthly_loan_payment(amount, rate, years)
        print(f"Monthly payment: ${payment:.2f}")

    elif choice == "2":
        years = read_whole_years()
        number_of_payments = payment_periods(years)
        for payment_number in range(1, number_of_payments + 1):
            print(f"Payment {payment_number}")

    elif choice == "3":
        print("Goodbye!")

    else:
        print(f"'{choice}' is not a valid choice. Please enter 1, 2, or 3.")
