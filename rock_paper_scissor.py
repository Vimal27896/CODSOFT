import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissor" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "Opponent wins!"

# Function to handle the user's choice
def make_choice(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result)
    
    if result == "It's a tie!":
        restart_button.pack()
    else:
        play_again_button.pack()
        exit_button.pack()

# Function to restart the game
def restart_game():
    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    result_label.config(text="")
    restart_button.pack_forget()
    play_again_button.pack_forget()
    exit_button.pack_forget()

# Function to exit the game
def exit_game():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Create labels and buttons
welcome_label = tk.Label(window, text="Welcome to Rock-Paper-Scissors!", font=("Times New Roman", 16))
welcome_label.pack()

instruction_label = tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Times New Roman", 14))
instruction_label.pack()

user_choice_label = tk.Label(window, text="", font=("Times New Roman", 14))
user_choice_label.pack()

computer_choice_label = tk.Label(window, text="", font=("Times New Roman", 14))
computer_choice_label.pack()

result_label = tk.Label(window, text="", font=("Times New Roman", 14))
result_label.pack()

rock_button = tk.Button(window, text="Rock", command=lambda: make_choice("Rock"))
rock_button.pack(side=tk.LEFT, padx=20)

paper_button = tk.Button(window, text="Paper", command=lambda: make_choice("Paper"))
paper_button.pack(side=tk.LEFT, padx=20)

scissors_button = tk.Button(window, text="Scissors", command=lambda: make_choice("Scissors"))
scissors_button.pack(side=tk.LEFT, padx=20)

restart_button = tk.Button(window, text="Restart", command=restart_game)
restart_button.pack_forget()

play_again_button = tk.Button(window, text="Play Again", command=restart_game)
play_again_button.pack_forget()

exit_button = tk.Button(window, text="Exit", command=exit_game)
exit_button.pack_forget()

# Start the main loop
window.mainloop()