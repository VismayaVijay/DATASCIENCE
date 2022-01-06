#plotly1

import plotly 
import plotly.graph_objs as go
import numpy as np
N=1000
random_x=np.linspace(0,1,N)
random_y0=np.random.randn(N)+5
random_y1=np.random.randn(N)
random_y2=np.random.randn(N)-5
trace0=go.Scatter(
    x=random_x,
    y=random_y0,
    mode='markers',
    name='markers'
    )

trace1=go.Scatter(
    x=random_x,
    y=random_y1,
    mode='lines+markers',
    name='lines+markers'
    )

trace2=go.Scatter(
    x=random_x,
    y=random_y2,
    mode='lines',
    name='lines'
    )


data=[trace0,trace1,trace2]
plotly.offline.plot(data,filename='scatter-mode')