import streamlit as st
from utils import get_travel_recommendations

st.set_page_config(page_title="AI Travel Planner", layout="centered")

st.title("AI Travel Planner")
st.write("Enter your source and destination to get the best travel recommendations.")

source = st.text_input("Enter Source:", placeholder="e.g., Mumbai")
destination = st.text_input("Enter Destination:", placeholder="e.g., Delhi")

if st.button("Get Travel Options"):
    if source and destination:
        with st.spinner("Fetching best travel option..."):
            travel_options = get_travel_recommendations(source, destination)
            st.success("Here are your travel options:")
            st.write(travel_options)
    else:
        st.warning("Please enter both source and destination.")
