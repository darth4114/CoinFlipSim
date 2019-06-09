import modules

print("Welcome to the flip a coin game!")

while True:

	num = modules.ask()

	results = modules.flip_count(num)

	print(f"Over {num} fiips, the results are {results[0]} heads and {results[1]} tails!\n")

	if input("Would you like to play again? (y/n): ").lower() == 'y':
		continue
	else:
		print("Thanks for playing!")
        print("This is an edit to test Git!")
		break
