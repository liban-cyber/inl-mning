import random

class BoardGameMaterial:
    """Class to represent generic board game materials."""
    pass # placeholder for future extensions

class Die(BoardGameMaterial):
    """ class to represent singel six-side die."""
    def __init__(self):
        """initialize die with random value between 1 to 6."""
        self.value = self.roll()  # Initialize die with a random roll

    def __str__(self):
        return f"Dice shows {self.value}"

    def roll(self):
        """Roll the die and update its value."""
        self.value = random.randint(1, 6)
        return self.value # return the new value

    @staticmethod
    def roll_static():
        """Static method to roll a die without creating an instance."""
        return random.randint(1, 6)

    def reroll(self):
        """Reroll the die and update its value."""
        return self.roll()

# Example usage
if __name__ == "__main__":
    die = Die()
    print(die)  # Print the current value of the die
    print("Rolling the die...")
    die.roll()  # Roll the die again
    print(die)  # Print the new value of the die
    print("Static roll:", Die.roll_static())  # Roll a die using the static method
