import streamlit as st

st.header("Help page")
st.subheader("Definitions and translations:")
st.markdown('To see the full descriptions, please scroll to the right.')
st.text(
"Activiteit = Activity.\n"
"\n"
"Buslijn = Bus line.\n"
"\n"
"Dienst rit = A ride/drive in which the bus transports passengers.\n"
"\n"
"Eindlocatie = The final destination of a bus ride.\n"
"\n"
"Eindtijd = The time a bus reaches its final destination of a ride/drive (24-hour clock).\n"
"\n"
"Eindtijd datum = The date and time a bus reaches its final destination of a ride/drive (24-hour clock).\n"
"\n"
"Energieverbruik = Energy used by the bus (in kWh).\n"
"\n"
"Gantt chart = A graph that illustrates a schedule.\n"
"\n"
"Idle (time) = When a bus is not in use.\n"
"\n"
"Key Performance Indicator = Quantifiable indicators to measure the quality of a planning.\n"
"\n"
"Materiaal rit = Any ride/drive in which the bus does not transport passengers.\n"
"\n"
"Omloop nummer = Circulation number. The number of the bus, which separates all the x amount of busses.\n"
"\n"
"Omloop planning = Circulation planning. The planning of the busses.\n"
"\n"
"Opladen = Charging the battery of the bus.\n"
"\n"
"Startlocatie = The starting location of a bus ride.\n"
"\n"
"Starttijd = The time a bus ride starts (24-hour clock).\n"
"\n"
"Starttijd datum = The date and time a bus ride starts (24-hour clock).\n"
"\n"
"State of Charge = The remaining dischargable capacity of a battery (in percentages).\n"
"\n"
"State of Health = The estimation of the maximum level of charge of a battery relative to its initial value "
"when it is first used (in percentages)."
"")

st.divider()

st.subheader("KPI calculations explained:")
st.text(
"Battery use = All the energy use added up together (in kWh).\n"
"\n"
"Total idle time = All the idle time added up together (in minutes).")

st.divider()

st.subheader("Abbreviations:")
st.text(
"ehvapt = Eindhoven Airport.\n"
"\n"
"ehvbst = Eindhoven Busstation.\n"
"\n"
"ehvgr = Eindhoven Garage.\n"
"\n"
"KPI = Key Performance Indicator.\n"
"\n"
"SOC = State of Charge.\n"
"\n"
"SOH = State of Health.")





