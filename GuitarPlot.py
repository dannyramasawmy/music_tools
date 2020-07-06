# -*- coding: utf-8 -*-
"""
    %GUITARPLOT Class definition for guitar plot.
    %
    % DESCRIPTION
    %   Plots the chord or scale.
    %
    % USAGE
    %   Initialise with a GuitarScale object as a list.
    %   GuitarPlot.GuitarPlot([guitar_scale_object])
    %
    % ATTRIBUTES
    %
    % METHODS
    %
    % DEPENDENCIES
    %
    % ABOUT
    %    author      :   Danny Ramasawmy
    %                :   Irina Grigorescu
    %    contact     :   dannyramasawmy@gmail.com
    %    date        :   31 - July      - 2019
    %    last edit   :   31 - December  - 2020
"""

# import numpy and pyplot for doing vector maths and plotting
import numpy as np
import matplotlib.pyplot as plt

class GuitarPlot:
    def __init__(self, guitar_scales):
        """
        Initialise the GuitarPlot object.
        :param guitar_scales
        """
        
        # initalise GuitarPlot class properties
        # GuitarScalce object
        scales      = []
        # name of the GuitarPlot object
        name        = []   
        # colour of the GuitarPlot object
        colour       = []
        # starting fret to plot
        self.start_fret  = -0.5;                    
        # last fret to plot
        self.end_fret    = 7.5;                     
        # the number of GuitarScale object
        self.n_scales    = 0.5;
        # tuning of the guitar
        self.tuning      = ['E','A','D','G','B','E'];
        
        # assign fret boards and names
        for idx in range(len(guitar_scales)):
            scales.append(guitar_scales[idx].getFretMask())
            name.append(guitar_scales[idx].getName())
            colour.append(guitar_scales[idx].getColour())
        
        self.scales = scales
        self.name = name
        self.colour = colour
        self.len  = len(guitar_scales)
        
    def __repr__(self):
        """
        Prints the important information.
        """
        print(self.start_fret)
        print(self.end_fret)
        print(self.tuning)
        print(self.name)
        return "GuitarPlot"
    
    def setStartFret(self,f_start,f_end = 0):
        """
            SETSTARTFRET The fret range to display
        """ 
        
        if f_start == 0:
            self.start_fret = -0.5
            
        # assign sart fret
        self.start_fret = f_start
        
        # assign end fret if no input given
        if f_end == 0:
            self.end_fret = round(self.start_fret) + 6
        else:
            self.end_fret = round(f_end)
                
        # add 0.5 so numbers appear in the middle of fret    
        self.start_fret = self.start_fret + 0.5;
        self.end_fret = self.end_fret + 0.5;
        
        
    def plot(self):
        """
        Plots the position of the chosen frets
        """
        
        # meshgrid for guitar neck
        tvec  = np.linspace(0, 24, 25) + 0.5
        tvec2 = np.linspace(0,  5, 6)
        X, Z = np.meshgrid(tvec2, tvec)
        
        # Figure size
        plt.figure(figsize=(4, 5.5))

        # plot fretboard grid
        plt.plot(X, Z, 'k', X.T, Z.T, 'k', zorder=0)
        
        # loop over each grid and plot the notes
        for idx in range(self.len):
            fret, string = self.scales[idx].nonzero()
            
            # add notes
            plt.scatter(string, fret, 
                        c=self.colour[idx], 
                        s=500/(idx**2+1), 
                        label=self.name[idx])
            
        # legend
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), 
                   loc='lower left',
                   ncol=2, 
                   mode="expand")
        # plot things nicely
        plt.ylim([self.start_fret, self.end_fret])
        plt.xticks([0,1,2,3,4,5], self.tuning)    
        plt.gca().invert_yaxis()
        # display the image    
        plt.show()
        
        
        
 
