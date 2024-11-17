def display_menu():
    print("\n--- The Avaliable oprions are: ---")
    print("1. Palindrome Check")
    print("2. Lowercase Check")
    print("3. Digit Check")
    print("4. Length Check (greater than 15)")
    print("5. Empty Check")
    print("6. Exit Program")
    print("--------------------------------")
    print("Enter the number for the operation you want to perform:")

def is_palindrome(input_str):
    return input_str == input_str[::-1]

def is_lowercase(input_str):
    return input_str.islower()

def is_digit(input_str):
    return input_str.isdigit()

def length_check(input_str, threshold=15):
    return len(input_str) > threshold

def is_empty(input_str):
    return input_str == ""

def main():
    while True:
        display_menu()
        
        try:
            choice = int(input("Choose an option (1-6): "))
            if choice == 6:
                print("Exiting the program.")
                break
            
            # Execute the chosen operation
            if choice == 1:
                # Ask for user input to again
                input_str = input("Enter the input string to analyze: ")
                result = is_palindrome(input_str)
                print(f"Palindrome Check: {'True' if result else 'False'}")
            elif choice == 2:
                # Ask for user input to again
                input_str = input("Enter the input string to analyze: ")
                result = is_lowercase(input_str)
                print(f"Lowercase Check: {'True' if result else 'False'}")
            elif choice == 3:
                # Ask for user input to again
                input_str = input("Enter the input string to analyze: ")
                result = is_digit(input_str)
                print(f"Digit Check: {'True' if result else 'False'}")
            elif choice == 4:
                # Ask for user input to again
                input_str = input("Enter the input string to analyze: ")
                result = length_check(input_str)
                print(f"Length Check (>15): {'True' if result else 'False'}")
            elif choice == 5:
                # Ask for user input to again
                input_str = input("Enter the input string to analyze: ")
                result = is_empty(input_str)
                print(f"Empty Check: {'True' if result else 'False'}")
            else:
                raise ValueError()
        
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
