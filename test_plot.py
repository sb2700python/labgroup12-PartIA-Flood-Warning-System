import datetime

from floodsystem.plot import plot_water_levels
from floodsystem.plot import plot_water_level_with_fit

def test_plot_water_levels():

    # Mock Station object
    class MockStation:
        def __init__(self, name, typical_range=None):
            self.name = name
            self.typical_range = typical_range   
    
    # Test if typical range in NONE
    station = MockStation("Test Station")
    dates = [datetime.datetime(2024, 2, 1) + datetime.timedelta(days=i) for i in range(10)]
    levels = [15, 18, 20, 25, 28, 30, 22, 19, 21, 24]
    try:
        plot_water_levels(station, dates, levels)
    except Exception as e:
        assert False, f"Exception occurred: {e}"
        
def test_plot_water_level_with_fit():
    # Mock Station object
    class MockStation:
        def __init__(self, name, typical_range=None):
            self.name = name
            self.typical_range = typical_range   
    
    # Test if typical range in NONE
    station = MockStation("Test Station")
    dates = [datetime.datetime(2024, 2, 1) + datetime.timedelta(days=i) for i in range(10)]
    levels = [15, 18, 20, 25, 28, 30, 22, 19, 21, 24]
    try:
        plot_water_level_with_fit(station, dates, levels,4)
    except Exception as e:
        assert False, f"Exception occurred: {e}"   