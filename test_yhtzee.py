from yahtzee import YahtzeeMainClass
from die import Die
import pytest

def test_is_yahtzee_when_all_dice_matches():
    # Create a list of five dice
    dice = [Die(), Die(), Die(), Die(), Die()]
    
    # Set all dice values to 6
    # by setting all dice to the same valu, it can test the yahtzee condition
    for die in dice:
        die.value = 6
    
    # Create a Yahtzee game instance with the dice
    yahtzee_game = YahtzeeMainClass()
    yahtzee_game.dice = dice  # Directly set the dice
    
    # Assert that it is a Yahtzee
    # this skould return true since all dice values are the same
    assert yahtzee_game.is_yahtzee() == True, "Should be Yahtzee when all dice match"

def test_is_not_yahtzee_when_all_dice_not_matching_each_other():
    # Create a list of five dice
    dice = [Die(), Die(), Die(), Die(), Die()]
    
    # Set four dice values to 6 and one die value to 2
    for die in dice:
        die.value = 6
    dice[0].value = 2
    
    # Create a Yahtzee game instance with the dice
    yahtzee_game = YahtzeeMainClass()
    yahtzee_game.dice = dice  # Directly set the dice
    
    # Assert that it is not a Yahtzee
    assert yahtzee_game.is_yahtzee() == False, "Should not be Yahtzee when all dice do not match"

if __name__ == '__main__':
    pytest.main()
