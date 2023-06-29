import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(cols, lines, bet, values):
    for line in range(lines):
        symbol = cols[0][line]
        for col in cols:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
    
    return winnings


def get_slot_machine_spin(rows, cols, symbols):
    """
    "Which symbol will represent each column, based on the frequency of
    our symbols we've defined outside of this function?"
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        curr_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(curr_symbols)
            curr_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns


def print_slot_machine(columns):
    # Transpose
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != (len(columns) - 1):
                print(col[row], end=" | ")
            else:
                print(col[row], end="")
        print()


def deposit():
    # Keep asking until input is valid
    while True:
        amount = input("What would you like deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if (amount > 0):
                break    # Break out of the while-loop
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if (1 <= lines <= MAX_LINES):
                break    # Break out of the while-loop
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if (MIN_BET <= amount <= MAX_BET):
                break    # Break out of the while-loop
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if (total_bet > balance):
            print(f"You cannot bet more than your balance.\nYour current balance: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()
