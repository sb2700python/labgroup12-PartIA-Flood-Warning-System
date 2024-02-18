import numpy as np
def polyfit(dates, levels, p):
    """
    curve fitting for water level against time
    
    """
    
    time_shift=dates[0]
    p_coeff = np.polyfit(dates-time_shift, levels, p)
    poly = np.poly1d(p_coeff)
    return poly,time_shift