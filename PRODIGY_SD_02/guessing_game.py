import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        
        # Create and place the widgets
        tk.Label(root, text="Guess the number between 1 and 100:").pack(pady=10)
        
        self.entry_guess = tk.Entry(root)
        self.entry_guess.pack(pady=5)
        
        self.btn_guess = tk.Button(root, text="Guess", command=self.check_guess)
        self.btn_guess.pack(pady=10)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
    
    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.attempts += 1
            if guess < self.target_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.target_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You guessed the number in {self.attempts} attempts.")
                self.show_win_message()
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number.")
    
    def show_win_message(self):
        messagebox.showinfo("Game Over", f"Congratulations! You guessed the number in {self.attempts} attempts.")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
