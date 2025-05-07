import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    score = 0
    current_number = random.randint(1, 100)

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_num}")
        print(f"Current number: {current_number}")
        
        
        guess = input("Will the next number be higher or lower? (h/l): ").lower()
        while guess not in ['h', 'l']:
            guess = input("Invalid input. Please enter 'h' for higher or 'l' for lower: ").lower()

        next_number = random.randint(1, 100)
        print(f"Next number: {next_number}")

        
        if (guess == 'h' and next_number > current_number) or (guess == 'l' and next_number < current_number):
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
        
        current_number = next_number

    print('--------------------------------')
    print(f"Game over! Your final score is {score} out of {NUM_ROUNDS}.")

if __name__ == "__main__":
    main()
