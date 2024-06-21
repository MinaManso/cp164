from mans3974_data_structures import Movie_utilities

def get_by_genre():
    """
    -------------------------------------------------------
    Tests Movie_utilities.get_by_genre.
    Use: get_by_genre()
    -------------------------------------------------------
    """
    movies = Movie_utilities.get_by_genre(1)
    for m in movies:
        print(m)
    
    return
