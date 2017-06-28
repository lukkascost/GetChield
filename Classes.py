from __future__ import division
import numpy as np
import math as mt
from serial import Serial
import time
def load_archive(path,cast = None):
        """ 
        Reads a archive in path and return it.
        
        Returns: 
        R1: An list with each line of archive;
        
        Params:
        P1: Path of the archive;
        cast: Converts the value of each line to 'int' or 'float'.
        """
        archive = open(path)
        result_archive = []
        for line in archive:
                objectLine = line
                if cast == "int": objectLine = int(objectLine)
                if cast == "float": objectLine = int(objectLine)                
                result_archive.append(objectLine)
        return result_archive        
        
def distanceOfSignalPower(power,pd0=6.0,n=2.75):
        exp = ((pd0-float(power))/(10*n))
        distance = mt.pow(10,exp)
        return float(distance/100)
