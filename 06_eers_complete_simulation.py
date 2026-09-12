# ============================================================
# EERS - PROGRAM 06
# COMPLETE EERS SOFTWARE SIMULATION
# ============================================================

import random

print("=" * 70)
print("     AI-IoT BASED INTELLIGENT EMERGENCY ENERGY RECOVERY")
print("              COMPLETE EV SIMULATION")
print("=" * 70)

# ------------------------------------------------------------
# BATTERY PARAMETERS
# ------------------------------------------------------------

main_capacity = 100.0
emergency_capacity = 50.0

main_soc = 100.0
emergency_soc = 30.0

# ------------------------------------------------------------
# VEHICLE PARAMETERS
# ------------------------------------------------------------

vehicle_power = 30.0
regeneration_efficiency = 0.70

# ------------------------------------------------------------
# SIMULATION
# ------------------------------------------------------------

for minute in range(1, 31):

    # Random vehicle speed
    speed = random.randint(15, 45)

    # Random braking condition
    braking = random.choice([True, False])

    # --------------------------------------------------------
    # MAIN BATTERY CONSUMPTION
    # --------------------------------------------------------

    energy_used = vehicle_power / 60

    soc_loss = (
        energy_used / main_capacity
    ) * 100

    main_soc -= soc_loss

    if main_soc < 0:
        main_soc = 0

    # --------------------------------------------------------
    # REGENERATIVE ENERGY
    # --------------------------------------------------------

    recovered_energy = 0

    if braking:

        speed_ms = speed / 3.6

        mass = 20

        kinetic_energy = (
            0.5 * mass * speed_ms ** 2
        )

        kinetic_energy_wh = (
            kinetic_energy / 3600
        )

        recovered_energy = (
            kinetic_energy_wh *
            regeneration_efficiency
        )

        emergency_soc_gain = (
            recovered_energy /
            emergency_capacity
        ) * 100

        emergency_soc += emergency_soc_gain

        if emergency_soc > 100:
            emergency_soc = 100

    # --------------------------------------------------------
    # BATTERY STATUS
    # --------------------------------------------------------

    if main_soc > 50:

        status = "NORMAL"

    elif main_soc > 30:

        status = "LOW"

    elif main_soc > 15:

        status = "CRITICAL"

    else:

        status = "EMERGENCY"

    # --------------------------------------------------------
    # EMERGENCY BACKUP
    # --------------------------------------------------------

    emergency_active = False

    if main_soc <= 15:

        if emergency_soc > 0:

            emergency_active = True

            emergency_energy = vehicle_power / 60

            emergency_loss = (
                emergency_energy /
                emergency_capacity
            ) * 100

            emergency_soc -= emergency_loss

            if emergency_soc < 0:
                emergency_soc = 0

    # --------------------------------------------------------
    # DISPLAY
    # --------------------------------------------------------

    if emergency_active:

        power_source = "EMERGENCY"

    else:

        power_source = "MAIN"

    print(
        f"Time:{minute:02d} min | "
        f"Speed:{speed:02d} km/h | "
        f"Main:{main_soc:6.2f}% | "
        f"Emergency:{emergency_soc:6.2f}% | "
        f"Regen:{recovered_energy:.3f} Wh | "
        f"{status:9s} | "
        f"Power:{power_source}"
    )

# ------------------------------------------------------------
# FINAL RESULT
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("                 FINAL EERS RESULT")
print("=" * 70)

print(f"Main Battery SOC      : {main_soc:.2f}%")
print(f"Emergency Battery SOC : {emergency_soc:.2f}%")

print("\nSYSTEM FEATURES SIMULATED:")
print("1. Main battery monitoring")
print("2. Vehicle energy consumption")
print("3. Regenerative braking")
print("4. Emergency battery charging")
print("5. Battery condition detection")
print("6. Emergency backup activation")

print("\nEERS SOFTWARE SIMULATION COMPLETED")
print("=" * 70)