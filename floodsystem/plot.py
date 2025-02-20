# plot/plot_module.py

import matplotlib
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
import numpy as np

def plot_water_levels(station, dates, levels):
    """
    Display a plot of water level data against time for a station.

    """

    # Plot the water levels against time
    plt.plot(dates, levels, label='Water Level')

    # Add lines for typical low and high levels
    if hasattr(station, 'typical_range') and station.typical_range is not None:
        low_level, high_level = station.typical_range

        if low_level is not None:
            plt.axhline(y=low_level, color='r', linestyle='--', label='Typical Low Level')
        if high_level is not None:
            plt.axhline(y=high_level, color='g', linestyle='--', label='Typical High Level')



    # Labeling and title
    plt.xlabel('Time')
    plt.ylabel('Water Level')
    plt.title(f'Water Level Data for {station.name}')
    plt.legend()
    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    # Display the plot
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """
    Display a plot of water level data against time for a station with curve fitting.

    """
    # Curve fitting
    poly, d0= polyfit(dates,levels,p)
    
    # Plot curve produced
    x=matplotlib.dates.date2num(dates)

    plt.plot(dates, poly(x - d0), label='Curve Fitting',linestyle='--')
    
    # Plot the water levels against time
    plt.plot(dates, levels, label='Water Level')


    # Add lines for typical low and high levels
    if hasattr(station, 'typical_range') and station.typical_range is not None:
        low_level, high_level = station.typical_range

        if low_level is not None:
            plt.axhline(y=low_level, color='r', linestyle='--', label='Typical Low Level')
        if high_level is not None:
            plt.axhline(y=high_level, color='g', linestyle='--', label='Typical High Level')

    # Labeling and title
    plt.xlabel('Time')
    plt.ylabel('Water Level')
    plt.title(f'Water Level Data for {station.name}')
    plt.legend()
    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    # Display the plot
    plt.show()