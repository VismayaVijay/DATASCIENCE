#psegments and rays

from bokeh.plotting import figure
from bokeh.plotting import output_file
from bokeh.plotting import show


output_file("segment.html")
f= figure(width=400,height=400)


f.segment(x0=[1,2,3],y0=[1,2,3],x1=[1.2,2.4,3.1],
          y1=[1.2,2.5,3.7],
          color="#F4A582", line_width=3)
show(f)