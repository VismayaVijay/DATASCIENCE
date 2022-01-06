#to create scatter circle markers

from bokeh.plotting import figure as fig
from bokeh.plotting import output_file as ON
from bokeh.plotting import show
ON("go.html")

plot1 = fig(plot_width = 500, plot_height = 500,title = "Scatter Markers")

plot1.circle([1,2,3,4,5,6], [2,1,6,8,0],
             size = 12,color = "green", alpha = 1)
show (plot1)