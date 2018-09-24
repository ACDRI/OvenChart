import plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
from plotly.offline import *
import numpy as np 
import pandas as pd
import csv
import sys
import webbrowser
import time

#if this fails go back to v3

def go_time(total_list, csv_num):
    wo_title = "WO #: "
    for x in range(0, len(total_list)):
      if len(total_list) > 1 and x != (len(total_list) - 1):
        wo_title = wo_title + ' ' + total_list[x] + ', '
      else:
        wo_title = wo_title + ' ' + total_list[x]

    df = pd.read_csv(csv_num)
    df2= df['Date (MDY)'].values
    df3=" Ran on " + df2[1]
    df4= df['Time'].values
    df5= df4[1]
    df6 = len(df4)
    final_time = df4[df6-1] 
    mod = (len(df4) % 60)
    if mod != 0:
      mod -= 1
    
    div_dirty = df6 / 60
    div_clean = df6 // 60
    if ((div_dirty != div_clean) and (mod > 15)):
      here_it_is = [df4[x * 60] for x in range(0, div_clean + 1)] + [df4[(60 * div_clean) + mod]]
    else:
      here_it_is = [df4[x * 60] for x in range(0, div_clean + 1)]

    find_date = df2[1]
    csv_len = len(csv_num) - 1
    find_oven = csv_num[0:4]
    find_profile = csv_num[5:7]  


    y = 10
    z = ""
    my_tick = []
    for x in range(0, 101):
      y = 10 * x 
      if ((y % 100) == 0 or (y % 25) == 0):
        my_tick.append(str(y) + '\N{DEGREE SIGN}' + 'F')
      else:
        my_tick.append(str(""))

       

    trace1 = go.Scatter(
                    x=df['Time'], y=df['Process PV (Deg F)'], # Data
                    mode='lines', name='Oven Behavior' # Additional options
                   )

    layout = go.Layout(title=wo_title + ':  Initiated ' + find_date + ' at ' + df5 + ' with Oven ' + find_oven + ' using  Profile ' + find_profile,
                   titlefont=dict(family='Droid Sans', size = 15, color='#000'),
                   autosize=False,
                   width=1300,
                   height=1000,
                   plot_bgcolor='rgb(255, 255, 255)',
                   yaxis=dict (
                       title='TEMPERATURE',
                       ticks='inside',
                       ticklen=7.5,
                       tickwidth=3,
                       tickvals=[10 * x for x in range(0, 101)],
                       ticktext=my_tick,
                      # showticklabels= False,
                       tickfont=dict(
                        family='Arial, sans-serif',
                        size = 12,
                        color='black'),
                        #tick0=0,
                        #dtick=20,
                       tickcolor='#000',
                       gridcolor='#C0C0C0',
                       linecolor='black',
                       linewidth=2,
                       mirror=True
                       ),
                   xaxis=dict (
                       title='TIME (24-HOUR)',
                      # titlefont=dict(
                       #    size = 12
                        #   ),
                       ticks='outside',
                       tickfont=dict(family='Arial, sans-serif', size = 11, color = 'black'),
                       tickwidth=3,
                       ticklen=7.5,
                       # tick0=df5,
                       # dtick=60,
                       tickvals= here_it_is,
                      # tickvals= [df4[x * 60] for x in range(0, div + 1)] + [df4[(60 * div) + mod]],
                       gridcolor='#C0C0C0',
                       linecolor='black',
                       linewidth=2,
                       mirror=True
                   )
    )


    fig = go.Figure(data=[trace1], layout=layout)

    # Plot data in the notebook
    py.offline.plot(fig, filename=csv_num, show_link=False)


