# Test script

from GuitarPlot import GuitarPlot as gp
from GuitarScale import GuitarScale as gs


a_minor_scale = gs('a-minor-scale', 
                   [5, 7, 8], 
                   [5, 7, 8], 
                   [5, 7], 
                   [5, 7], 
                   [5, 6, 8], 
                   [5, 7, 8], 'k') 

a_minor_chord = gs('a-minor-chord', 
                   [5], 
                   [7], 
                   [7], 
                   [6], 
                   [5], 
                   [5], 'b') 

a_minor_arpeg = gs('a-minor-arp', 
                   [5, 8], 
                   [7], 
                   [5, 7], 
                   [5], 
                   [5, 8], 
                   [5, 8], 'r') 

x = gp([a_minor_scale, a_minor_chord, a_minor_arpeg])
x.setStartFret(f_start=4, f_end=9)
x.plot()
