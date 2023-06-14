import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
  
    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    res = linregress(x, y)
    x_best_fit = pd.Series([year for year in range(1880, 2051)])
    y_best_fit = res.slope * x_best_fit + res.intercept
    plt.plot(x_best_fit, y_best_fit, 'r')
  
    # Create second line of best fit
    new_df = df.loc[df["Year"] >= 2000]
    new_x = new_df["Year"]
    new_y = new_df["CSIRO Adjusted Sea Level"]
    res2 = linregress(new_x, new_y)
    x_best_fit_2 = pd.Series([year for year in range(2000, 2051)])
    y_best_fit_2 = res2.slope * x_best_fit_2 + res2.intercept
    plt.plot(x_best_fit_2, y_best_fit_2)

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
