import tkinter as tk
from tkinter import colorchooser

def pick_color():
    color_code = colorchooser.askcolor(title="Choose a color")
    if color_code:
        hex_color, rgb_color = color_code[1], color_code[0]
        if hex_color:
            color_preview.config(bg=hex_color)
            hex_value_label.config(text=hex_color)
            rgb_value_label.config(text=f"RGB: {int(rgb_color[0])}, {int(rgb_color[1])}, {int(rgb_color[2])}")

root = tk.Tk()
root.title("Enhanced Color Picker Tool")
root.geometry("400x300")

tk.Label(root, text="Enhanced Color Picker Tool", font="Arial 18 bold").pack(pady=10)

# Enlarged 'Pick a Color' button
pick_button = tk.Button(root, text="Pick a Color", command=pick_color, font="Arial 14", width=15, height=2)
pick_button.pack(pady=10)

# Color preview area
color_preview = tk.Label(root, text="Color Preview", font="Arial 12", bg="white", width=30, height=3, relief="sunken")
color_preview.pack(pady=10)

# Separate labels for Hex and RGB values
tk.Label(root, text="Hex Color:", font="Arial 12").pack(pady=5)
hex_value_label = tk.Label(root, text="#FFFFFF", font="Arial 12", bg="white", relief="sunken", width=15)
hex_value_label.pack()

tk.Label(root, text="RGB Color:", font="Arial 12").pack(pady=5)
rgb_value_label = tk.Label(root, text="RGB: (255, 255, 255)", font="Arial 12", bg="white", relief="sunken", width=15)
rgb_value_label.pack()

root.mainloop()
