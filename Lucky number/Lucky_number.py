import random

class LuckyNumberGame:
    def __init__(self):
        # Initialize game variables
        self.player_name = None
        self.player_birthdate = None
        self.player_age = None
        self.lucky_list = []
        self.lucky_number = None
        self.tries_count = 0

    def get_player_name(self):
        """Get the player's name."""
        while True:
            # Ask the user for their full name
            self.player_name = input("Enter your full name: ")

            # Check if the input contains only letters and one space between first and last name
            if self.player_name.replace(" ", "").isalpha():
                break
            else:
                print("Please enter a valid name with only characters and one space between first and last name.")

    def get_player_birthdate(self):
        """Get the player's birthdate."""
        while True:
            # Prompt the user for their birthdate in the specified format
            birthdate = input("Enter your birthdate in yyyymmdd format: ")

            # Check if the input is in the correct format and within valid date ranges
            if len(birthdate) == 8 and birthdate.isdigit():
                year = int(birthdate[:4])
                month = int(birthdate[4:6])
                day = int(birthdate[6:])
                if 1900 <= year <= 2023 and 1 <= month <= 12 and 1 <= day <= 31:
                    self.player_birthdate = birthdate
                    break
                else:
                    print("Invalid date. Please enter a valid date.")
            else:
                print("Invalid format. Please enter a valid birthdate.")

    def calculate_player_age(self):
        """Calculate the player's age."""
        birth_year = int(self.player_birthdate[:4])
        # Calculate the player's age based on the current year (2023)
        self.player_age = 2023 - birth_year

    def generate_lucky_list(self):
        """Generate a list of lucky numbers."""
        # Generate a list of 9 random integers between 0 and 100 (inclusive)
        self.lucky_list = random.sample(range(101), 9)

    def generate_lucky_number(self):
        """Generate a lucky number and add it to the lucky list."""
        # Generate a random lucky number between 0 and 100 (inclusive)
        self.lucky_number = random.randint(0, 100)
        # Add the lucky number to the lucky list
        self.lucky_list.append(self.lucky_number)

    def play_game(self):
        """Play the game."""
        try_count = 0  # Initialize try_count to 0
        while True:
            try_count += 1  # Increment the try_count for each try
            # Display the current try number and the current lucky list
            print(f"This is try #{try_count}, and the new list is: {self.lucky_list}")
            # Prompt the player to choose a lucky number from the list
            player_input = input("Choose a lucky number from the list: ")
            try:
                player_choice = int(player_input)
                if player_choice == self.lucky_number:
                    self.tries_count += 1
                    # Display a congratulatory message with the try number
                    print(f"Congratulations! You got the lucky number from try #{self.tries_count}")
                    play_again = input("Do you want to play again? (y/n): ")
                    if play_again.lower() == 'n':
                        break
                    else:
                        self.reset_game()  # Reset the game if the player wants to play again
                elif player_choice in range(self.lucky_number - 10, self.lucky_number + 11):
                    self.tries_count += 1
                    # Shorten the lucky list based on the player's choice
                    self.shorten_lucky_list(player_choice)
                else:
                    print("Invalid choice. Please choose a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def shorten_lucky_list(self, player_choice):
        """Shorten the lucky list based on the player's choice."""
        # Filter the lucky list to include only numbers within 10 units of the player's choice
        self.lucky_list = [num for num in self.lucky_list if abs(num - player_choice) <= 10]

    def reset_game(self):
        """Reset the game by reinitializing game variables."""
        self.__init__()  # Reset all game variables

if __name__ == "__main__":
    random.seed(42)  # Set a fixed seed for reproducibility
    game = LuckyNumberGame()
    game.get_player_name()
    game.get_player_birthdate()
    game.calculate_player_age()

    if game.player_age < 18:
        print("Sorry, you must be at least 18 years old to play.")
    else:
        game.generate_lucky_list()
        game.generate_lucky_number()
        game.play_game()  # Start the game if the player is old enough
