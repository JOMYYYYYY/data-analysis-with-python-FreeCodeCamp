import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Sea Level Data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    line1 = [slope * x + intercept for x in range(1880, 2051)]
    plt.plot(range(1880, 2051), line1, label='Line of Best Fit (1880-2050)', color='orange')

    # Create second line of best fit (from 2000 to the most recent year)
    recent_data = data[data['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    line2 = [slope * x + intercept for x in range(2000, 2051)]
    plt.plot(range(2000, 2051), line2, label='Line of Best Fit (2000-2050)', color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
