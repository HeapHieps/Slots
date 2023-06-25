import random

MAX_LINES = 3
MAX_BET = 100 # Maxium amount you can bet(interchangeable)
MIN_BET = 1   # Minimum amount you can bet(interchangeable)

ROWS = 3
COLS = 3

symbol_count = {
    "A":2, 
    "B":4,
    "C":6,
    "D":8
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winning(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_Slot_spins(rows,cols,symbols):
    All_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            All_symbols.append(symbol)
    
    columns = []
    for col in range(cols):
        column=[]
        current_symbols = All_symbols[:]## [:] means copy
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value) #remove the value so we dont pick it again
            column.append(value)
        columns.append(column)
    return columns

def print_slots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):## enumerage gives index(0,1,2,3) and item
            if i != len(columns) - 1:
                print(column[row], end = "|")
            else:
                print(column[row], end ="")## end tells the statement what to end the line with
        print()

def desposit():
    while True: #While Loop, only stops when theres a "break"
        amount = input("Enter desposit amount:$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount need to be greater than 0")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    while True: #While Loop, only stops when theres a "break"
        lines = input("Enter number of lines to bet on (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Invalid lines")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True: #While Loop, only stops when theres a "break"
        bet = input("Enter betting amount:$")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Amount must be between $" + str(MIN_BET) + "-$" + str(MAX_BET))
        else:
            print("Please enter a number")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet_amount = get_bet()
        total_bet = lines * bet_amount  

        if total_bet > balance:
            print(f"Not enough to bet, current balance:${balance}")
        else:
            break

    print(f" You're betting ${bet_amount} on {lines} lines. Total bet is ${total_bet}")
    
    slots = get_Slot_spins(ROWS, COLS, symbol_count)
    print_slots(slots)
    winnings, winning_lines = check_winning(slots, lines, bet_amount, symbol_value)
    print(f"You've won ${winnings}.")
    print(f"You won o lines: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = desposit()
    while True:
        print(f"Current balance is:${balance}")
        answer= input("Please enter to play(q to quit)")
        if answer == "q":
            break
        balance +=spin(balance)

    print(f"You've left with ${balance}")

main()
