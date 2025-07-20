import datetime
import time
import pygame


def set_alarm_clock(alarm_clock):
    print("Alarm Clock set for " + alarm_clock)
    sound_file = "Scooter x Blasterjaxx x CERES - Heart Attack.mp3"
    is_rinning = True

    while is_rinning:
        curent_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(curent_time)
        if curent_time == alarm_clock:
            print("+++++++++++++++++++")
            print("WAKE UP")
            print(" ")
            print(" ")
            print("I LIKE IT LOUD")
            print("+++++++++++++++++++")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while (pygame.mixer.music.get_busy()):
                time.sleep(1)

        time.sleep(1)


if __name__ == '__main__':
    alarm_time = input("Enter alarm time (HH:MM:SS):")
    set_alarm_clock(alarm_time)
