import random

# main routine goes here
tokens =["unicorn", "horse", "horse", "horse", "zebra", "zebra", "zebra", "donkey", "donkey", "donkey"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0, 100):
    chosen = random. randint(1, 100)
    # Adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final balance: ${:.2f}".format(balance))
    #output
print("token: {} , Balance: ${}".format(chosen, balance))
