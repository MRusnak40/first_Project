import random
import time


def hazard(budget):
    while True:
        print(" ")
        print("-------------------------")
        moneyForRound = input("What you want give in to one round:")

        if moneyForRound.isdigit():
            moneyForRound = int(moneyForRound)
        else:
            print("That's not a number")
            print("Try again")
            continue

        if moneyForRound <= budget and budget>0:
            print(" ")

            return moneyForRound

        else:
            print("You don't have enough money")
            print("Try again")
            print(" ")
            break


def spin():
    roulette = ["♥", "♦", "♣"]
    #

    return [random.choice(roulette) for _ in range(3)]


def checkingList(money):
    roulette = spin()

    print("******************")
    for x in roulette:
        print(f"|-{x}-|", end=" ")

    print(" ")
    print("******************")

    if roulette[0] == roulette[1] == roulette[2]:
        print(f"You won ${money * 3:.2f}!")
        return True
    else:
        print(f"You lost ${money:.2f}!")
        return False


def casino(budget):
    print("------------------")
    print("Welcome to Casino!")
    print("------------------")

    playing = True
    print(" ")
    print("LETS PLAY")
    print("------------------")
    print(" ")

    while playing:
        match input("Press 'p' to continue | Press 'q' to quit:"):

            case "p":

                print(f"Your budget is ${budget:.2f}:" )
                moneyInRound = hazard(budget)

                lottery = checkingList(moneyInRound)
                print(" ")
                if lottery:
                    budget += int(moneyInRound * 2)
                else:
                    budget -= moneyInRound

            case "q":

                playing = False
                print("++++++++++++++++++++++")
                print("Thank you for playing!")
                print("RETURNING TO BANK", end=" ")
                for x in range(4):
                    print(".", end=" ")
                    time.sleep(1)
                print(" ")
                print("++++++++++++++++++++++")

            case _:
                print("++++++++++++++++++++++")
                print("Invalid input. Please try again.")
                print("++++++++++++++++++++++")

                continue


if __name__ == "__main__":
    casino(int(300))
