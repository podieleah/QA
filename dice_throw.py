from dice import roll_dice

def throw_dice():
    dice1 = roll_dice()
    dice2 = roll_dice()
    total = dice1 + dice2
    print(f"You rolled {dice1} and {dice2} - Total: {total}")

throw_dice()
