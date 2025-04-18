import random


def print_row(row):
    print(" | ".join(row))


def spin_row():
    symbol = ["🍒","🍉", "🔔", "⭐"]
    return [random.choice(symbol)for _ in range(3)]

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0]== "🍒":
            return bet*3
        elif row[0]=='🍉':
            return bet*4
        elif row[0]=="🔔":
            return bet*10
        elif row[0]=="⭐":
            return bet*20
    return 0

def main():
    print("Welcome to Slot Machine")
    balance = float(input("Enter your Balance: $ "))
    print(f"Your balance is ${balance}")
    print("🍒 🍉 🔔 ⭐")

    while balance > 0:
        print(f"Your balance is ${balance}")
        bet = input("Place your amount :")

        if not bet.isdigit():
            print("Invalid number")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient funds")

        elif bet <= 0:
            print("Your bet must be greater than 0$")

        else:
            balance -= bet
            row = spin_row()
            print("Spinning...")
            print_row(row)
            payout = get_payout(row, bet)
            if payout > 0:
                print(f"You won ${payout}")
            else:
                print("You lost this round")
            balance +=payout
        play_again=input("Do you want to spin again(Y/N): ").upper()
        if play_again !='Y':
            break
    print("Better luck next time")

if __name__ == "__main__":
    main()