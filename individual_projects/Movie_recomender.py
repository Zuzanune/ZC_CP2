#ZC 1st Movie Recommender
import csv
import os
import sys

#use file Movies_dictionary.csv to create a movie database
#the database should be a dictionary where the keys are the movie titles and the values are lists containing the director, genre, rating, length, and notable actors for each movie
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'Movies_dictionary.csv')
try:
    with open(csv_path, mode='r') as file:
        database = {}
        reader = csv.reader(file)
        for row in reader:
            title = row[0]
            director = row[1]
            genre = row[2]
            rating = row[3]
            length = row[4]
            notable_actors = row[5]
            database[title] = [director, genre, rating, length, [notable_actors.split(", ")]]

except FileNotFoundError:
    print(f"CSV file not found at: {csv_path}")
    print("Make sure Movies_dictionary.csv is in the same folder as this script.")
    sys.exit(1)
#introduction
print("Welcome to the Movie Recommender!")
print("You can search for movies based on Title, Director, Genre, Rating, Length, or Notable Actors.")
#while true:
while True:
    print ("would you like to search for a movie or print the entire database?")
    user_choice = input("Enter 'search' to search for a movie or 'print' to print the entire database: ")
    if user_choice.lower() == "print":
        for title, info in database.items():
            print(f"Title: {title}")
            print(f"Director: {info[0]}")
            print(f"Genre: {info[1]}")
            print(f"Rating: {info[2]}")
            print(f"Length: {info[3]}")
            print(f"Notable Actors: {info[4]}")
            print()
        continue
    elif user_choice.lower() != "search":
        print("Invalid choice. Please enter 'search' or 'print'.")
        continue
    if user_choice.lower() == "search":
    #ask user if they are selecting Title,Director,Genre,Rating,Length, or Notable Actors
        display_search_types = ["Title", "Director", "Genre", "Rating", "Minimum Length", "Notable Actors"]
    #ask user to input the specific title, director, genre, rating, length, or notable actor
        filters = []
        for x in display_search_types:
            appends = input(f"Enter the {x} you are looking for (or leave blank to skip): ")
            if appends == "":
                appends = "N/APPLICABLE"
            filters.append(appends)
        print (filters)
        matching_movies = []
        for i in database:
            if filters[0].lower() in i.lower() or filters[1].lower() in database[i][0].lower() or filters[2].lower() in database[i][1].lower() or filters[3].lower() in database[i][2].lower() or filters[4] in database[i][3] or filters[5].lower() in database[i][4][0][0].lower() or filters[5].lower() in database[i][4][0][1].lower() or filters[5].lower() in database[i][4][0][2].lower() or filters[5].lower() in database[i][4][0][3].lower() or filters[5].lower() in database[i][4][0][4].lower():
                matching_movies.append(i)
        if matching_movies:
            print("Matching movies:")
            for movie in matching_movies:
                print(movie)
        else:
            print("No matching movies found.")
        


#search through the movie database and find movies that match the user's input
#display the matching movies to the user