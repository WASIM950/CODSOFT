import random
import tkinter as tk
from tkinter import messagebox

def get_user_choice():
    user_choice = user_choice_var.get()
    if user_choice in ["Rock", "Paper", "Scissor"]:
        return user_choice
    else:
        messagebox.showerror("Error", "Invalid input. Please enter Rock, Paper, or Scissor.")
        return None

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "Tie"

    if (user_choice == "Rock" and comp_choice == "Scissor") or \
       (user_choice == "Paper" and comp_choice == "Rock") or \
       (user_choice == "Scissor" and comp_choice == "Paper"):
        return "You Win"
    else:
        return "Computer Wins"

def play_game(event=None):
    user_choice = get_user_choice()
    if user_choice:
        comp_choice = random.choice(["Rock", "Paper", "Scissor"])
        computer_choice_var.set(f"Computer's choice: {comp_choice}")

        result = determine_winner(user_choice, comp_choice)
        result_var.set(f"Result: {result}")

        # Clear user input and set focus back to input field
        user_choice_var.set("")
        user_input.focus_set()

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x250")

# Styling
root.configure(bg="#E6E6FA")  # Lavender background color

# Labels
tk.Label(root, text="Enter your move (Rock, Paper, Scissor):", font=("Arial", 12), bg="#E6E6FA").pack(pady=10)
user_choice_var = tk.StringVar()
user_input = tk.Entry(root, textvariable=user_choice_var, font=("Arial", 12), bd=3, relief='ridge')
user_input.pack()

# Bind Enter key to play_game function
user_input.bind("<Return>", play_game)

# Buttons
play_button = tk.Button(root, text="Play", font=("Arial", 12), bd=3, relief='raised', fg="#FFFFFF", bg="#3CB371", command=play_game)
play_button.pack(pady=10)

# Output Labels
computer_choice_var = tk.StringVar()
computer_choice_label = tk.Label(root, textvariable=computer_choice_var, font=("Arial", 12), bg="#E6E6FA")
computer_choice_label.pack()

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12, "bold"), bg="#E6E6FA")
result_label.pack()

# Focus on input field at start
user_input.focus_set()

root.mainloop()
