import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Import data
df = pd.read_csv('medical_examination.csv')

# 2 Add an overweight column to data --> Calculate BMI = weight/height 
df['overweight'] = None

# 3 Normalize 'cholesterol' and 'glucose' so 0 = good value and 1 = bad value


# 4 Drawing the categorical plot 
def draw_cat_plot():
    # 5 Create the DataFrame
    df_cat = None


    # 6 Formatting the data
    df_cat = None
    

    # 7 Draw the catplot



    # 8 Fig for output
    fig = None


    # 9 Save the fig
    fig.savefig('catplot.png')
    return fig


# 10 Drawing Heat map 
def draw_heat_map():
    # 11 Clean the data
    df_heat = None

    # 12 Calculate the corr. matrix
    corr = None

    # 13 Create a mask for upper triangle
    mask = None



    # 14 Matplot fig
    fig, ax = None

    # 15 Draw the heatmap



    # 16 Save the fig
    fig.savefig('heatmap.png')
    return fig
