import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    df.info()

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,8))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color='blue')
    # Create first line of best fit
    lin1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    slope1 = lin1.slope
    intercept1 = lin1.intercept
    x_pred1 = np.arange(df["Year"].min(), 2051)
    y_pred1 = intercept1 + slope1 * x_pred1
    ax.plot(x_pred1, y_pred1, color='red', linewidth=2)

    # Create second line of best fit
    df_recentyears = df[df["Year"]> 1999]
    lin2 = linregress(df_recentyears["Year"], df_recentyears["CSIRO Adjusted Sea Level"])
    slope2 = lin2.slope
    intercept2 = lin2.intercept
    x_pred2 = np.arange(df_recentyears["Year"].min(), 2051)
    y_pred2 = intercept2 + slope2 * x_pred2
    ax.plot(x_pred2, y_pred2, color='green', linewidth=2)
    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.legend(["Sea level", "Predicted sea level", "Predicted sea level based on recent  years"])
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()