#

from bokeh.plotting import figure
from bokeh.plotting import output_notebook
from bokeh.plotting import show

output_notebook()

p = figure(width = 500, height = 500)

p.square([1,2,3,4,5,], [6,7,2,4,5],
             size = 14,color = "olive", alpha=0.5)
show (p)