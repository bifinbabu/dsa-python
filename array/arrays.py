expenses = [2200, 2350, 2600, 2130, 2190]


# 1. In Feb, how many dollars you spent extra compare to January?
def jan_feb_comparison():
    return expenses[1] - expenses[0]


print(jan_feb_comparison())


# 2. Find out your total expense in first quarter (first three months) of the year.
def find_first_quarter_expense():
    total_expense = 0
    for i in range(3):
        total_expense += expenses[i]
    return total_expense


print(find_first_quarter_expense())


# 3. Find out if you spent exactly 2000 dollars in any month
def check_2000_spend():
    for i in range(len(expenses)):
        if expenses[i] == 2000:
            return True
    return False


print(check_2000_spend())


# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
def add_june_expense():
    expenses.append(1980)
    return expenses


print(add_june_expense())


# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
def add_april_refund():
    expenses[3] = expenses[3] - 200
    return expenses


print(add_april_refund())


# --------------------------------------------------------------------------------------------------------------


exp = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print("In feb this much extra was spent compared to jan:", exp[1] - exp[0])  # 150

# 2. Find out your total expense in first quarter (first three months) of the year
print("Expense for first quarter:", exp[0] + exp[1] + exp[2])  # 7150

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month? ", 2000 in exp)  # False

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print("Expenses at the end of June:", exp)  # [2200, 2350, 2600, 2130, 2190, 1980]

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3] = exp[3] - 200
print(
    "Expenses after 200$ return in April:", exp
)  # [2200, 2350, 2600, 1930, 2190, 1980]
