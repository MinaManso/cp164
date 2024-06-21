from mans3974_data_structures import Movie_utilities

def test_get_by_year():
    """
    -------------------------------------------------------
    Tests Movie_utilities.get_by_year.
    Use: test_get_by_year()
    -------------------------------------------------------
    """
    test_years = [1999, 2001, 2020, 1980]  # Including a year with expected zero results

    # Loop through each test year and apply the get_by_year function
    for year in test_years:
        print(f"Movies from the year {year}:")
        movies = Movie_utilities.get_by_year()
        if movies:
            for movie in movies:
                print(movie)
        else:
            print("No movies found for this year.")

