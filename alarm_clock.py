import datetime
import time
import pygame



def set_alarm_clock(alarm_clock):
    print("Alarm Clock set for " + alarm_clock)

if __name__ == '__main__':
    alarm_time=input("Enter alarm time (HH:MM:SS):")
    set_alarm_clock(alarm_time)
