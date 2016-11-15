
import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly


dagmc_data = go.Bar(x = ['FNG','ATR','UWNR'],
                    y = [22769.33,8627.80,69429.60],
                    name = 'DAG-MCNP5')
native_data = go.Bar(x = ['FNG','ATR','UWNR'],
                    y = [5871.92,901.68,8767.29],
                    name = 'MCNP5')
data = [native_data,dagmc_data]
layout = go.Layout(barmode='group',
                   yaxis = dict(title = "Runtime (min)"))
fig = go.Figure(data=data,layout=layout)
py.plot(fig,filename="fng_performance_plot.html",auto_open=False)

