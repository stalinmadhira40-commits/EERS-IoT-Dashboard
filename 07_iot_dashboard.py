# ============================================================
# EERS - PROGRAM 07
# AI-IoT EV Dashboard
# GOOGLE MAPS + LIVE LOCATION + EV CHARGING STATIONS
# ============================================================

import streamlit as st
import random
import math
import urllib.parse

from streamlit_geolocation import streamlit_geolocation


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="EERS EV Emergency Dashboard",
    page_icon="🔋",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title(
    "🔋 EERS - Intelligent Emergency Energy Recovery System"
)

st.subheader(
    "AI + IoT Based Electric Vehicle Energy Management Dashboard"
)

st.write(
    "Monitor EV battery condition, regenerative energy recovery, "
    "emergency backup and nearby EV charging stations using Google Maps."
)

st.divider()


# ============================================================
# INITIAL SIMULATION VALUES
# ============================================================

if "main_soc" not in st.session_state:
    st.session_state.main_soc = 85.0

if "emergency_soc" not in st.session_state:
    st.session_state.emergency_soc = 40.0

if "total_recovered" not in st.session_state:
    st.session_state.total_recovered = 0.0


# ============================================================
# SIMULATED EV PARAMETERS
# ============================================================

vehicle_speed = random.randint(20, 60)

temperature = random.uniform(25, 40)

motor_power = random.uniform(20, 80)

braking = random.choice(
    [True, False]
)


# ============================================================
# MAIN BATTERY CONSUMPTION
# ============================================================

energy_used = motor_power / 60

main_soc_loss = (
    energy_used / 100
) * 100

st.session_state.main_soc -= main_soc_loss

if st.session_state.main_soc < 0:
    st.session_state.main_soc = 0


# ============================================================
# REGENERATIVE ENERGY RECOVERY
# ============================================================

recovered_energy = 0.0

if braking:

    recovered_energy = random.uniform(
        0.05,
        0.50
    )

    st.session_state.total_recovered += (
        recovered_energy
    )

    emergency_gain = (
        recovered_energy / 50
    ) * 100

    st.session_state.emergency_soc += (
        emergency_gain
    )

    if st.session_state.emergency_soc > 100:
        st.session_state.emergency_soc = 100


# ============================================================
# AI ENERGY MANAGEMENT
# ============================================================

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


# ============================================================
# POWER SOURCE
# ============================================================

if (
    ai_status == "EMERGENCY"
    and
    st.session_state.emergency_soc > 0
):

    power_source = "EMERGENCY BATTERY"

else:

    power_source = "MAIN BATTERY"


# ============================================================
# LIVE EV PARAMETERS
# ============================================================

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


# ============================================================
# SECOND ROW
# ============================================================

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

    st.metric(
        "🔄 Regenerative Braking",
        "ACTIVE" if braking else "OFF"
    )


with col8:

    st.metric(
        "🔌 Power Source",
        power_source
    )


# ============================================================
# BATTERY MONITORING
# ============================================================

st.divider()

st.header("🔋 Battery Monitoring")


st.write(
    f"Main Battery: "
    f"{st.session_state.main_soc:.1f}%"
)

st.progress(
    int(
        max(
            0,
            min(
                100,
                st.session_state.main_soc
            )
        )
    )
)


st.write(
    f"Emergency Battery: "
    f"{st.session_state.emergency_soc:.1f}%"
)

st.progress(
    int(
        max(
            0,
            min(
                100,
                st.session_state.emergency_soc
            )
        )
    )
)


# ============================================================
# AI ENERGY MANAGEMENT
# ============================================================

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


# ============================================================
# REGENERATIVE ENERGY
# ============================================================

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


# ============================================================
# LIVE LOCATION
# ============================================================

st.divider()

st.header("📍 Live EV Location")


st.write(
    "Allow browser location access to find EV charging "
    "stations near your current location."
)


location = streamlit_geolocation()


latitude = None
longitude = None


if location:

    latitude = location.get("latitude")

    longitude = location.get("longitude")


# ============================================================
# MANUAL LOCATION
# ============================================================

with st.expander("📌 Use Manual Location"):

    st.write(
        "If your browser cannot provide GPS location, "
        "enter latitude and longitude manually."
    )


    manual_lat = st.number_input(
        "Latitude",
        value=17.3850,
        format="%.6f"
    )


    manual_lon = st.number_input(
        "Longitude",
        value=78.4867,
        format="%.6f"
    )


    use_manual = st.checkbox(
        "Use manual location"
    )


    if use_manual:

        latitude = manual_lat

        longitude = manual_lon


# ============================================================
# DISTANCE CALCULATION
# ============================================================

def calculate_distance(
    lat1,
    lon1,
    lat2,
    lon2
):

    earth_radius = 6371.0

    lat1_rad = math.radians(lat1)

    lat2_rad = math.radians(lat2)

    delta_lat = math.radians(
        lat2 - lat1
    )

    delta_lon = math.radians(
        lon2 - lon1
    )

    a = (
        math.sin(delta_lat / 2) ** 2
        +
        math.cos(lat1_rad)
        *
        math.cos(lat2_rad)
        *
        math.sin(delta_lon / 2) ** 2
    )

    c = (
        2
        *
        math.atan2(
            math.sqrt(a),
            math.sqrt(1 - a)
        )
    )

    return earth_radius * c


# ============================================================
# GOOGLE MAPS SECTION
# ============================================================

if (
    latitude is not None
    and
    longitude is not None
):

    st.divider()

    st.success(
        f"📍 Your live location detected\n\n"
        f"Latitude: {latitude:.6f}\n\n"
        f"Longitude: {longitude:.6f}"
    )


    # ========================================================
    # GOOGLE MAPS URL
    # ========================================================

    location_query = (
        f"{latitude},{longitude}"
    )


    google_map_url = (
        "https://www.google.com/maps/"
        f"@{latitude},{longitude},15z"
    )


    charging_search_url = (
        "https://www.google.com/maps/search/"
        "?api=1"
        "&query="
        +
        urllib.parse.quote(
            f"EV charging station near {latitude},{longitude}"
        )
    )


    # ========================================================
    # GOOGLE MAPS BUTTONS
    # ========================================================

    st.header(
        "🗺️ Google Maps"
    )


    map_col1, map_col2 = st.columns(2)


    with map_col1:

        st.link_button(
            "🗺️ Open My Live Location",
            google_map_url,
            use_container_width=True
        )


    with map_col2:

        st.link_button(
            "⚡ Find EV Charging Stations",
            charging_search_url,
            use_container_width=True
        )


    # ========================================================
    # GOOGLE MAPS EMBED
    # ========================================================

    st.subheader(
        "📍 Your Current Location"
    )


    st.components.v1.html(
        f"""
        <iframe
            src="https://www.google.com/maps?q={latitude},{longitude}&output=embed"
            width="100%"
            height="500"
            style="border:0;"
            allowfullscreen=""
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade">
        </iframe>
        """,
        height=520
    )


    # ========================================================
    # CHARGING STATION SEARCH
    # ========================================================

    st.divider()

    st.header(
        "⚡ EV Charging Stations Near You"
    )


    st.write(
        "Google Maps will search charging stations "
        "around your current location."
    )


    st.link_button(
        "🔋 SEARCH NEARBY CHARGING STATIONS ON GOOGLE MAPS",
        charging_search_url,
        use_container_width=True
    )


    # ========================================================
    # SELECT STATION FOR DIRECTIONS
    # ========================================================

    st.divider()

    st.header(
        "🧭 Get Directions to Charging Station"
    )


    station_name = st.text_input(
        "Enter charging station name",
        placeholder="Example: Tata Power EV Charging Station"
    )


    if station_name:

        destination = urllib.parse.quote(
            station_name
        )


        directions_url = (
            "https://www.google.com/maps/dir/"
            "?api=1"
            f"&origin={latitude},{longitude}"
            f"&destination={destination}"
        )


        st.link_button(
            "🧭 Navigate to This Charging Station",
            directions_url,
            use_container_width=True
        )


    # ========================================================
    # QUICK SEARCH OPTIONS
    # ========================================================

    st.divider()

    st.header(
        "⚡ Quick Charging Searches"
    )


    q1, q2, q3 = st.columns(3)


    fast_dc_url = (
        "https://www.google.com/maps/search/"
        "?api=1&query="
        +
        urllib.parse.quote(
            f"DC fast EV charger near {latitude},{longitude}"
        )
    )


    tata_url = (
        "https://www.google.com/maps/search/"
        "?api=1&query="
        +
        urllib.parse.quote(
            f"Tata Power EV charging station near {latitude},{longitude}"
        )
    )


    ev_station_url = (
        "https://www.google.com/maps/search/"
        "?api=1&query="
        +
        urllib.parse.quote(
            f"EV charging station near {latitude},{longitude}"
        )
    )


    with q1:

        st.link_button(
            "⚡ DC Fast Chargers",
            fast_dc_url,
            use_container_width=True
        )


    with q2:

        st.link_button(
            "🔋 Tata Power Chargers",
            tata_url,
            use_container_width=True
        )


    with q3:

        st.link_button(
            "🚗 All EV Chargers",
            ev_station_url,
            use_container_width=True
        )


else:

    st.info(
        "📍 Allow browser location access above "
        "to use Google Maps and find charging stations."
    )


# ============================================================
# EERS SYSTEM INFORMATION
# ============================================================

st.divider()

st.header(
    "📡 EERS System Information"
)


st.write(
    "**System:** AI-IoT Based Intelligent "
    "Emergency Energy Recovery System"
)


st.write(
    "**Controller:** ESP32 "
    "(future hardware integration)"
)


st.write(
    "**AI:** Machine Learning / TinyML"
)


st.write(
    "**Energy Recovery:** Regenerative Braking"
)


st.write(
    "**Emergency Backup:** Dedicated Emergency Battery"
)


st.write(
    "**Location:** Browser GPS / Future NEO-6M GPS"
)


st.write(
    "**Map:** Google Maps"
)


st.write(
    "**Dashboard:** Streamlit IoT Web Dashboard"
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "EERS - AI-IoT Based Intelligent Emergency "
    "Energy Recovery System for Electric Vehicles"
)

st.caption(
    "Software simulation stage | "
    "Real ESP32 sensor integration will be added later."
)
