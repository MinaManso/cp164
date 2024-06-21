from mans3974_data_structures import Movie_utilities

def test_get_by_rating():
    """
    -------------------------------------------------------
    Tests Movie_utilities.get_by_rating.
    Use: test_get_by_rating()
    -------------------------------------------------------
    """
    movies = Movie_utilities.get_by_rating(7.0)
    for m in movies:
        print(m)
    
    return