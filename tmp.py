#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


secret = random.randint(1, 99)
guess = 0
tries = 0
print(type(secret))
print(type(guess))
print("AHOY! I'm the Dread Pireate Roberts, and I have a secret!")
print("It is a number from 1 to 99, I'll give you 6 tries.")
while guess != secret and tries < 6:
    guess = int(input("What's yer guess? "))  # In Python 2, don't need int()
    if guess < secret:
        print("Too low, ye scurvy dog!")
    elif guess > secret:
        print("Too high, landlubber!")

    tries = tries + 1

if guess == secret:
    print("Avant! Ye got is! Found my secret, ye did!")
else:
    print("No more guesses! Better luck next time, matey!")
    print("The secret number was", secret)
