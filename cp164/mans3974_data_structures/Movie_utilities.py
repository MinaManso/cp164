"""
-------------------------------------------------------
Movie class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 B
__updated__ = "2021-01-12"
-------------------------------------------------------
"""
from mans3974_data_structures.Movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """

    #creates a movie object by requesting data from a user.

    #title
    title = input("Title: ")

    #year of release
    year = int(input("Year of release: "))

    #director
    director = input("Director: ")

    #rating

    rating = float(input("Rating: "))
    while rating < 0 or rating > 10:
        print("Error: rating must be between 0 and 10")
        rating = float(input("Rating: "))


    #genre
    genres = read_genres()

    genre_number = int(input("Enter a genre number (ENTER to Quit): "))



    movie = Movie(title, year, director, rating, genres)


    # Your code here

    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """

    #creates and returns a movie object from a line of formatted string data
    parts = line.strip().split('|')
    title, year, director, rating, genres = parts[0], int(parts[1]), parts[2], float(parts[3]), list(map(int, parts[4].split(',')))
    movie = Movie(title, year, director, rating, genres)
    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """

    #reads a file of string data into a list of movie objects

    movies = []
    for line in fv:
        movie = read_movie(line)
        movies.append(movie)
    return movies


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """
    #print genres
    genres_menu = Movie.genres_menu()
    print(genres_menu)
    selected_genres = []
    choice = input("Enter genre numbers separated by commas or ENTER to finish: ")
    while choice:
        genre_numbers = list(map(int, choice.split(',')))
        for num in genre_numbers:
            if 1 <= num <= len(Movie.GENRES):
                selected_genres.append(num)
            else:
                print("Invalid genre number")
        choice = input("Add more genres or ENTER to finish: ")
    return sorted(set(selected_genres))


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """
    for movie in movies:
        fv.write(f"{movie.title}|{movie.year}|{movie.director}|{movie.rating}|{','.join(map(str, movie.genres))}\n")

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    The original list of movies must be unchanged.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is
            year (list of Movie)
    -------------------------------------------------------
    """

    ymovies = [movie for movie in movies if movie.year == year]

    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    The original list of movies must be unchanged.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """

    rmovies = [movie for movie in movies if movie.rating >= rating]

    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    The original list of movies must be unchanged.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes
            genre (list of Movie)
    -------------------------------------------------------
    """

    gmovies = [movie for movie in movies if genre in movie.genres]

    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    The original list of movies must be unchanged.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """
    gmovies = [movie for movie in movies if all(g in movie.genres for g in genres)]

    # Your code here

    return gmovies


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    The original list of movies must be unchanged.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    counts = [0] * len(Movie.GENRES)
    for movie in movies:
        for genre in movie.genres:
            counts[genre - 1] += 1  # assuming genre codes are 1-based

    # Your code here

    return counts