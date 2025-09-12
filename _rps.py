import tkinter as tk
import random

# Game Logic
def play(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"
        update_score("user")
    else:
        result = "Computer wins!"
        update_score("computer")

    result_label.config(
        text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}"
    )

def update_score(winner):
    global user_score, computer_score
    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Main GUI
root = tk.Tk()
root.title("Rock-Paper-Scissors Game 🎮")
root.geometry("400x400")
root.resizable(False, False)
root.config(bg="#f0f0f0")

# Scores
user_score = 0
computer_score = 0

# Labels
tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

tk.Button(button_frame, text="🪨 Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="📄 Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="✂️ Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="blue")
result_label.pack(pady=20)

# Score Display
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="green")
score_label.pack(pady=10)

# Exit Button
tk.Button(root, text="Exit Game", command=root.quit, bg="red", fg="white", width=15).pack(pady=20)

root.mainloop()
