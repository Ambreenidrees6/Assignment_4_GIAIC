AFFIRMATION : str = "I am a programmer and one day I'll become successful!"

def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()  # Get user's input
    while user_feedback != AFFIRMATION:  
        print("That was not the affirmation.")
        return

    print("That's right! :)")

main()
