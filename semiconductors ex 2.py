import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Data for the 10V Zener diode
temperature = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])  # Temperature in °C
Vz = np.array([10.48, 10.49, 10.52, 10.55, 10.58, 10.61, 10.64, 10.67, 10.7, 10.73, 10.75, 10.81])  # Breakdown voltage in V

# Reference temperature and breakdown voltage
T_ref = 25  # Reference temperature in °C
Vz_ref = 10.48  # Breakdown voltage at 25°C

# Linear regression: Vz(T) = Vz_ref + α(T - T_ref)
T_shifted = temperature - T_ref  # Shifted temperature values (T - 25)
Vz_shifted = Vz - Vz_ref  # Shifted voltage values (Vz - Vz_ref)

# Perform linear regression
slope_alpha, intercept_alpha, r_value_alpha, p_value_alpha, std_err_alpha = linregress(T_shifted, Vz_shifted)

# Alpha is the slope of the regression
alpha = slope_alpha  # Temperature coefficient in V/°C

# Plot the data and the regression line
plt.figure(figsize=(10, 6))
plt.plot(temperature, Vz, 'o', label="Observed Data", color='blue')
plt.plot(temperature, Vz_ref + alpha * (temperature - T_ref), '-', label=f"Linear Fit: $V_Z(T) = {Vz_ref:.2f} + {alpha:.4f}(T - {T_ref})$, α = {alpha:.4f} V/°C", color='orange')

# Add labels, title, and legend
plt.xlabel("Temperature (°C)", fontsize=14)
plt.ylabel("Zener Breakdown Voltage, $V_Z$ (V)", fontsize=14)
plt.title("Linear Fit for Temperature Dependence of Zener Breakdown Voltage", fontsize=16)
plt.legend(fontsize=12)

# Show the plot
plt.show()








# Data for the 4.3V Zener diode
temperature_4v3 = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75])  # Temperature in °C
Vz_4v3 = np.array([4.38, 4.37, 4.36, 4.35, 4.34, 4.33, 4.32, 4.32, 4.31, 4.3, 4.29])  # Breakdown voltage in V

# Reference temperature and breakdown voltage
T_ref_4v3 = 25  # Reference temperature in °C
Vz_ref_4v3 = 4.38  # Breakdown voltage at 25°C

# Linear regression: Vz(T) = Vz_ref + α(T - T_ref)
T_shifted_4v3 = temperature_4v3 - T_ref_4v3  # Shifted temperature values (T - 25)
Vz_shifted_4v3 = Vz_4v3 - Vz_ref_4v3  # Shifted voltage values (Vz - Vz_ref)

# Perform linear regression
slope_alpha_4v3, intercept_alpha_4v3, r_value_alpha_4v3, p_value_alpha_4v3, std_err_alpha_4v3 = linregress(T_shifted_4v3, Vz_shifted_4v3)

# Alpha is the slope of the regression
alpha_4v3 = slope_alpha_4v3  # Temperature coefficient in V/°C

# Plot the data and the regression line
plt.figure(figsize=(10, 6))
plt.plot(temperature_4v3, Vz_4v3, 'o', label="Observed Data", color='blue')
plt.plot(temperature_4v3, Vz_ref_4v3 + alpha_4v3 * (temperature_4v3 - T_ref_4v3), '-', 
         label=f"Linear Fit: $V_Z(T) = {Vz_ref_4v3:.2f} + {alpha_4v3:.4f}(T - {T_ref_4v3})$,α = {alpha_4v3:.4f} V/°C ", color='orange')

# Add labels, title, and legend
plt.xlabel("Temperature (°C)", fontsize=14)
plt.ylabel("Zener Breakdown Voltage, $V_Z$ (V)", fontsize=14)
plt.title("Linear Fit for Temperature Dependence of Zener Breakdown Voltage (4.3V)", fontsize=16)
plt.legend(fontsize=12)

# Show the plot
plt.show()

# Display the results
print(f"Temperature Coefficient (α) for 4.3V Zener Diode: {alpha_4v3:.4f} V/°C")
print(f"Goodness of Fit (R^2): {r_value_alpha_4v3**2:.4f}")

