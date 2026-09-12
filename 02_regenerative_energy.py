# ============================================================
# EERS - PROGRAM 02
# Regenerative Energy Recovery Simulation
# ============================================================

print("=" * 60)
print("     EERS - REGENERATIVE ENERGY RECOVERY")
print("=" * 60)

# ------------------------------------------------------------
# MAIN BATTERY
# ------------------------------------------------------------

main_battery_capacity = 100.0       # Wh
main_battery_soc = 70.0              # %

# ------------------------------------------------------------
# EMERGENCY BATTERY
# ------------------------------------------------------------

emergency_battery_capacity = 50.0    # Wh
emergency_battery_soc = 20.0         # %

# ------------------------------------------------------------
# VEHICLE PARAMETERS
# ------------------------------------------------------------

vehicle_mass = 20.0                  # kg
regeneration_efficiency = 0.70       # 70%

# ------------------------------------------------------------
# DISPLAY INITIAL STATUS
# ------------------------------------------------------------

print("\nINITIAL BATTERY STATUS")
print("-" * 60)

print(f"Main Battery      : {main_battery_soc:.2f}%")
print(f"Emergency Battery : {emergency_battery_soc:.2f}%")

print("\nREGENERATIVE BRAKING SIMULATION")
print("-" * 60)

# ------------------------------------------------------------
# SIMULATE DIFFERENT BRAKING EVENTS
# ------------------------------------------------------------

braking_speeds = [20, 30, 40, 25, 35]   # km/h

total_recovered_energy = 0.0

for event, speed_kmh in enumerate(braking_speeds, start=1):

    # Convert km/h to m/s
    speed_ms = speed_kmh / 3.6

    # Kinetic energy:
    # E = 1/2 * m * v^2
    kinetic_energy = 0.5 * vehicle_mass * speed_ms ** 2

    # Convert Joules to Wh
    kinetic_energy_wh = kinetic_energy / 3600

    # Recover only part of the kinetic energy
    recovered_energy = (
        kinetic_energy_wh * regeneration_efficiency
    )

    total_recovered_energy += recovered_energy

    # Convert recovered energy to emergency battery SOC
    soc_increase = (
        recovered_energy / emergency_battery_capacity
    ) * 100

    emergency_battery_soc += soc_increase

    # Limit battery SOC to 100%
    if emergency_battery_soc > 100:
        emergency_battery_soc = 100

    print(
        f"Brake Event {event}: "
        f"Speed = {speed_kmh:02d} km/h | "
        f"Recovered = {recovered_energy:.3f} Wh | "
        f"Emergency SOC = {emergency_battery_soc:.2f}%"
    )

# ------------------------------------------------------------
# FINAL RESULTS
# ------------------------------------------------------------

print("\n" + "-" * 60)
print("SIMULATION COMPLETED")
print("-" * 60)

print(f"Total Recovered Energy : {total_recovered_energy:.3f} Wh")
print(f"Final Emergency SOC    : {emergency_battery_soc:.2f}%")

# ------------------------------------------------------------
# BATTERY STATUS
# ------------------------------------------------------------

if emergency_battery_soc >= 80:
    status = "READY"

elif emergency_battery_soc >= 50:
    status = "AVAILABLE"

elif emergency_battery_soc >= 20:
    status = "LOW"

else:
    status = "CRITICAL"

print(f"Emergency Battery Status : {status}")

print("=" * 60)
print("EERS PROGRAM 02 FINISHED")
print("=" * 60)