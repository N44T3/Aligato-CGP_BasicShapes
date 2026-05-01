import tkinter as tk

window = tk.Tk()
window.title("My Train - BSIT3-EV")
window.geometry("1000x700")
window.resizable(False, False)

# Canvas
canvas = tk.Canvas(window, width=1000, height=550, bg="white")
canvas.pack()

# Colors
green = "#2ecc71"
yellow = "#f1c40f"
red = "#e74c3c"
blue = "#3498db"
dark_green = "#1e8449"
brown = "#7d3c98"
black = "black"
gray = "#ecf0f1"


# ENGINE (GREEN)
canvas.create_rectangle(100, 250, 300, 400, fill=green, outline=black, width=3)

# Front triangle
canvas.create_polygon(50, 400, 100, 250, 100, 400, fill=dark_green, outline=black)

# Window
canvas.create_rectangle(160, 280, 240, 360, fill=gray, outline=black, width=3)

# Chimney (LABASAN NG USOK)
canvas.create_rectangle(170, 140, 210, 250, fill=blue, outline=black, width=2)

# Top triangle
canvas.create_polygon(150, 140, 230, 140, 190, 90, fill="red", outline=black)


# FIRST CAR (YELLOW)
canvas.create_rectangle(360, 250, 560, 400, fill=yellow, outline=black, width=3)

canvas.create_rectangle(380, 280, 460, 340, fill=gray, outline=black, width=3)
canvas.create_rectangle(470, 280, 550, 340, fill=gray, outline=black, width=3)


# SECOND CAR (RED)
canvas.create_rectangle(620, 250, 820, 400, fill=red, outline=black, width=3)

canvas.create_rectangle(640, 280, 720, 340, fill=gray, outline=black, width=3)
canvas.create_rectangle(730, 280, 810, 340, fill=gray, outline=black, width=3)


# CONNECTORS TO PRE
canvas.create_rectangle(300, 370, 360, 400, fill="brown", outline=black)
canvas.create_rectangle(560, 370, 620, 400, fill="brown", outline=black)

wheel_y = 400
wheel_r = 30
wheel_centers = [150, 250, 410, 510, 670, 770]

for x in wheel_centers:
    canvas.create_oval(x-wheel_r, wheel_y-wheel_r, x+wheel_r, wheel_y+wheel_r,
                       fill=blue, outline=black, width=3)    
    canvas.create_oval(x-15, wheel_y-15, x+15, wheel_y+15,
                       fill="black", outline="white", width=2)

canvas.create_text(500, 470, text="Aligato, Nathaniel L.",
                   font=("Arial", 20, "bold"), fill="black")

canvas.create_text(500, 510, text="BSIT3-EV",
                   font=("Arial", 15, "bold"), fill="black")




window.mainloop()
