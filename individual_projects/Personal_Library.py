#ZC 1st Personal Library.py
#introduce the program
print("Welcome to your personal library!")
library = []
#library = [{'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}, {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}, {'title': '1984', 'author': 'George Orwell'}, {'title': 'Pride and Prejudice', 'author': 'Jane Austen'}, {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'}, {'title': 'Fahrenheit 451', 'author': 'Ray Bradbury'}, {'title': 'Moby Dick', 'author': 'Herman Melville'}, {'title': 'Jane Eyre', 'author': 'Charlotte Bronte'}, {'title': 'Wuthering Heights', 'author': 'Emily Bronte'}, {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien'}, {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien'}, {'title': 'Harry Potter and the Sorcerers Stone', 'author': 'J.K. Rowling'}, {'title': 'The Chronicles of Narnia', 'author': 'C.S. Lewis'}, {'title': 'A Tale of Two Cities', 'author': 'Charles Dickens'}, {'title': 'Great Expectations', 'author': 'Charles Dickens'}, {'title': 'Oliver Twist', 'author': 'Charles Dickens'}, {'title': 'Frankenstein', 'author': 'Mary Shelley'}, {'title': 'Dracula', 'author': 'Bram Stoker'}, {'title': 'The Picture of Dorian Gray', 'author': 'Oscar Wilde'}, {'title': 'The Strange Case of Dr Jekyll and Mr Hyde', 'author': 'Robert Louis Stevenson'}, {'title': 'Treasure Island', 'author': 'Robert Louis Stevenson'}, {'title': 'The Three Musketeers', 'author': 'Alexandre Dumas'}, {'title': 'The Count of Monte Cristo', 'author': 'Alexandre Dumas'}, {'title': 'War and Peace', 'author': 'Leo Tolstoy'}, {'title': 'Crime and Punishment', 'author': 'Fyodor Dostoevsky'}, {'title': 'The Brothers Karamazov', 'author': 'Fyodor Dostoevsky'}, {'title': 'Anna Karenina', 'author': 'Leo Tolstoy'}, {'title': 'Madame Bovary', 'author': 'Gustave Flaubert'}, {'title': 'Les Miserables', 'author': 'Victor Hugo'}, {'title': 'The Hunchback of Notre Dame', 'author': 'Victor Hugo'}, {'title': 'Dune', 'author': 'Frank Herbert'}, {'title': 'Foundation', 'author': 'Isaac Asimov'}, {'title': 'Enders Game', 'author': 'Orson Scott Card'}, {'title': 'The Martian', 'author': 'Andy Weir'}, {'title': 'Ready Player One', 'author': 'Ernest Cline'}, {'title': 'Snow Crash', 'author': 'Neal Stephenson'}, {'title': 'Neuromancer', 'author': 'William Gibson'}, {'title': 'The Handmaids Tale', 'author': 'Margaret Atwood'}, {'title': 'Beloved', 'author': 'Toni Morrison'}, {'title': 'One Hundred Years of Solitude', 'author': 'Gabriel Garcia Marquez'}, {'title': 'The Odyssey', 'author': 'Homer'}, {'title': 'Beowulf', 'author': 'Unknown'}, {'title': 'Hamlet', 'author': 'William Shakespeare'}, {'title': 'Macbeth', 'author': 'William Shakespeare'}, {'title': 'Utopia', 'author': 'Thomas More'}, {'title': 'The Republic', 'author': 'Plato'}, {'title': 'Aesops Fables', 'author': 'Aesop'}, {'title': 'Don Quixote', 'author': 'Miguel de Cervantes'}, {'title': 'The Jungle Book', 'author': 'Rudyard Kipling'}, {'title': 'Alice in Wonderland', 'author': 'Lewis Carroll'}]
#define add function
def add():
    #   ask user for book title and author
    title = input("Enter book title: ").capitalize()
    author = input("Enter book author: ").capitalize()
    for book in library:
        if book['title'].lower() == title.lower() and book['author'].lower() == author.lower():
            print("This book is already in the library.")
            doub = input("are you sure you want to add it again? (yes/no)   ").strip().lower()
            if doub == "no" or doub == "n":
                return
            if doub == "yes" or doub == "y":
                break
    
#   add book to library list
    library.append({'title': title, 'author': author})
    print(f'Book "{title}" by {author} added to library.')
#define search function
def search():
    #   ask user to search by title or author
    search_type = input("Search by title or author?   ").strip().lower()
    search_term = input("Enter search term: ").strip().lower()
    
    #   search list by going through each name in a for loop, then checking if the search term is in the name
    matches = []
    for book in library:
        if (search_type == 'title' or search_type == 't') and search_term in book['title'].lower() or (search_type == 'author' or search_type == 'a') and search_term in book['author'].lower():
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
    #   remove book from library list
    matches = []
    for book in library:
        if book['title'].lower() == title_to_remove:
            count += 1
            matches.append(book)
    if count == 0:
        print ("no book found matching that title")
    if count > 1:
        print ("more than one book found matching that title")
        for x in matches:
            print (f'"{x["title"]}" by {x["author"]}')
        author_to_remove = input("Enter the author of the book to remove: ").strip().lower()
        for book in library:
            if book['title'].lower() == title_to_remove and book['author'].lower() == author_to_remove:
                library.remove(book)
                print(f'Book "{book["title"]}" by {book["author"]} removed from library.')
                return
            else:
                print ("no book matches that title and author")
    if count == 1:
        library.remove(book)
        print(f'Book "{book["title"]}" by {book["author"]} removed from library.')
        return

#define view function
def view():
    #   display all books in library list
    if library:
        print("Books in library:")
        for book in library:
            print(f'"{book["title"]}" by {book["author"]}')
    else:
        print("Library is empty.")

#define main function
def main():
    while True:
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