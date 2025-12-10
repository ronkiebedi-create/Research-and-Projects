import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Data from the experiment
Vi = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0,
               5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 8.94, 9.5, 10.0,
               10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5])
Iz = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0.25, 1.7, 2.95,
               5.78, 7.12, 8.59, 9.8, 11.34, 12.58, 14.08, 15.4, 16.88])

# Extracting the range where the current shoots up (linear region for regression)
Vi_linear = np.array([9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5])
Iz_linear = np.array([1.7, 2.95, 5.78, 7.12, 8.59, 9.8, 11.34, 12.58, 14.08, 15.4, 16.88])

# Performing linear regression on the linear region
slope, intercept, r_value, p_value, std_err = linregress(Iz_linear, Vi_linear)

# Error values for plotting
Vz_error = 0.005  # Voltage error in V
Iz_error = 0.005  # Current error in mA

# Slope is the resistance in kΩ since current is in mA
slope_kohms = slope  # Resistance in kΩ

# Observed breakdown voltage from regression
Vz_regression = intercept  # Breakdown voltage purely from regression

# Calculate observed average breakdown voltage using known R = 270 Ω
R_series = 270  # Series resistance in Ω
Vz_calculated = Vi_linear - R_series * Iz_linear / 1000  # Convert mA to A
Vz_average_with_r = np.mean(Vz_calculated)  # Average observed breakdown voltage

# Plotting the graph with multiple breakdown voltage interpretations
plt.figure(figsize=(12, 8))
plt.errorbar(Vi, Iz, xerr=Vz_error, yerr=Iz_error, fmt='o', label="Observed Data with Error Bars", color='blue', ecolor='gray', capsize=4)
plt.axvline(x=9.1, color='red', linestyle='--', label="Theoretical Breakdown Voltage ($V_Z = 9.1$ V)")
plt.axvline(x=Vz_regression, color='green', linestyle='--', label=f"Regression Breakdown Voltage ($V_Z = {Vz_regression:.3f}$ V)")
plt.axvline(x=Vz_average_with_r, color='purple', linestyle='--', label=f"Breakdown Voltage with $R = 270 \, \Omega$ ($V_Z = {Vz_average_with_r:.3f}$ V)")

# Adding the regression line
fit_line = slope * Iz_linear + intercept
plt.plot(fit_line, Iz_linear, color='orange', label=f"Linear Fit: $V_i = {slope_kohms:.3f} \,k\Omega \cdot I_Z + {intercept:.3f}$")

# Adding labels, grid, and title
plt.xlabel("Input Voltage, $V_i$ (V)", fontsize=16)
plt.ylabel("Current through Zener Diode, $I_Z$ (mA)", fontsize=16)
plt.title("Zener Diode I-V Characteristics with Multiple $V_Z$ Interpretations", fontsize=18)
plt.legend(fontsize=10)

# Displaying the plot
plt.show()

# Printing results
print(f"Breakdown Voltage purely from Regression (Intercept): {Vz_regression:.3f} V")
print(f"Breakdown Voltage using Regression and R = 270 Ω: {Vz_average_with_r:.3f} V")
print(f"Linear Fit Slope (Resistance R): {slope_kohms:.3f} kΩ")
print(f"Goodness of Fit (R^2): {r_value**2:.3f}")












import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# New data for the 2.7V Zener diode breakdown
Vi_new = np.array([0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 
                   2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 
                   5.0, 5.2, 5.4, 5.6, 5.8, 6.0])
Iz_new = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.69, 
                   1.31, 1.71, 2.07, 2.49, 2.99, 3.46, 3.83, 4.47, 4.88, 5.3, 
                   5.79, 6.35, 6.81, 7.35, 7.84, 8.4, 9.04, 9.52])

# Extracting the linear region for regression
Vi_linear_new = np.array([ 2.4, 
                   2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 
                   5.0, 5.2, 5.4, 5.6, 5.8, 6.0])
Iz_linear_new = np.array([0.69, 
                   1.31, 1.71, 2.07, 2.49, 2.99, 3.46, 3.83, 4.47, 4.88, 5.3, 
                   5.79, 6.35, 6.81, 7.35, 7.84, 8.4, 9.04, 9.52])

# Performing linear regression on the linear region
slope_new, intercept_new, r_value_new, p_value_new, std_err_new = linregress(Iz_linear_new, Vi_linear_new)

# Slope is the resistance in kΩ (current in mA)
slope_kohms_new = slope_new  # Resistance in kΩ

# Observed breakdown voltage from regression
Vz_regression_new = intercept_new  # Breakdown voltage purely from regression

# Calculate observed average breakdown voltage using known R = 270 Ω
Vz_calculated_new = Vi_linear_new - (270 * Iz_linear_new / 1000)  # Convert mA to A
Vz_average_with_r_new = np.mean(Vz_calculated_new)

# Plotting the graph with multiple breakdown voltage interpretations
plt.figure(figsize=(12, 8))
plt.errorbar(Vi_new, Iz_new, xerr=Vz_error, yerr=Iz_error, fmt='o', label="Observed Data with Error Bars", color='blue', ecolor='gray', capsize=4)
plt.axvline(x=2.7, color='red', linestyle='--', label="Theoretical Breakdown Voltage ($V_Z = 2.7$ V)")
plt.axvline(x=Vz_regression_new, color='green', linestyle='--', label=f"Regression Breakdown Voltage ($V_Z = {Vz_regression_new:.3f}$ V)")
plt.axvline(x=Vz_average_with_r_new, color='purple', linestyle='--', label=f"Breakdown Voltage with $R = 270 \, \Omega$ ($V_Z = {Vz_average_with_r_new:.3f}$ V)")

# Adding the regression line
fit_line_new = slope_new * Iz_linear_new + intercept_new
plt.plot(fit_line_new, Iz_linear_new, color='orange', label=f"Linear Fit: $V_i = {slope_kohms_new:.3f} \,k\Omega \cdot I_Z + {intercept_new:.3f}$")

# Adding labels, grid, and title
plt.xlabel("Input Voltage, $V_i$ (V)", fontsize=16)
plt.ylabel("Current through Zener Diode, $I_Z$ (mA)", fontsize=16)
plt.title("2.7V Zener Diode I-V Characteristics with Multiple $V_Z$ Interpretations", fontsize=18)
plt.legend(fontsize=10)

# Displaying the plot
plt.show()

# Printing results
print(f"Breakdown Voltage purely from Regression (Intercept): {Vz_regression_new:.3f} V")
print(f"Breakdown Voltage using Regression and R = 270 Ω: {Vz_average_with_r_new:.3f} V")
print(f"Linear Fit Slope (Resistance R): {slope_kohms_new:.3f} kΩ")
print(f"Goodness of Fit (R^2): {r_value_new**2:.3f}")
