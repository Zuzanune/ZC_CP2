from tkinter import *
root = Tk()
root.title("My Portfolio")
root.geometry("400x300")
title_label = Label(root, text="My Portfolio", font=("Arial", 16))
title_label.pack(pady=10)
#buttons!
rpg_button = Button(root, text="RPG Character Manager", font=("Arial", 12), command=lambda: open_rpg()).grid(row=1, column=0)
financial_button = Button(root, text="maze generator", font=("Arial", 12), command=lambda: open_maze()).grid(row=1, column=1)
library_button = Button(root, text="Personal Library", font=("Arial", 12), command=lambda: open_library()).grid(row=1, column=2)
back_button = Button(root, text="Back to menu", font=("Arial", 12), command=show_buttons).grid(row=2, column=1)
root.mainloop()
def hide_buttons():
    rpg_button.grid_remove()
    financial_button.grid_remove()
    library_button.grid_remove()
    back_button.grid()
def show_buttons():
    rpg_button.grid()
    financial_button.grid()
    library_button.grid()
    back_button.grid_remove()
def open_rpg():
    hide_buttons()
    rpg_discription = Label(root, text="RPG Character Manager is a program that allows you to create and manage your own RPG characters. You can create characters with different attributes, skills, and equipment. I made it originally as a group project, but I remade it as a personal project. i pretty much just remade the entire program and i am very proud of it.", font=("Arial", 12), wraplength=300)
    rpg_discription.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
def open_maze():
    hide_buttons()
    maze_discription = Label(root, text="The maze generator is a program that allows you to create mazes that are theoreticlly solvable. I made it as a personal project. I was very proud of it, as i used an interesting method for creating the maze and figuring out how to solve it. even if it never worked perfectly.", font=("Arial", 12), wraplength=300)
    maze_discription.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
def open_library():
    hide_buttons()
    library_discription = Label(root, text="The personal library is a program that allows you to manage your own collection of books. I made it as a personal project, and I am very proud of it. i actually used it formy own use to keep track of books on my shelve on my home computer.", font=("Arial", 12), wraplength=300)
    library_discription.grid(row=3, column=0, columnspan=3, padx=10, pady=10)