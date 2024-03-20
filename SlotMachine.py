MAX_LINES=3
MAX_BET=100
MIN_BET=1

def deposit():
    while True:
        amount=input("what would you like to deposit?")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("emount must be greater then 0.")
        else:
            print("please enter a number.")

    return amount



def get_number_of_lineS():
     
     while True:
        lines=input("Enter the number of lines to bet on (1-" +str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines=int(lines)

            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter a valid nunber of lines")
        else:
            print("please enter a number.")

     return lines

def get_bet():
     while True:
        amount=input("what would you like to bet for each line?")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"emount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a bet.")

     return amount

def main():
    balance=deposit()
    lines=get_number_of_lineS()
    while True:
        bet=get_bet()
        total_bet=bet*lines

        if total_bet> balance:
            print(f"you do not have enough to bet that amount,your current balance is: ${balance}")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines. total bet is equal to: ${total_bet}")


main()
