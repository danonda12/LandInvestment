import streamlit as st 
import pandas as pd

st.title("StatisticsDemographics")
acre = 43560
numacre = st.number_input("Acre of Land: ")
if acre: 
    sqft = numacre * acre
    st.write("Square Footage of Acre is: ", sqft)
    st.info(sqft)
investment = st.number_input("Investment of property: ")
st.write("Investment of a property is: ", investment)
st.info(investment)
investmentpersqft = st.number_input("Square footage of investment: ")
st.write("Square Footage of Investment: ")
st.warning(investmentpersqft)
numinvestment = st.number_input("Number of investments: ")
multiplication = numinvestment * investmentpersqft
st.write("Investment by Square Feet: ", multiplication)
subtract = sqft - numinvestment
st.write("Amount of Land left after investments in Square feet: ",subtract)
growthrate = st.number_input("Growth rate percentage of investment: ")
growthratemultiplication = growthrate * investment
nextyear = investment * 1+(growthrate)
NumberofPeriods = st.slider("Number of years: ",min_value = 1, max_value = 100, value = 1)
returninvestment = investment * (1 + (growthrate / 100))**NumberofPeriods

st.write("Return in Investment: ",returninvestment)


# Initialization
if 'Number_of_Acres' not in st.session_state:
    st.session_state['Number_of_Acres'] = []
st.session_state['Number_of_Acres'].append(numacre)

# Session State also supports attribute based syntax
if 'Investment' not in st.session_state:
    st.session_state.Investment = []
st.session_state.Investment.append(investment)

# Session State also supports attribute based syntax
if 'Number_of_Investment' not in st.session_state:
    st.session_state.Number_of_Investment = []
st.session_state.Number_of_Investment.append(numinvestment)

# Session State also supports attribute based syntax
if 'Return_in_Investment' not in st.session_state:
    st.session_state.Return_in_Investment = []
st.session_state.Return_in_Investment.append(returninvestment)

# Create a DataFrame
data = {
    "Number of Acres": st.session_state.Number_of_Acres,
    "Investment": st.session_state.Investment,
    "Number of Investment": st.session_state.Number_of_Investment,
    "Return in Investment": st.session_state.Return_in_Investment
}

df = pd.DataFrame(data)

# Export the DataFrame to a CSV file

def convert_df_to_csv(df):
  # IMPORTANT: Cache the conversion to prevent computation on every rerun
  return df.to_csv().encode('utf-8')


if not df.empty:
    st.download_button(
        label="Download data as CSV",
        data=convert_df_to_csv(df),
        file_name='investments.csv',
        mime='text/csv',
    )