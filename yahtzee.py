from die import Die

class YahtzeeMainClass:
    def __init__(self):
        self.dice = [Die() for _ in range(5)]  # Create a list of five dice
        self.keep_playing = True  # Flag to keep the game going
        
        # Start the game loop
        while self.keep_playing:
            self.play_game()

    def play_game(self):
        """Main logic for the Yahtzee game."""
        turn = 0
        print("Welcome to Yahtzee!")
        
        # Loop for up to three turns
        while turn < 3:
            print(f"Starting turn: {turn + 1} of 3, rolling dice")
            
            # Roll all dice
            for i, die in enumerate(self.dice):
                die.roll()
                print(f"{i + 1}: {die}")

            # Check for Yahtzee
            if self.is_yahtzee():
                print(f"You got YAHTZEE! in {self.dice[0].value}'s")
                return
            else:
                # If not Yahtzee, ask if the player wants to continue
                if turn < 2:
                    if input("Want to throw again? (y for yes, anything else for no) ").lower() != 'y':
                        self.keep_playing = False
                        break
                else:
                    if input("Game over! Want to play again? (y for yes, anything else for no) ").lower() == 'y':
                        turn = 0  # Reset turn to 0 to start a new game
                        continue
                    else:
                        self.keep_playing = False
                        break
            
            turn += 1

    def is_yahtzee(self):
        """Check if all dice have the same value."""
        first_value = self.dice[0].value
        return all(die.value == first_value for die in self.dice)

def main():
    YahtzeeMainClass()

if __name__ == '__main__':
    main()
