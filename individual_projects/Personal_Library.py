#ZC 1st Personal Library.py
# define library list
library = []
library = [{'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}, {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}]
#define add function
def add():
    #   ask user for book title and author
    title = input("Enter book title: ").capitalize()
    author = input("Enter book author: ").capitalize()
    
#   add book to library list
    library.append({'title': title, 'author': author})
    print(f'Book "{title}" by {author} added to library.')
#define search function
def search():
    #   ask user to search by title or author
    search_type = input("Search by title or author? (title/author): ").strip().lower()
    search_term = input("Enter search term: ").strip().lower()
    
    #   search list by going through each name in a for loop, then checking if the search term is in the name
    matches = []
    for book in library:
        if (search_type == 'title' or search_type == "t" and search_term in book['title'].lower()) or (search_type == 'author' or search_type == "a" and search_term in book['author'].lower()):
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
    #   ask user for book title to remove
    title_to_remove = input("Enter the title of the book to remove: ").strip().lower()
    #   remove book from library list
    for book in library:
        if book['title'].lower() == title_to_remove:
            library.remove(book)
            print(f'Book "{book["title"]}" by {book["author"]} removed from library.')
            return
    print("Book not found in library.")
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
        if menu_choice == "add" or "a":
            add()
        elif menu_choice == "remove" or "r":
            remove()
        elif menu_choice == "search" or "s":
            search()
        elif menu_choice == "view" or "v":
            view()
        elif menu_choice == "quit" or "q":
            print("Goodbye.")
            return
        else:
            print("Invalid input")
#   loop until user chooses to quit
#call main function
main()
