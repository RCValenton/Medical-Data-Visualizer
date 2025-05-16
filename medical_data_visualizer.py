import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Import data
df = pd.read_csv('medical_examination.csv')

# 2 Add an overweight column to data --> Calculate BMI = weight/height 
df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2)) > 25).astype(int) 

# 3 Normalize 'cholesterol' and 'glucose' so 0 = good value and 1 = bad value

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4 Drawing the categorical plot 
def draw_cat_plot():
    # 5 Create the DataFrame
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6 Formatting the data
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    
    # 7 Draw the catplot
    catplot = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat)

    # 8 Fig for output
    fig = catplot.fig

    # 9 Save the fig
    fig.savefig('catplot.png')
    return fig


# 10 Drawing Heat map 
def draw_heat_map():
    # 11 Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12 Calculate the corr. matrix
    corr = df_heat.corr()

    # 13 Create a mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14 Matplot fig
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15 Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, square=True, linewidths=0.5, cbar_kws={"shrink": 0.5})

    # 16 Save the fig
    fig.savefig('heatmap.png')
    return fig

