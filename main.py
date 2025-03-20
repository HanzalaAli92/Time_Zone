# Import required libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of available time zones
TIME_ZONES = [
    "UTC 🌍",
    "Asia/Karachi 🇵🇰",
    "America/New_York 🇺🇸",
    "Europe/London 🇬🇧",
    "Asia/Tokyo 🇯🇵",
    "Australia/Sydney 🇦🇺",
    "America/Los_Angeles 🇺🇸",
    "Europe/Berlin 🇩🇪",
    "Asia/Dubai 🇦🇪",
    "Asia/Kolkata 🇮🇳",
    "America/Chicago 🇺🇸",
    "America/Toronto 🇨🇦",
    "Europe/Paris 🇫🇷",
    "Europe/Madrid 🇪🇸",
    "Europe/Rome 🇮🇹",
    "Europe/Moscow 🇷🇺",
    "Asia/Shanghai 🇨🇳",
    "Asia/Hong_Kong 🇭🇰",
    "Asia/Singapore 🇸🇬",
    "Asia/Jakarta 🇮🇩",
    "Asia/Seoul 🇰🇷",
    "Africa/Cairo 🇪🇬",
    "Africa/Johannesburg 🇿🇦",
    "America/Mexico_City 🇲🇽",
    "America/Sao_Paulo 🇧🇷",
    "Australia/Melbourne 🇦🇺",
    "Australia/Perth 🇦🇺",
    "Pacific/Auckland 🇳🇿",
    "Pacific/Honolulu 🇺🇸",
    "Europe/Amsterdam 🇳🇱",
    "Europe/Stockholm 🇸🇪",
    "Europe/Oslo 🇳🇴",
    "Europe/Vienna 🇦🇹",
    "Europe/Brussels 🇧🇪",
    "Asia/Kuala_Lumpur 🇲🇾",
    "Asia/Manila 🇵🇭",
    "Asia/Colombo 🇱🇰",
    "Asia/Tehran 🇮🇷",
    "Asia/Baghdad 🇮🇶",
    "Asia/Riyadh 🇸🇦",
    "Asia/Amman 🇯🇴",
    "Asia/Bangkok 🇹🇭",
    "Asia/Yangon 🇲🇲",
    "America/Vancouver 🇨🇦",
    "America/Denver 🇺🇸",
    "America/Phoenix 🇺🇸",
    "America/Argentina/Buenos_Aires 🇦🇷",
    "America/Bogota 🇨🇴",
    "America/Caracas 🇻🇪",
    "Antarctica/Casey ❄️",
    "Pacific/Fiji 🇫🇯"
]

# Set page title and icon
st.set_page_config(page_title="Time Zone Converter 🌍⏰", page_icon="⏳")

# Add custom CSS for dark mode
st.markdown(
    """
    <style>
    .st-emotion-cache-bm2z3a {
        position: absolute;
        inset: 0px;
        background: black;
        color: white;
    }

    h1, h2, h3, h4, h5, h6, p, label {
        color: white;  /* White text */
    }
    .stButton>button {
        background-color: #007BFF !important;
        color: white !important;
        font-size: 16px !important;
        padding: 10px 24px !important;
        border-radius: 8px !important;
    }
    .stButton>button:hover {
        background-color: #0056b3 !important;
    }
    .stTextInput>div>div>input {
        background-color: #222222 !important;
        color: white !important;
        border-color: #007BFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title with emoji
st.markdown("<h1 style='text-align: center;'>⏳ Time Zone Converter 🌎</h1>", unsafe_allow_html=True)

# Time zone selection
st.markdown("### 🌐 Select Timezones")
selected_timezone = st.multiselect(
    "Choose timezones to display:", TIME_ZONES, default=["UTC 🌍", "Asia/Karachi 🇵🇰"]
)

# Display current time for selected time zones
st.markdown("### 🕰️ Current Time in Selected Zones")
for tz in selected_timezone:
    tz_name = tz.split(" ")[0]  # Extract timezone ID without emoji
    current_time = datetime.now(ZoneInfo(tz_name)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: 🕒 {current_time}")

# Section for time conversion
st.markdown("---")
st.markdown("### 🔄 Convert Time Between Timezones")

# Input fields for time conversion
current_time = st.time_input("⏱ Enter Time to Convert", value=datetime.now().time())
from_tz = st.selectbox("🌍 From Timezone", TIME_ZONES, index=0)
to_tz = st.selectbox("🌎 To Timezone", TIME_ZONES, index=1)

# Convert button
if st.button("🔄 Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz.split(" ")[0]))
    converted_time = dt.astimezone(ZoneInfo(to_tz.split(" ")[0])).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"✅ Converted Time in {to_tz}: 🕒 {converted_time}")