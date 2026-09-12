# ============================================================
# EERS - PROGRAM 03
# Emergency Energy Management System
# ============================================================

print("=" * 65)
print("       EERS - EMERGENCY ENERGY MANAGEMENT")
print("=" * 65)

# ------------------------------------------------------------
# BATTERY PARAMETERS
# ------------------------------------------------------------

main_battery_capacity = 100.0       # Wh
emergency_battery_capacity = 50.0   # Wh

main_battery_soc = 100.0
emergency_battery_soc = 40.0

# ------------------------------------------------------------
# VEHICLE PARAMETERS
# ------------------------------------------------------------

vehicle_power = 30.0                # Watts
simulation_time = 20                # minutes

# Emergency activation limit
emergency_limit = 15.0              # %

# ------------------------------------------------------------
# INITIAL STATUS
# ------------------------------------------------------------

print("\nINITIAL SYSTEM STATUS")
print("-" * 65)

print(f"Main Battery SOC      : {main_battery_soc:.2f}%")
print(f"Emergency Battery SOC : {emergency_battery_soc:.2f}%")
print(f"Vehicle Power         : {vehicle_power:.2f} W")

print("\nSYSTEM SIMULATION STARTED")
print("-" * 65)

# ------------------------------------------------------------
# SIMULATION
# ------------------------------------------------------------

for minute in range(1, simulation_time + 1):

    # Energy consumed during one minute
    energy_used = vehicle_power / 60

    # Main battery SOC reduction
    main_soc_reduction = (
        energy_used / main_battery_capacity
    ) * 100

    # Reduce main battery
    main_battery_soc -= main_soc_reduction

    if main_battery_soc < 0:
        main_battery_soc = 0

    # --------------------------------------------------------
    # DETERMINE BATTERY CONDITION
    # --------------------------------------------------------

    if main_battery_soc > 50:
        status = "NORMAL"

    elif main_battery_soc > 30:
        status = "LOW"

    elif main_battery_soc > emergency_limit:
        status = "CRITICAL"

    else:
        status = "EMERGENCY"

    # --------------------------------------------------------
    # EMERGENCY BATTERY DECISION
    # --------------------------------------------------------

    emergency_active = False

    if main_battery_soc <= emergency_limit:

        if emergency_battery_soc > 0:

            emergency_active = True

            # Emergency battery supplies vehicle power
            emergency_energy_used = vehicle_power / 60

            emergency_soc_reduction = (
                emergency_energy_used /
                emergency_battery_capacity
            ) * 100

            emergency_battery_soc -= emergency_soc_reduction

            if emergency_battery_soc < 0:
                emergency_battery_soc = 0

    # --------------------------------------------------------
    # DISPLAY SYSTEM STATUS
    # --------------------------------------------------------

    if emergency_active:
        power_source = "EMERGENCY BATTERY"

    else:
        power_source = "MAIN BATTERY"

    print(
        f"Time: {minute:02d} min | "
        f"Main SOC: {main_battery_soc:6.2f}% | "
        f"Emergency SOC: {emergency_battery_soc:6.2f}% | "
        f"Status: {status:9s} | "
        f"Source: {power_source}"
    )

# ------------------------------------------------------------
# FINAL RESULTS
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("                 FINAL RESULTS")
print("=" * 65)

print(f"Initial Main Battery SOC      : 100.00%")
print(f"Final Main Battery SOC        : {main_battery_soc:.2f}%")

print(f"Initial Emergency Battery SOC : 40.00%")
print(f"Final Emergency Battery SOC   : {emergency_battery_soc:.2f}%")

print(f"Final Main Battery Status     : {status}")

# ------------------------------------------------------------
# FINAL DECISION
# ------------------------------------------------------------

print("\nAI ENERGY MANAGEMENT DECISION")
print("-" * 65)

if main_battery_soc > 50:

    print("DECISION : NORMAL OPERATION")
    print("ACTION   : Continue using main battery.")

elif main_battery_soc > 30:

    print("DECISION : ENERGY SAVING")
    print("ACTION   : Reduce unnecessary energy consumption.")

elif main_battery_soc > emergency_limit:

    print("DECISION : CRITICAL BATTERY")
    print("ACTION   : Prepare emergency battery.")

else:

    if emergency_battery_soc > 0:

        print("DECISION : EMERGENCY BACKUP")
        print("ACTION   : Emergency battery available.")

    else:

        print("DECISION : NO BACKUP ENERGY")
        print("ACTION   : Vehicle should stop safely.")

print("=" * 65)
print("EERS PROGRAM 03 FINISHED")
print("=" * 65)
