import numpy as np
from scipy.optimize import root
import matplotlib.pyplot as plt
from modelDefinition import modelEquations


# Fixed parameters
yieldstress= 100.0
viscosity  = 1.0
penaltyfluidity= 1e-3
maxterm = 0
# Outer loop over c
shearrate_range = np.logspace(3, -4, 200)   # finer grid for smoother line
stressSolution = []
x0=[0.01]

for shearrate in shearrate_range:
    sol = root(modelEquations, x0, args=(yieldstress, viscosity, penaltyfluidity, shearrate))
    if sol.success:
        stressSolution.append(sol.x)
        x0 = sol.x  +1.0# use the current solution as the next initial guess
    else:
        print(f"Root finding failed for shearrate={shearrate}")

# Convert to arrays for plotting
# shearrate_range = np.array([pair[0] for pair in stressSolution])
x_array = np.array(stressSolution)
viscosity_function = x_array.squeeze() / shearrate_range.squeeze()

# Plot
plt.plot(shearrate_range, x_array, 'b-', label='solution x(c)')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Shear Rate")
plt.ylabel("solution x")
plt.title("Stress vs Shear Rate")
plt.legend()
plt.grid(True)
plt.savefig("results.png", dpi=300, bbox_inches="tight")
plt.close()

plt.plot(shearrate_range, viscosity_function, 'b-', label='viscosity')
plt.xlabel("Shear Rate")
plt.ylabel("Viscosity function")
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.savefig("resultsviscosity.png", dpi=300, bbox_inches="tight")
plt.close()


