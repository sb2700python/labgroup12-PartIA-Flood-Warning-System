import datetime
import numpy as np
from floodsystem.analysis import polyfit 

def test_polyfit():
    # Generate mock data
    dates = [datetime.datetime(2024, 2, 1) + datetime.timedelta(days=i) for i in range(10)]
    levels = [15, 18, 20, 25, 28, 30, 22, 19, 21, 24]
    degree_of_polynomial = 2

    try:
        
        poly_function, time_shift = polyfit(dates, levels, degree_of_polynomial)

        # Check if the returned poly_function is a numpy poly1d object
        assert isinstance(poly_function, np.poly1d)

        # Check if the time_shift is a datetime object
        assert isinstance(time_shift, float)

    except Exception as e:
        # If any exception occurs, fail the test and print the exception
        assert False, f"Exception occurred: {e}"


