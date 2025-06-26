
import random


def spin():
    roulette = ["♥", "♦", "♣"]
    finish=[]

    return [random.choice(roulette) for _ in range(3)]



def casino():
    print("------------------")
    print("Welcome to Casino!")
    print("------------------")
    print(" ")


if __name__ == "__main__":
    casino()
    spin()

