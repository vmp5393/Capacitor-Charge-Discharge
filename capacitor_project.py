import numpy as np
import matplotlib.pyplot as plt

def capacitor_voltage(t, voltage_max, R, C, charge=True):
    if charge:
        return voltage_max * (1 - np.exp(-t / (R * C)))
    else:
        return voltage_max * np.exp(-t / (R * C)) 

voltage_max = 5  
res_vals = [1e3, 10e3] 
cap_vals = [1e-6, 10e-6]  
time = np.linspace(0, 0.1, 1000) 

plt.figure(figsize=(10, 5))

for R in res_vals:
    for C in cap_vals:
        v_charge = capacitor_voltage(time, voltage_max, R, C, charge=True)
        v_discharge = capacitor_voltage(time, voltage_max, R, C, charge=False)
        label_text = f"R={R/1e3}kΩ, C={C*1e6}µF"
        
        plt.plot(time, v_charge, label=f"Charging ({label_text})")
        plt.plot(time, v_discharge, '--', label=f"Discharging ({label_text})")

plt.xlabel("Time (s)")
plt.ylabel("Capacitor Voltage (V)")
plt.title("Charging and Discharging of a Capacitor in an RC Circuit")
plt.legend()
plt.grid()
plt.show()