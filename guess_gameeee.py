# Initial balance for the user
user_balance = 100  # Let's assume they have KSh 100 initially
account_balance = 0  # Your account balance

secret_number = 9
guess_count = 0
guess_limit = 1
entry_fee = 20  # KSh 20
winning_prize = 40  # KSh 40

# Check if the user has enough money to play
if user_balance >= entry_fee:
    print("Welcome to the game! You've been charged KSh 20 to play.")

    # Deduct the entry fee and add it to your account
    user_balance -= entry_fee
    account_balance += entry_fee

    while guess_count < guess_limit:
        guess = int(input("Guess: "))
        guess_count += 1

        if guess == secret_number:
            print("You won! You've earned KSh 40.")
            # Transfer prize to user
            user_balance += winning_prize
            account_balance -= winning_prize
            break
    else:
        print("You lost! KSh 20 remains in my account.")
else:
    print("You don't have enough money to play.")

print(f"Your balance: KSh {user_balance}")
print(f"My account balance: KSh {account_balance}")
