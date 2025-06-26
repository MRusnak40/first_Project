# show balance
import time
import Casino




def showBalance(balance):
    print("********************")
    print(f"balance ${balance:.2f}")
    print("********************")


# vklad
def deposit(balance, amount):
    balance += amount
    print("********************")
    print(f"you deposited ${amount:.2f}")
    print("********************")

    return balance


# vybrat
def withdraw(balance, amount):
    print("********************")
    if amount > 0:

        if balance >= amount:
            balance -= amount

            return balance
        else:
            print("Invalid amount (REQUEST CANCELED)")
            print("********************")
            return balance

    else:
        print("Invalid amount (REQUEST CANCELED)")
        print("********************")
        return balance


def convert(balance, amount):
    print("********************")

    name = str(input("Enter name the recipient:"))
    if amount > 0:

        if balance >= amount:
            balance -= amount

            print(f"you sent ${amount:.2f} to {name}")
            print("********************")
            return balance
        else:
            print("Invalid amount (REQUEST CANCELED)")
            print("********************")
            return balance

    else:
        print("Invalid amount (REQUEST CANCELED)")
        print("********************")
        return balance


def main():
    balance = 0
    is_running = True

    while is_running:
        print("-------Banking program-------")
        print("STARTING", end=" ")

        for x in range(6):
            time.sleep(1)
            print(".", end="")

        print(" ")
        print(" ")
        print("1-FUNCION-")
        print("-------------")
        print("2-Show balance-")
        print("3-Deposit-")
        print("4-Withdraw-")
        print("5-Convert-")
        print("6-Casino")
        print("7-Exit-")
        print(" ")

        while is_running:
            match input("Enter what you want: "):

                case "1":
                    showBalance(balance)
                case "2":
                    balance = deposit(balance,float(input("Enter amount to deposit: ")))
                case "3":

                    balance = withdraw(balance,float(input("Enter amount to deposit: ")))
                case "4":
                    balance = withdraw(balance,float(input("Enter amount to deposit: ")))
                case "5":
                    balance = convert(balance,float(input("Enter amount to deposit: ")))
                case "6":
                    Casino.casino()
                case "7":
                    print(" ")
                    print("Thank you for using this program")
                    print("Closing program", end="")
                    for x in range(6):
                        time.sleep(1)
                        print(".", end="")

                    is_running = False

                case _:
                    print(" ")
                    print("Invalid input")
                    print("choose 1-6")
                    print(" ")
                    continue


if __name__ == "__main__":
    main()
