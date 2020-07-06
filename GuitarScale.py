# -*- coding: utf-8 -*-
"""
    %GUITARSCALE Class definition for guitar scale.
    %
    % DESCRIPTION
    %   GuitarScale is a class to aid with plotting of scales, arpeggios
    %   and chord shapes for guitarists. This class contains the fret and
    %   string information and the class GuitarPlot plots the information
    %   contained in GuitarScale. 
    %
    % USAGE
    % Initialise the object with the name, the fret numbers on each string
    % and the colour.
    %     
    % In general:
    % object = GuitarScale('name', [f1,...,fn], [f1,...,fn], [f1,...,fn],
    %       [f1,...,fn], [f1,...,fn], [f1,...,fn], 'colour');
    %         
    % Example: create the a-minor scale from the 5th fret:
    % a_minor_scale = GuitarScale('a_minor_scale',...
    %       [5 7 8],[5 7 8],[5 7],[4 5 7],[5 6 8],[5 7 8],'k');
    %
    % Example: create the a-minor chord from the 0th fret:
    % a_minor_chord = GuitarScale('a_minor_chord',...
    %       -1, 0, 2, 2, 1, 0,'k');
    %   note: the low-E string is not played, to represent this set to any
    %   negative number.
    %
    % ATTRIBUTES
    %   fret_mask   :   A matrix of the dimensions [25 X 6] that only
    %                   contain 0's or 1's. When GuitarScale is initialised
    %                   this matrix is populated. On the fret and string
    %                   where the note is defined the matrix will contain a
    %                   1, otherwise it will contain a zero.
    %   name        :   A string type, of the name of the
    %                   scale/chord/arpeggio etc. When the class GuitarPlot
    %                   is used, the name will be plotted above the
    %                   relevant diagram.
    %   colour      :   A string type which must be a valid MATLAB
    %                   colour argument. When the class GuitarPlot is used
    %                   the colour specified here will be used. Some valid
    %                   arguments:
    %                       'r'     -   red
    %                       'k;     -   black
    %                       'g'     -   green
    %                       'b'     -   blue
    %                       'y'     -   yellow
    %                       'm'     -   magenta
    %                   The default argument is 'k'.
    %
    % METHODS
    %
    %
    %
    % DEPENDENCIES
    %   Python3 and numpy and matlpotlib
    %
    % ABOUT
    %    author      :   Danny Ramasawmy
    %    contact     :   dannyramasawmy@gmail.com
    %    date        :   31 - July      - 2019
    %    last edit   :   30 - December   - 2019
"""

# import numpy and pyplot for doing vector maths and plotting
import numpy as np
import matplotlib.pyplot as plt


class GuitarScale:
    def __init__(self, name = "gs", nts_s1 = 0, nts_s2 = 0, \
                 nts_s3 = 0, nts_s4 = 0, nts_s5 = 0, \
                 nts_s6 = 0, colour = 'k'):
        '''
        Initialise the GuitarScale class.
        '''
        # initialise the class properties
        
        self.name       = name
        self.colour     = colour
    
        # convert to numpy array because python is annoying
        nts_s1 = np.array(nts_s1)
        nts_s2 = np.array(nts_s2)
        nts_s3 = np.array(nts_s3)
        nts_s4 = np.array(nts_s4)
        nts_s5 = np.array(nts_s5)
        nts_s6 = np.array(nts_s6)
    
        # check for negative (i.e. no strings)
        nts_s1 = nts_s1[nts_s1 > 0]
        nts_s2 = nts_s2[nts_s2 > 0]
        nts_s3 = nts_s3[nts_s3 > 0]
        nts_s4 = nts_s4[nts_s4 > 0]
        nts_s5 = nts_s5[nts_s5 > 0]
        nts_s6 = nts_s6[nts_s6 > 0]
    
        # find the correct frets
        nts_s1 = np.unique(np.round(nts_s1))
        nts_s2 = np.unique(np.round(nts_s2))
        nts_s3 = np.unique(np.round(nts_s3)) 
        nts_s4 = np.unique(np.round(nts_s4))
        nts_s5 = np.unique(np.round(nts_s5)) 
        nts_s6 = np.unique(np.round(nts_s6)) 
        
        # assign frets
        tmp = np.zeros([25, 6])
        tmp[nts_s1, 0] = 1;
        tmp[nts_s2, 1] = 1;
        tmp[nts_s3, 2] = 1;
        tmp[nts_s4, 3] = 1;
        tmp[nts_s5, 4] = 1;
        tmp[nts_s6, 5] = 1;
        
        # fret mask
        self.fret_mask  = tmp
        
    def __repr__(self):
        '''
        Prints the name of the fretboard mask and class.
        '''
        print('Fretboard Mask')
        print(self.fret_mask)
        return self.name
        
    
    def getFretMask(self):
        '''
        Returns the fretboard mask.
        '''
        return self.fret_mask
        
        
    def getName(self):
        """
        Returns the name of the object.
        """
        return self.name
     
    def getColour(self):
        """
        Returns the colour of the object.
        """
        return self.colour
        
        
    def rename(self, new_name):
        '''
        Rename the object.
        '''
        self.name = new_name
        



