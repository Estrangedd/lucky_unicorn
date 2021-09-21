
import random

# main routine goes here
STARTING_BALANCE = 100
balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0,500):
    chosen_num = random.randint(1,100)
    # Adjust balance]
    if chosen_num <= 5:
        chosen = "Unicorn"
        balance += 4

    elif 6 > chosen_num < 36:
        chosen = "Donkey"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen ="Horse"
        else:
            chosen = "Zebra"
    balance -= 0.5

    #output
    print("token: {} , Balance: ${:.2f}".format(chosen, balance))

print()
