import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("rent_model.pkl")

st.title("🏠 House Rent Prediction Web App")
st.markdown("Enter the house details below to predict rent:")

# User input fields
BHK = st.number_input("BHK (Number of Bedrooms)", min_value=1, max_value=10, value=2)
Size = st.number_input("Size (in sq ft)", min_value=200, max_value=10000, value=1000)
Bathroom = st.number_input("Number of Bathrooms", min_value=1, max_value=5, value=2)

area_type = st.selectbox("Area Type", ['Built Area', 'Carpet Area', 'Super Area'])
city = st.selectbox("City", ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai'])
furnishing = st.selectbox("Furnishing Status", ['Furnished', 'Semi-Furnished', 'Unfurnished'])
tenant = st.selectbox("Tenant Preferred", ['Bachelors', 'Bachelors/Family', 'Family'])

# Encode values (same as used during training)
area_map = {'Built Area': 0, 'Carpet Area': 1, 'Super Area': 2}
city_map = {'Bangalore': 0, 'Chennai': 1, 'Delhi': 2, 'Hyderabad': 3, 'Kolkata': 4, 'Mumbai': 5}
furnishing_map = {'Furnished': 0, 'Semi-Furnished': 1, 'Unfurnished': 2}
tenant_map = {'Bachelors': 0, 'Bachelors/Family': 1, 'Family': 2}

# Predict rent
if st.button("Predict Rent"):
    input_data = np.array([[BHK, Size, Bathroom,
                            area_map[area_type],
                            city_map[city],
                            furnishing_map[furnishing],
                            tenant_map[tenant]]])

    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Monthly Rent: ₹{int(prediction[0]):,}")
