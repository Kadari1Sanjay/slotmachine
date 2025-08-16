import random

MAX_BET = 100
MIN_BET = 1
MAX_LINES = 3

ROWS = 3
COLM = 3

Symbols_Count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

Symbols_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, values, bet, lines):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings, winnings_lines

def get_slot_machine_spin(rows, colm, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(colm):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_sm(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("Enter the amount: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input(f"Enter your bet per line (${MIN_BET}-${MAX_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough balance. Your balance: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLM, Symbols_Count)
    print_sm(slots)
    winnings, winnings_lines = check_winnings(slots, Symbols_values, bet, lines)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winnings_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to spin (or 'q' to quit): ")
        if answer.lower() == "q":
            break
        balance += spin(balance)
    print(f"You left with a balance of ${balance}")

main()
