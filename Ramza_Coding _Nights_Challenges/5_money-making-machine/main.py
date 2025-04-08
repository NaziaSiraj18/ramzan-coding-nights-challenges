# import necessary tools/libraries
import streamlit as st  
import random
import time
import requests

# Set the title of our web app
st.title("Money Making Machine")

# Function to create random amount of money
def generate_money():
      return random.randint(1, 1000)
  
# Create a section for generating money  
st.subheader("InstantCash Generator")
if st.button("Generate_money"): #When user clicks the button
    st.write ("Counting Your Money...") #Show loading message
    time.sleep(5)
    amount = generate_money() # Get random amount
    st.success(f"You made ${amount}!") #Show success message with amount

# Function to get side hustle ideas  from a server
def fetch_side_hustle():
    try:
        # Try to get data from local server
        response = requests.get("http://127.0.0.1:8000/side-hustles")
        if response.status_code == 200: # if request successful
            hustles = response.json() # Convert response to JSON
            return hustles["side_hustles"] # Return the hustle idea
        else:
            return("Freelancing!")  # Default response if server fails
    except:
        return ("Something went wrong!") # Error message if request fails

# Create a section for side hustle ideas 
st.subheader("Side Hustle Ideas")
if st.button("Generate Hustle"): # When user clicks button 
    idea = fetch_side_hustle()
    st.success(idea) # Show the idea 

# Function to get money-related quotes from server        
def fetch_money_quotes():
    try:
        # Try to get quotes from local server
        response = requests.get("http://127.0.0.1:8000/money-quotes")
        if response.status_code == 200: # if request sceessful
            quotes = response.json()  # Convert response to JSON
            return quotes["side_hustles"] # Return the quotes
        else:
            return("Money is the root of all evil!") # Default response if server fails
    except:
        return ("Something went wrong!") # Error message if request fails

# Create a section for motivational quotes
st.subheader("Money-Making Motivation")
if st.button("Get Inspired"): # When user clicks button
    quote = fetch_money_quotes() # Get the quote
    st.info(quote) # Show the quote
        
      
    
    