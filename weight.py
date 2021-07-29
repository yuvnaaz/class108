import plotly.figure_factory as ff
import pandas as pd 
import csv
df = pd.read_csv('108.csv')
fig = ff.create_distplot([df['Weight(Pounds)'].tolist()],['Height(Inches)'], show_hist = False)
fig.show()

