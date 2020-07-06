# -*- coding: utf-8 -*-

import importlib
# importlib.reload(module)

import GuitarScale
import GuitarPlot

# create two guitar scale objects
gs1 = GuitarScale.GuitarScale('a',[5, 7, 8],[5, 7, 8],[5, 7, 9],[5, 7],[5, 6, 8],[5, 7, 8])
gs2 = GuitarScale.GuitarScale('c',-1,0,2,2,1,0)

# create a guitar plot object
gp = GuitarPlot.GuitarPlot([gs1,gs2])
gp.setStartFret(0,9)
gp.plot()

print('Reloaded GuitarTest.py')
