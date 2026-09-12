# ============================================================
# EERS - PROGRAM 07
# IoT Dashboard - Software Simulation
# ============================================================

import streamlit as st
import random
import time

# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------

st.set_page_config(
    page_title="EERS IoT Dashboard",
    page_icon="🔋",
    layout="wide"
)

# ------------------------------------------------------------
# TITLE
# ------------------------------------------------------------

st.title("🔋 EERS - Intelligent Emergency Energy Recovery System")

st.subheader(
    "AI + IoT Based Electric Vehicle Energy Management Dashboard"
)

st.write(
    "Software simulation of battery monitoring, "
    "regenerative energy recovery and emergency backup."
)

st.divider()

# ------------------------------------------------------------
# INITIAL VALUES
# ------------------------------------------------------------

if "main_soc" not in st.session_state:
    st.session_state.main_soc = 85.0

if "emergency_soc" not in st.session_state:
    st.session_state.emergency_soc = 40.0

if "total_recovered" not in st.session_state:
    st.session_state.total_recovered = 0.0

# ------------------------------------------------------------
# SIMULATE EV DATA
# ------------------------------------------------------------

vehicle_speed = random.randint(20, 60)

temperature = random.uniform(25, 40)

motor_power = random.uniform(20, 80)

braking = random.choice([True, False])

# ------------------------------------------------------------
# BATTERY CONSUMPTION
# ------------------------------------------------------------

energy_used = motor_power / 60

main_soc_loss = (energy_used / 100) * 100

st.session_state.main_soc -= main_soc_loss

if st.session_state.main_soc < 0:
    st.session_state.main_soc = 0

# ------------------------------------------------------------
# REGENERATIVE ENERGY
# ------------------------------------------------------------

recovered_energy = 0.0

if braking:

    recovered_energy = random.uniform(0.05, 0.5)

    st.session_state.total_recovered += recovered_energy

    emergency_gain = (
        recovered_energy / 50
    ) * 100

    st.session_state.emergency_soc += emergency_gain

    if st.session_state.emergency_soc > 100:
        st.session_state.emergency_soc = 100

# ------------------------------------------------------------
# AI BATTERY STATUS
# ------------------------------------------------------------

main_soc = st.session_state.main_soc

if main_soc > 50:

    ai_status = "NORMAL"
    ai_action = "Continue normal operation"

elif main_soc > 30:

    ai_status = "LOW"
    ai_action = "Enable energy-saving mode"

elif main_soc > 15:

    ai_status = "CRITICAL"
    ai_action = "Prepare emergency battery"

else:

    ai_status = "EMERGENCY"
    ai_action = "Activate emergency battery"

# ------------------------------------------------------------
# POWER SOURCE
# ------------------------------------------------------------

if ai_status == "EMERGENCY" and st.session_state.emergency_soc > 0:

    power_source = "EMERGENCY BATTERY"

else:

    power_source = "MAIN BATTERY"

# ------------------------------------------------------------
# DASHBOARD METRICS
# ------------------------------------------------------------

st.header("🚗 Live EV Parameters")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "🔋 Main Battery",
        f"{st.session_state.main_soc:.1f}%"
    )

with col2:

    st.metric(
        "🆘 Emergency Battery",
        f"{st.session_state.emergency_soc:.1f}%"
    )

with col3:

    st.metric(
        "⚡ Recovered Energy",
        f"{st.session_state.total_recovered:.2f} Wh"
    )

with col4:

    st.metric(
        "🚗 Vehicle Speed",
        f"{vehicle_speed} km/h"
    )

# ------------------------------------------------------------
# SECOND ROW
# ------------------------------------------------------------

st.divider()

col5, col6, col7, col8 = st.columns(4)

with col5:

    st.metric(
        "🌡️ Temperature",
        f"{temperature:.1f} °C"
    )

with col6:

    st.metric(
        "⚙️ Motor Power",
        f"{motor_power:.1f} W"
    )

with col7:

    if braking:
        st.metric(
            "🔄 Regenerative Braking",
            "ACTIVE"
        )
    else:
        st.metric(
            "🔄 Regenerative Braking",
            "OFF"
        )

with col8:

    st.metric(
        "🔌 Power Source",
        power_source
    )

# ------------------------------------------------------------
# BATTERY GAUGES
# ------------------------------------------------------------

st.divider()

st.header("🔋 Battery Monitoring")

st.write(
    f"Main Battery: {st.session_state.main_soc:.1f}%"
)

st.progress(
    int(st.session_state.main_soc)
)

st.write(
    f"Emergency Battery: {st.session_state.emergency_soc:.1f}%"
)

st.progress(
    int(st.session_state.emergency_soc)
)

# ------------------------------------------------------------
# AI STATUS
# ------------------------------------------------------------

st.divider()

st.header("🤖 AI Energy Management")

if ai_status == "NORMAL":

    st.success(
        f"AI STATUS: {ai_status}\n\n"
        f"ACTION: {ai_action}"
    )

elif ai_status == "LOW":

    st.warning(
        f"AI STATUS: {ai_status}\n\n"
        f"ACTION: {ai_action}"
    )

elif ai_status == "CRITICAL":

    st.warning(
        f"AI STATUS: {ai_status}\n\n"
        f"ACTION: {ai_action}"
    )

else:

    st.error(
        f"AI STATUS: {ai_status}\n\n"
        f"ACTION: {ai_action}"
    )

# ------------------------------------------------------------
# REGENERATIVE ENERGY
# ------------------------------------------------------------

st.divider()

st.header("⚡ Regenerative Energy Recovery")

if braking:

    st.success(
        f"Braking detected! "
        f"{recovered_energy:.3f} Wh recovered."
    )

else:

    st.info(
        "Vehicle is not braking. "
        "No regenerative energy recovered."
    )

# ------------------------------------------------------------
# SYSTEM INFORMATION
# ------------------------------------------------------------

st.divider()

st.header("📡 EERS System Information")

st.write("**System:** AI-IoT Intelligent Emergency Energy Recovery System")

st.write("**Controller:** ESP32 (future hardware integration)")

st.write("**AI:** TinyML / Machine Learning")

st.write("**Energy Recovery:** Regenerative braking")

st.write("**Backup:** Dedicated emergency battery")

st.write("**Dashboard:** IoT software simulation")

# ------------------------------------------------------------
# REFRESH
# ------------------------------------------------------------

st.divider()

st.info(
    "Dashboard automatically updates every 3 seconds."
)

time.sleep(3)

st.rerun()