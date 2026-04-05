import numpy as np


def modelEquations(x, yieldstress, viscosity, penaltyfluidity,shearrate):

    shearstress = x[0]
    stressmagnitude = np.abs(shearstress)
    if (stressmagnitude - yieldstress) > 0.0:
        maxterm = (stressmagnitude - yieldstress)/viscosity
        maxterm = maxterm/stressmagnitude + penaltyfluidity
    else:
        maxterm = penaltyfluidity
    # print(f"maxterm={maxterm}, shearrate={shearrate}, shearstress={shearstress}")
    return shearstress - shearrate/maxterm
