import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level")

    # Create first line of best fit
    slope, intercept, *kwargs = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred_all = range(1880, 2051)
    y_pred_all = slope * x_pred_all + intercept
    plt.plot(x_pred_all, y_pred_all, 'r', label='Fit line (all data)')
    
    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]

    slope_recent, intercept_recent, *kwargs = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_pred_recent = range(2000, 2051) 
    y_pred_recent = slope_recent * x_pred_recent + intercept_recent
    plt.plot(x_pred_recent, y_pred_recent, 'g', label='Fit line (2000 onward)')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')

    plt.show()

    return plt.gca()
