"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-06-28"
-------------------------------------------------------
"""
# Imports
from Movie import Movie

# Constants

def test_movie_creation():
    # Test basic instantiation and __str__
    movie = Movie("Inception", 2010, "Christopher Nolan", 8.8, [0, 2])
    assert str(movie) == """Title:    Inception
Year:     2010
Director: Christopher Nolan
Rating:   8.8
Genres:   science fiction, drama"""

def test_movie_comparison():
    # Test comparison operators
    movie1 = Movie("Inception", 2010, "Christopher Nolan", 8.8, [0, 2])
    movie2 = Movie("Inception", 2010, "Christopher Nolan", 8.8, [0, 2])
    movie3 = Movie("Avatar", 2009, "James Cameron", 7.8, [0, 1])
    assert movie1 == movie2
    assert movie1 != movie3
    assert movie3 < movie1

def test_movie_genres_string():
    # Test genre string generation
    movie = Movie("The Matrix", 1999, "Lana Wachowski", 8.7, [0, 6])
    assert movie.genres_string() == "science fiction, action"

def test_movie_file_write():
    # Test writing to a file
    movie = Movie("The Matrix", 1999, "Lana Wachowski", 8.7, [0, 6])
    with open("test_movie_output.txt", "w") as file:
        movie.write(file)
    with open("test_movie_output.txt", "r") as file:
        data = file.read()
        expected_output = "The Matrix|1999|Lana Wachowski|8.7|0,6\n"
        assert data == expected_output

def run_tests():
    test_movie_creation()
    test_movie_comparison()
    test_movie_genres_string()
    test_movie_file_write()
    print("All tests passed!")
