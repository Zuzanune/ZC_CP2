from tkinter import *
root = Tk()
root.title("My Portfolio")
root.geometry("400x300")
title_label = Label(root, text="My Portfolio", font=("Arial", 16))
title_label.pack(pady=10)
#buttons for code
rpg_button = Button(root, text="RPG Character Manager", font=("Arial", 12), command=lambda: open_rpg()).grid(row=1, column=0)
financial_button = Button(root, text="maze generator", font=("Arial", 12), command=lambda: open_maze()).grid(row=1, column=1)
library_button = Button(root, text="Personal Library", font=("Arial", 12), command=lambda: open_library()).grid(row=1, column=2)
back_button = Button(root, text="Back to menu", font=("Arial", 12), command=show_buttons()).grid(row=2, column=1)
root.mainloop()
#functions for buttons.
def hide_buttons():
    #this hides the buttons and shows the discription of the project, then shows a back button to go back to the menu
    rpg_button.grid_remove()
    financial_button.grid_remove()
    library_button.grid_remove()
    back_button.grid()
def show_buttons():
    #this shows the buttons and hides the discription of the project, then shows a back button to go back to the menu
    rpg_button.grid()
    financial_button.grid()
    library_button.grid()
    back_button.grid_remove()
def open_rpg():
    #hides buttons and shows discription of the project, then shows a back button to go back to the menu
    hide_buttons()
    rpg_discription = Label(root, text="- RPG Character Manager is a program that allows you to create and manage your own RPG characters. \n" \
    "- You can create characters with different attributes, skills, and equipment. \n" \
    "- I made it originally as a group project, but I remade it as a personal project. \n" \
    "- i pretty much just remade the entire program to save with files, and i am very proud of it.", font=("Arial", 12), wraplength=300)
    rpg_discription.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
def open_maze():
    #hides buttons and shows discription of the project, then shows a back button to go back to the menu
    hide_buttons()
    maze_discription = Label(root, text="-The maze generator is a program that allows you to create mazes that are theoreticlly solvable. \n I made it as a personal project. \n I was very proud of it, as i used an interesting method for creating the maze and figuring out how to solve it. \n it never worked perfectly, but i  still enjoyed building it", font=("Arial", 12), wraplength=300)
    maze_discription.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
def open_library():
    #hides buttons and shows discription of the project, then shows a back button to go back to the menu
    hide_buttons()
    library_discription = Label(root, text="- The personal library is a program that allows you to manage your own collection of books. \nI made it as a personal project, and I am quite happy at how it turned out.\n It was my first time working with csv files, and I think i did pretty great. \ni actually used it for my own use to keep track of books on my shelve on my home computer, and it worked for the most part", font=("Arial", 12), wraplength=300)
    library_discription.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
