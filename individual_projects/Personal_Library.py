#ZC 1st Personal Library.py
def validate_input(text, kind='int'):
    s = str(text).strip().capitalize()
    if kind == 'int':
        try:
            int(s)
            return True
        except ValueError:
            return False
    elif kind == 'float':
        try:
            float(s)
            return True
        except ValueError:
            return False
    elif kind == 'alpha':
        return s.isalpha()
    else:
        return False
import csv
with open('individual_projects/Library.csv', 'r') as library_file:
    library = list(csv.DictReader(library_file))

#introduce the program
print("Welcome to your personal library!")
def add():
    #   ask user for book title and author
    title = input("Enter book title: ").capitalize()
    author = input("Enter book author: ").capitalize()
    genre = input("enter book genre:  ").capitalize()
    while True:
        year = input("enter year book was released:  ").strip()
        if not validate_input(year, kind='int'):
            print ("please enter an intiger value")
            continue
        year = int(year)
        break
    for book in library:
        if book['title'].lower() == title.lower() and book['author'].lower() == author.lower():
            print("This book is already in the library.")
            doub = input("are you sure you want to add it again? (yes/no)   ").strip().lower()
            if doub == "no" or doub == "n":
                return
            if doub == "yes" or doub == "y":
                break
    
#   add book to library list
    with open('individual_projects/Library.csv', 'a', newline='') as book:
        writer = csv.DictWriter(book, fieldnames=['title', 'author', 'genre', 'year'])
        writer.writerow({'title': title, 'author': author, 'genre' : genre, 'year' : year})
    print(f'Book "{title}" by {author} added to library.')

#define search function
def search():
    #   ask user to search by title or author
    search_type = int(input("Search by 1.title, 2.author, 3.genre or 4. year released? ").strip())
    if search_type == 1:
        search_type = "title"
    elif search_type == 2:
        search_type = "author"
    elif search_type == 3:
        search_type = "genre"
    elif search_type == 4:
        search_type = "year"
    search_term = input("Enter search term: ").strip().lower()
    #   search list by going through each name in a for loop, then checking if the search term is in the name
    matches = []
    for book in library:
        if search_type == 'title' and search_term in book['title'].lower() or (search_type == 'author') and search_term in book['author'].lower() or (search_type == 'genre') and search_term in book['genre'].lower() or (search_type == 'year') and search_term in book['year'].lower():
            matches.append(book)
#   display matching books from library list
    if matches:
        print("matching books:")
        for book in matches:
            print(f'"{book["title"]}" by {book["author"]}')
    else:
        print("No books were found matching your search.")

#define remove function
def remove():
    count = 0
    #   ask user for book title to remove
    title_to_remove = input("Enter the title of the book to remove: ").strip().lower()
    #   remove book from library.csv
    matches = []
    for book in library:
        if book['title'].lower() == title_to_remove:
            count += 1
            matches.append(book)
    if count == 0:
        print("no book found matching that title")
        return
    if count > 1:
        print("more than one book found matching that title")
        for x in matches:
            print(f'"{x["title"]}" by {x["author"]}')
        author_to_remove = input("Enter the author of the book to remove: ").strip().lower()
    else:
        author_to_remove = matches[0]['author'].lower()
    with open('individual_projects/Library.csv', 'r') as books:
        lines = books.readlines()
    with open('individual_projects/Library.csv', 'w') as books:
        for line in lines:
            if not (line.strip().split(',')[0].lower() == title_to_remove and line.strip().split(',')[1].lower() == author_to_remove):
                books.write(line)
    print(f'Book "{title_to_remove}" by {author_to_remove} removed from library.')

#define view function
def view():
    #   display all books in library list
    emp = False
    if library:
        print("Books in library:")
        for book in library:
            print(f'{book["title"]} by {book["author"]}')
        emp = True
    else:
        print("Library is empty.")
    if emp:
        while True:
            while True:
                select = input("would you like to select any of these books? (y/n) \n").lower()
                if select not in ["y", "n", "yes", "no"]:
                    print ("please enter y or n")
                    continue
                break
            if select == "y" or select =="yes":
                name = input("please enter the name of the book you are looking for:  \n")
                for book in library:
                    if book["title"] == name:
                        print (f"title: {book['title']} \n author: {book['author']} \n genre : {book['genre']} \n year released: {book['year']}")
            if select == 'n' or select == 'no':
                break
    return

#define main function
def main():
    global library
    while True:
        with open('individual_projects/Library.csv', 'r') as library_file:
            library = list(csv.DictReader(library_file))
    #   display menu with options to add, search, remove, or quit
        print ("would you like to add, remove, search, view, or quit")
        menu_choice = input()
    #   call appropriate function based on user input
        if menu_choice == "add" or menu_choice == "a":
            add()
        elif menu_choice == "remove" or menu_choice == "r":
            remove()
        elif menu_choice == "search" or menu_choice == "s":
            search()
        elif menu_choice == "view" or menu_choice == "v":
            view()
        elif menu_choice == "quit" or menu_choice == "q":
            print("Goodbye.")
            return
        else:
            print("Invalid input")
#   loop until user chooses to quit
#call main function
main()