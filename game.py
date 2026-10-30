import random

def choose_difficulty():
    print("\nSelect Difficulty Level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")
    
    while True:
        choice = input("Enter choice (1/2/3 or q to quit): ").strip()
        if choice.lower() == 'q':
            return None
        
        if choice == '1':
            return 10
        elif choice == '2':
            return 7
        elif choice == '3':
            return 5
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 'q'.")

def guess_the_number():
    print("========================================")
    print("  Welcome to the Number Guessing Game! (1 to 100)")
    print("========================================")
    
    
    max_attempts = choose_difficulty()
    if max_attempts is None:
        return False
        
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print(f"\nGame started! You have {max_attempts} attempts to guess the number.")
    
    while attempts < max_attempts:
        user_input = input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter a number (1-100) or 'q' to quit: ").strip()
        
        if user_input.lower() == 'q':
            return False

        try:
            guess = int(user_input)
            
            if guess < 1 or guess > 100:
                print("❌ Error: Please enter a number between 1 and 100 only.")
                continue
                
            attempts += 1
            
            if guess < secret_number:
                print("🔼 Too low!")
            elif guess > secret_number:
                print("🔽 Too high!")
            else:
                print(f"🎉 Congratulations! You found the correct number in {attempts} attempts.")
                return True
                
        except ValueError:
            print("❌ Error: Please enter a valid number.")
            
  
    print(f"\n❌ Game Over! You've used all {max_attempts} attempts. The secret number was {secret_number}.")
    return True

def main():
    while True:
        result = guess_the_number()

        if result is False:
            print("Game exited. See you next time!")
            break
        
        restart = input("\nDo you want to play again? (y/n): ").strip().lower()
        if restart != 'y':
            print("Thank you for playing. Good luck!")
            break

if __name__ == "__main__":
    main()
