import random


MAX_LINES = 5
MAX_BET = 200
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 5,
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [[], [], []]
    for _ in range(cols):
        column = [] 
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

        
def deposit():
    while True:
        amount = input("How much would you like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a number greater than 0: ")
        else:
            print("Please enter a number that is greater than 0: ")
    return amount

def number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines, (1-" + str(MAX_LINES) + "),: ")
        else:
            print("Please enter a number that is greater than 0: ")
    return lines

def get_bet():
    while True:
        bet = input("How much do you to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter a number between ${MIN_BET} and ${MAX_BET}:")
        else:
            print("Please enter a number that is greater than 0: ")
    return bet

def main():
    balance = deposit()
    lines = number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet >= balance:
            print(f"You do not have enough money to make this bet. Your balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Your total bet is ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()