# AI-IoT Based Intelligent Emergency Energy Recovery System
# EERS - Program 01
# Battery and EV Energy Simulation

battery_capacity = 100.0      # Wh
battery_soc = 100.0           # Percentage

vehicle_power = 30.0          # Watts
simulation_time = 30          # minutes

print("======================================")
print("       EERS BATTERY SIMULATION")
print("======================================")

print(f"Battery Capacity : {battery_capacity} Wh")
print(f"Initial SOC      : {battery_soc}%")
print(f"Vehicle Power    : {vehicle_power} W")
print("--------------------------------------")

for minute in range(1, simulation_time + 1):

    # Energy consumed during one minute
    energy_used = vehicle_power / 60

    # SOC reduction
    soc_reduction = (energy_used / battery_capacity) * 100

    battery_soc = battery_soc - soc_reduction

    if battery_soc < 0:
        battery_soc = 0

    print(
        f"Time: {minute:02d} min | "
        f"Battery SOC: {battery_soc:.2f}%"
    )

print("--------------------------------------")
print("Simulation completed.")
print(f"Final Battery SOC: {battery_soc:.2f}%")
print("======================================")