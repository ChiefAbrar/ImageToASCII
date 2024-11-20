from PIL import Image
import tkinter as tk
from tkinter import filedialog, simpledialog
import os

def asciiConvert(image, type, scale):
    scale = int(scale)
    img = Image.open(image)
    w, h = img.size
    img.resize((w // scale, h // scale)).save("resized.%s" % type)
    img = Image.open("resized.%s" % type)
    w, h = img.size
    grid = []
    for i in range(h):
        grid.append(["X"] * w)

    pix = img.load()

    for y in range(h):
        for x in range(w):
            if sum(pix[x, y]) == 0:
                grid[y][x] = "#"
            elif sum(pix[x, y]) in range(1, 100):
                grid[y][x] = "X"
            elif sum(pix[x, y]) in range(100, 200):
                grid[y][x] = "%"
            elif sum(pix[x, y]) in range(200, 300):
                grid[y][x] = "&"
            elif sum(pix[x, y]) in range(300, 400):
                grid[y][x] = "*"
            elif sum(pix[x, y]) in range(400, 500):
                grid[y][x] = "+"
            elif sum(pix[x, y]) in range(500, 600):
                grid[y][x] = "/"
            elif sum(pix[x, y]) in range(600, 700):
                grid[y][x] = "("
            elif sum(pix[x, y]) in range(700, 750):
                grid[y][x] = "'"
            else:
                grid[y][x] = " "
    save_directory = filedialog.askdirectory(title="Select a directory to save the file")
    
    if save_directory:
        new_filename = simpledialog.askstring("Save As", "Enter the name of the file (without extension):", initialvalue="Cat")
        
        if new_filename:
            save_path = os.path.join(save_directory, f"{new_filename}.txt")
            with open(save_path, "w") as art:
                for row in grid:
                    art.write("".join(row) + "\n")
            print(f"File saved to: {save_path}")
        else:
            print("No filename provided. File not saved.")
    else:
        print("No directory selected. File not saved.")

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    image_file = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image Files", "*.jpg;*.png")])

    if image_file:
        asciiConvert(image_file, "jpg", "Cat.txt", "3")
    else:
        print("No image file selected.")