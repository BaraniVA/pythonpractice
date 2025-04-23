import tkinter as tk
import random
import time
import os

colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'Purple', 'Brown', 'Gray']
score = 0
time_left = 45
high_score_file = "highscore.txt"

def load_high_score():
    if os.path.exists(high_score_file):
        with open(high_score_file, "r") as file:
            return int(file.read())
    return 0

def save_high_score(score):
    with open(high_score_file, "w") as file:
        file.write(str(score))

def start_game(event):
    if time_left == 30:
        countdown()
    next_color()

def next_color():
    global score
    global time_left

    if time_left > 0:
        entry.focus_set()

        if entry.get().lower() == color_label.cget("fg").lower():
            score += 1

        entry.delete(0, tk.END)

        random.shuffle(colors)
        color_label.config(text=colors[0], fg=colors[1])
        score_label.config(text=f"Score: {score}")

def countdown():
    global time_left
    if time_left > 0:
        time_left_label.config(text=f"Time left: {time_left}s")
        time_left -= 1
        root.after(1000, countdown)
    else:
        high = load_high_score()
        if score > high:
            save_high_score(score)
            result_label.config(text=f"Time's up! New High Score: {score}")
        else:
            result_label.config(text=f"Time's up! Your score: {score} | High Score: {high}")

# GUI setup
root = tk.Tk()
root.title("Color Game")
root.geometry("400x200")

instructions = tk.Label(root, text="Type the COLOR of the word, not the word itself!", font=('Helvetica', 12))
instructions.pack()

score_label = tk.Label(root, text="Score: 0", font=('Helvetica', 12))
score_label.pack()

time_left_label = tk.Label(root, text="Time left: 30s", font=('Helvetica', 12))
time_left_label.pack()

color_label = tk.Label(root, font=('Helvetica', 30))
color_label.pack()

entry = tk.Entry(root)
entry.pack()
entry.bind('<Return>', start_game)

result_label = tk.Label(root, text="", font=('Helvetica', 12))
result_label.pack()

entry.focus_set()
root.mainloop()
