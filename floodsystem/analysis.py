import numpy as np
import matplotlib
def polyfit(dates, levels, p):
    """
    curve fitting for water level against time
    
    """
    dates=matplotlib.dates.date2num(dates)
    time_shift=dates[0]
    p_coeff = np.polyfit(dates-time_shift, levels, p)
    poly = np.poly1d(p_coeff)
    return poly,time_shift