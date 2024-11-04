import random
import tkinter as tk
from tkinter import messagebox


def roll_dice():
    # Simulate rolling two dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2


def play_game(player_choice):
    dice1, dice2 = roll_dice()
    dice_sum = dice1 + dice2

    # Update dice roll labels
    dice1_label.config(text=f"Dice 1: {dice1}")
    dice2_label.config(text=f"Dice 2: {dice2}")
    total_label.config(text=f"Total: {dice_sum}")

    # Determine the outcome
    if dice_sum > 7:
        result = 'up'
    elif dice_sum < 7:
        result = 'down'
    else:
        result = '7'

    # Check if the player won
    if player_choice == result:
        messagebox.showinfo("Result", "Congratulations! You won!")
    else:
        messagebox.showinfo("Result", "Sorry, you lost!")


def on_up():
    play_game('up')


def on_down():
    play_game('down')


def on_seven():
    play_game('7')


# Create the main window
window = tk.Tk()
window.title("7 Up and 7 Down Game")

# Instructions label
instructions_label = tk.Label(window,
                              text="Guess whether the sum of two dice is greater than 7, less than 7, or exactly 7.")
instructions_label.pack()

# Dice roll result labels
dice1_label = tk.Label(window, text="Dice 1: ")
dice1_label.pack()

dice2_label = tk.Label(window, text="Dice 2: ")
dice2_label.pack()

total_label = tk.Label(window, text="Total: ")
total_label.pack()

# Buttons for player's choice
up_button = tk.Button(window, text="Up (Greater than 7)", command=on_up)
up_button.pack()

down_button = tk.Button(window, text="Down (Less than 7)", command=on_down)
down_button.pack()

seven_button = tk.Button(window, text="Exactly 7", command=on_seven)
seven_button.pack()

# Start the GUI event loop
window.mainloop()