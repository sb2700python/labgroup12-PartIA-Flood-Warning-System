import numpy as np
import matplotlib
import datetime

def polyfit(dates, levels, p):
    """
    curve fitting for water level against time
    
    """
    dates1=matplotlib.dates.date2num(dates)
    time_shift=dates1[0]
    p_coeff = np.polyfit(dates1-time_shift, levels, p)
    poly = np.poly1d(p_coeff)
    return poly,time_shift

def predict_highest_water_level(dates,levels,p,dt):
    poly, time_shift=polyfit(dates,levels,p)
    last_date=dates[-1]
    generated_dates=[last_date+datetime.timedelta(days=i/10) for i in range(1, 10*dt + 1)]
    generated_times=[matplotlib.dates.date2num(date)-time_shift for date in generated_dates]
    predicted_water_levels=poly(generated_times)
    return max(predicted_water_levels)