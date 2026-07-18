"""Visualize an illustrative worldwide popularity comparison of ten premium cars.

This chart is a relative ranking based on the earlier discussion, not verified
global June sales.  Manufacturers do not release comparable global monthly
sales data for every model.
"""

import tkinter as tk


# Higher values indicate comparatively broader worldwide buying volume.
# Values are illustrative ranking scores (not reported sales figures).
cars = [
    "Tesla Model S Plaid",
    "Porsche 911 Turbo S",
    "BMW M5",
    "Audi RS6 Avant",
    "Mercedes-AMG GT",
    "Rolls-Royce Phantom",
    "Lamborghini Revuelto",
    "Ferrari SF90 Stradale",
    "McLaren 750S",
    "Bugatti Chiron Super Sport",
]
scores = [100, 82, 75, 68, 62, 28, 21, 18, 14, 5]

BAR_START = 285
BAR_MAX_WIDTH = 560
ROW_HEIGHT = 43

window = tk.Tk()
window.title("Top 10 Cars - Popularity Comparison")

canvas = tk.Canvas(window, width=970, height=570, bg="white", highlightthickness=0)
canvas.pack(padx=16, pady=16)

canvas.create_text(
    485,
    25,
    text="Illustrative Worldwide Buying Popularity: Top 10 Premium Cars",
    font=("Arial", 16, "bold"),
)

for tick in range(0, 101, 20):
    x = BAR_START + (tick / 100) * BAR_MAX_WIDTH
    canvas.create_line(x, 65, x, 500, fill="#d9d9d9", dash=(3, 3))
    canvas.create_text(x, 515, text=str(tick), font=("Arial", 9))

for index, (car, score) in enumerate(zip(cars, scores)):
    y = 72 + index * ROW_HEIGHT
    width = (score / 100) * BAR_MAX_WIDTH
    color = "#2b6cb0" if index < 5 else "#718096"
    canvas.create_text(BAR_START - 12, y + 14, text=car, anchor="e", font=("Arial", 10))
    canvas.create_rectangle(BAR_START, y, BAR_START + width, y + 28, fill=color, outline="")
    canvas.create_text(BAR_START + width + 8, y + 14, text=str(score), anchor="w", font=("Arial", 10, "bold"))

canvas.create_text(
    485,
    550,
    text=("Blue: comparatively higher-volume models. Gray: exclusive low-volume models. "
          "Scores are illustrative, not worldwide June sales figures."),
    font=("Arial", 9),
)

window.mainloop()
