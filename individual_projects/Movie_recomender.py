# ZC 1st Movie Recommender
import csv
import os
import sys

# use file Movies_dictionary.csv to create a movie database
# the database should be a dictionary where the keys are the movie titles and the values are lists containing the director, genre, rating, length, and notable actors for each movie
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'Movies_dictionary.csv')

database = {}
with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader, None)

    for row in reader:
        title = row[0].strip()
        director = row[1].strip()
        genre = row[2].strip()
        rating = row[3].strip()
        length = row[4].strip()
        notable_actors = row[5].strip()

        # directors and notable actors can be comma-separated lists (some CSV cells are quoted)
        directors_list = [d.strip() for d in director.split(",")]
        actors_list = [a.strip() for a in notable_actors.split(",")]

        try:
            length_int = int(length)
        except ValueError:
            length_int = -1

        database[title] = [directors_list, genre, rating, length_int, actors_list]

# introduction
print("Welcome to the Movie Recommender!")
print("You can search for movies based on Title, Director, Genre, Rating, Length, or Notable Actors.")

# while true:
while True:
    print("would you like to search for a movie or print the entire database?")
    user_choice = input("Enter 'search' to search for a movie or 'print' to print the entire database: ")

    if user_choice.lower() == "print":
        for title, info in database.items():
            print(f"Title: {title}")
            print(f"Director: {', '.join(info[0])}")
            print(f"Genre: {info[1]}")
            print(f"Rating: {info[2]}")
            print(f"Length: {info[3]}")
            print(f"Notable Actors: {', '.join(info[4])}")
            print()
        continue

    elif user_choice.lower() != "search":
        print("Invalid choice. Please enter 'search' or 'print'.")
        continue

    if user_choice.lower() == "search":
        # ask user if they are selecting Title,Director,Genre,Rating,Length, or Notable Actors
        display_search_types = ["Title", "Director", "Genre", "Rating", "Minimum Length", "Notable Actors"]

        # ask user to input the specific title, director, genre, rating, length, or notable actor
        filters = []
        for search_type in display_search_types:
            user_input = input(f"Enter the {search_type} you are looking for (or leave blank to skip): ").strip()
            if user_input == "":
                user_input = "NON APPLICABLE"
            filters.append(user_input)

        matching_movies = []

        for title, info in database.items():
            directors, genre, rating, length_int, actors = info
            # search through the movie database and find movies that match the user's input
            ok = True

            def title_check():
                if filters[0] != "NON APPLICABLE":
                    if filters[0].lower() not in title.lower():
                        return False
                return True

            def director_check():
                if filters[1] != "NON APPLICABLE":
                    if not any(filters[1].lower() in d.lower() for d in directors):
                        return False
                return True

            def genre_check():
                if filters[2] != "NON APPLICABLE":
                    if filters[2].lower() not in genre.lower():
                        return False
                return True

            def rating_check():
                if filters[3] != "NON APPLICABLE":
                    if filters[3].lower() not in rating.lower():
                        return False
                return True

            def min_length_check():
                if filters[4] != "NON APPLICABLE":
                    try:
                        min_length = int(filters[4])
                        if length_int < min_length:
                            return False
                    except ValueError:
                        print(f"Invalid minimum length: {filters[4]}. Skipping length filter.")
                return True

            def actors_check():
                if filters[5] != "NON APPLICABLE":
                    if not any(filters[5].lower() in a.lower() for a in actors):
                        return False
                return True

            def all_checks():
                return all([
                    title_check(),
                    director_check(),
                    genre_check(),
                    rating_check(),
                    min_length_check(),
                    actors_check()
                ])

            if all_checks():
                matching_movies.append(title)

    # display the matching movies to the user
    if matching_movies:
        print("Matching movies:")
        for movie in matching_movies:
            print(movie)

        print("would you like to select one of these movies to see more information about it?")
        movie_choice = input("(y/n): ")
        if movie_choice.lower() == "y":
            print("Which movie would you like to see more information about?")
            selected_movie = input("Enter the movie title: ").strip().capitalize()
            if selected_movie in database:
                info = database[selected_movie]
                print(f"Title: {selected_movie}")
                print(f"Director: {', '.join(info[0])}")
                print(f"Genre: {info[1]}")
                print(f"Rating: {info[2]}")
                print(f"Length: {info[3]}")
                print(f"Notable Actors: {', '.join(info[4])}")
            else:
                print("Movie not found in the database.")
    else:
        print("No matching movies found.")