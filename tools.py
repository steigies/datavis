import numpy as np
import pandas as pd
#import sys

def cutoff(year=2000):
    #Planet = pd.read_csv(filename)
    Planet = pd.read_csv("cutoff/Planet/" +str(year) + "/Planet.csv")
    
    PlanetLat = Planet["Latitude"]
    PlanetLong = Planet["Longitude"]
    PlanetR = Planet["Rc"]

    PlanetLat = np.array([PlanetLat])
    PlanetLong = np.array([PlanetLong])
    PlanetR = np.array([PlanetR])

    PlanetLat = np.ndarray.flatten(PlanetLat)
    PlanetLong = np.ndarray.flatten(PlanetLong)
    PlanetR = np.ndarray.flatten(PlanetR)

    PlanetDf = pd.DataFrame({'x':PlanetLong, 'y':PlanetLat, 'z':PlanetR})

    Z = PlanetDf.pivot_table(index='x', columns='y', values='z').T.values

    X_unique = np.sort(PlanetDf.x.unique())
    Y_unique = np.sort(PlanetDf.y.unique())
    X, Y = np.meshgrid(X_unique, Y_unique)

    return(X, Y, Z)

