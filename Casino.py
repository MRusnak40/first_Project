
import random


def spin():
    roulette = ["♥", "♦", "♣"]
    finish=[]

    return [random.choice(roulette) for _ in range(3)]

def checkingList():
    roulette = spin()

    print("******************")
    for x in roulette:
        print(f"|-{x}-|",end=" ")

    print(" ")
    print("******************")

    if roulette[0] == roulette[1]==roulette[2]:
        print("You won!")
    else:
        print("You lost!")

def casino():
    print("------------------")
    print("Welcome to Casino!")
    print("------------------")
    print(" ")
    checkingList()



if __name__ == "__main__":
    casino()


