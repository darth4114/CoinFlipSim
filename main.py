import modules

print("Welcome to the flip a coin game! You can pick how many times you want to flip a coin, and this program will tell you how many were heads and how many were tails.\nLet's Begin!")

while True:

    num = modules.ask()

    results = modules.flip_count(num)

    print(
        f"Over {num} fiips, the results are {results[0]} heads and {results[1]} tails!\n")

    if input("Would you like to play again? (y/n): ").lower() == 'y':
        continue
    else:
        print("Thanks for playing!")
        break
