# ============================================================
# EERS - PROGRAM 07
# AI-IoT EV Dashboard + Interactive Charging Station Map
# ============================================================

import streamlit as st
import random
import math
import requests
import folium

from streamlit_folium import st_folium
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

st.title("🔋 EERS - Intelligent Emergency Energy Recovery System")

st.subheader(
    "AI + IoT Based Electric Vehicle Energy Management Dashboard"
)

st.write(
    "Real-time software simulation of battery monitoring, "
    "regenerative energy recovery, emergency backup and "
    "nearby EV charging-station detection."
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

braking = random.choice([True, False])


# ============================================================
# MAIN BATTERY ENERGY CONSUMPTION
# ============================================================

energy_used = motor_power / 60

main_soc_loss = (energy_used / 100) * 100

st.session_state.main_soc -= main_soc_loss

if st.session_state.main_soc < 0:
    st.session_state.main_soc = 0


# ============================================================
# REGENERATIVE ENERGY RECOVERY
# ============================================================

recovered_energy = 0.0

if braking:

    recovered_energy = random.uniform(0.05, 0.5)

    st.session_state.total_recovered += recovered_energy

    emergency_gain = (recovered_energy / 50) * 100

    st.session_state.emergency_soc += emergency_gain

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

if ai_status == "EMERGENCY" and st.session_state.emergency_soc > 0:

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
    int(max(0, min(100, st.session_state.main_soc)))
)


st.write(
    f"Emergency Battery: "
    f"{st.session_state.emergency_soc:.1f}%"
)

st.progress(
    int(max(0, min(100, st.session_state.emergency_soc)))
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
# LOCATION
# ============================================================

st.divider()

st.header("📍 Your EV Location")


st.write(
    "Allow location access in your browser to find "
    "nearby EV charging stations."
)


location = streamlit_geolocation()


# ============================================================
# LOCATION VARIABLES
# ============================================================

latitude = None
longitude = None


if location:

    latitude = location.get("latitude")

    longitude = location.get("longitude")


# ============================================================
# MANUAL LOCATION OPTION
# ============================================================

with st.expander("📌 Enter location manually"):

    st.write(
        "If browser location is unavailable, "
        "you can enter latitude and longitude manually."
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
# DISTANCE FUNCTION
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

    delta_lat = math.radians(lat2 - lat1)

    delta_lon = math.radians(lon2 - lon1)

    a = (
        math.sin(delta_lat / 2) ** 2
        +
        math.cos(lat1_rad)
        *
        math.cos(lat2_rad)
        *
        math.sin(delta_lon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return earth_radius * c


# ============================================================
# FIND NEARBY CHARGING STATIONS
# ============================================================

def get_charging_stations(
    latitude,
    longitude,
    radius=10000
):

    query = f"""
    [out:json];

    (
      node
        ["amenity"="charging_station"]
        (around:{radius},{latitude},{longitude});

      way
        ["amenity"="charging_station"]
        (around:{radius},{latitude},{longitude});

      relation
        ["amenity"="charging_station"]
        (around:{radius},{latitude},{longitude});
    );

    out center tags;
    """

    url = "https://overpass-api.de/api/interpreter"

    try:

        response = requests.post(
            url,
            data=query,
            timeout=30
        )

        response.raise_for_status()

        return response.json().get(
            "elements",
            []
        )

    except Exception as error:

        st.error(
            "Unable to retrieve charging stations "
            "right now."
        )

        return []


# ============================================================
# MAP SECTION
# ============================================================

if latitude is not None and longitude is not None:

    st.success(
        f"📍 Location detected: "
        f"{latitude:.6f}, {longitude:.6f}"
    )

    st.header(
        "🗺️ Nearby EV Charging Stations"
    )

    # --------------------------------------------------------
    # GET CHARGING STATIONS
    # --------------------------------------------------------

    stations = get_charging_stations(
        latitude,
        longitude,
        radius=10000
    )


    # --------------------------------------------------------
    # PROCESS STATIONS
    # --------------------------------------------------------

    station_data = []


    for station in stations:

        tags = station.get(
            "tags",
            {}
        )

        station_lat = station.get(
            "lat"
        )

        station_lon = station.get(
            "lon"
        )


        # For ways/relations
        if station_lat is None:

            center = station.get(
                "center",
                {}
            )

            station_lat = center.get(
                "lat"
            )

            station_lon = center.get(
                "lon"
            )


        if (
            station_lat is None
            or station_lon is None
        ):
            continue


        distance = calculate_distance(
            latitude,
            longitude,
            station_lat,
            station_lon
        )


        name = (
            tags.get("name")
            or tags.get("operator")
            or "EV Charging Station"
        )


        operator = (
            tags.get("operator")
            or "Not specified"
        )


        station_data.append(
            {
                "name": name,
                "operator": operator,
                "latitude": station_lat,
                "longitude": station_lon,
                "distance": distance
            }
        )


    # --------------------------------------------------------
    # SORT BY DISTANCE
    # --------------------------------------------------------

    station_data.sort(
        key=lambda x: x["distance"]
    )


    # --------------------------------------------------------
    # SHOW MAP
    # --------------------------------------------------------

    ev_map = folium.Map(

        location=[
            latitude,
            longitude
        ],

        zoom_start=13,

        control_scale=True
    )


    # --------------------------------------------------------
    # YOUR LOCATION MARKER
    # --------------------------------------------------------

    folium.Marker(

        [
            latitude,
            longitude
        ],

        popup=(
            "<b>🚗 Your EV</b><br>"
            "Current Location"
        ),

        tooltip="🚗 Your EV",

        icon=folium.Icon(
            color="blue",
            icon="car",
            prefix="fa"
        )

    ).add_to(ev_map)


    # --------------------------------------------------------
    # CHARGING STATION MARKERS
    # --------------------------------------------------------

    for index, station in enumerate(
        station_data[:50]
    ):

        popup_text = f"""
        <b>⚡ {station['name']}</b><br>
        Operator: {station['operator']}<br>
        Distance: {station['distance']:.2f} km
        """


        folium.Marker(

            [
                station["latitude"],
                station["longitude"]
            ],

            popup=popup_text,

            tooltip=(
                f"⚡ {station['name']} "
                f"({station['distance']:.2f} km)"
            ),

            icon=folium.Icon(
                color="green",
                icon="bolt",
                prefix="fa"
            )

        ).add_to(ev_map)


    # --------------------------------------------------------
    # DISPLAY MAP
    # --------------------------------------------------------

    map_data = st_folium(

        ev_map,

        width=None,

        height=600,

        returned_objects=[]
    )


    # ========================================================
    # NEAREST STATION
    # ========================================================

    if station_data:

        nearest = station_data[0]


        st.divider()

        st.header(
            "🥇 Nearest EV Charging Station"
        )


        c1, c2, c3 = st.columns(3)


        with c1:

            st.metric(
                "⚡ Station",
                nearest["name"]
            )


        with c2:

            st.metric(
                "📏 Distance",
                f"{nearest['distance']:.2f} km"
            )


        with c3:

            st.metric(
                "🏢 Operator",
                nearest["operator"]
            )


        # ----------------------------------------------------
        # GOOGLE MAPS DIRECTIONS
        # ----------------------------------------------------

        directions_url = (
            "https://www.google.com/maps/dir/?api=1"
            f"&origin={latitude},{longitude}"
            f"&destination="
            f"{nearest['latitude']},"
            f"{nearest['longitude']}"
        )


        st.link_button(
            "🧭 Get Directions",
            directions_url
        )


        # ====================================================
        # TOP NEARBY STATIONS
        # ====================================================

        st.divider()

        st.header(
            "⚡ Nearby Charging Stations"
        )


        for number, station in enumerate(
            station_data[:10],
            start=1
        ):

            st.write(
                f"**{number}. ⚡ "
                f"{station['name']}**"
            )

            st.write(
                f"Distance: "
                f"{station['distance']:.2f} km"
                f" | Operator: "
                f"{station['operator']}"
            )

            st.divider()


    else:

        st.warning(
            "No EV charging stations were found "
            "within approximately 10 km of your location."
        )


else:

    st.info(
        "📍 Please allow location access above "
        "to display your position and nearby "
        "EV charging stations."
    )


# ============================================================
# EERS SYSTEM INFORMATION
# ============================================================

st.divider()

st.header(
    "📡 EERS System Information"
)


st.write(
    "**System:** AI-IoT Intelligent Emergency "
    "Energy Recovery System"
)

st.write(
    "**Controller:** ESP32 "
    "(future hardware integration)"
)

st.write(
    "**AI:** Machine Learning / TinyML "
    "(future hardware integration)"
)

st.write(
    "**Energy Recovery:** Regenerative braking"
)

st.write(
    "**Backup:** Dedicated emergency battery"
)

st.write(
    "**GPS:** Vehicle location and charging-station guidance"
)

st.write(
    "**Map:** OpenStreetMap + EV charging-station data"
)

st.write(
    "**Dashboard:** Streamlit IoT Web Dashboard"
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "EERS - AI-IoT Based Intelligent Emergency Energy "
    "Recovery System for Electric Vehicles"
)

st.caption(
    "Software simulation stage | "
    "Real ESP32 sensor integration will be added later."
)
