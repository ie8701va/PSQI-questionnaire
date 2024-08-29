# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:41:13 2024

@author: ieva.valaviciute
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
PSQI = pd.read_excel(r"C:\Users\ieva.valaviciute\Downloads\PSQI.xlsx")
# Print the column names to verify their correctness
print(PSQI.columns)
PSQI.columns = [int(col) if str(col).isdigit() else col for col in PSQI.columns]

#%% 

# Remove the column named '8remove'
PSQI = PSQI.drop(columns=['8remove'])
# Convert 'Q3' to strings
PSQI['Q3'] = PSQI['Q3'].astype(str)

#%%
# Function to standardize time
def standardize_time(value):
    try:
        value = str(value).strip()
        
        # Special case: Convert any value containing '11' to '23:00'
        if '11' in value:
            return '23:00'
        
        if '12' in value:
            return '23:00'
        
        # Handle times with colon (e.g., '8:00', '23:30')
        if ':' in value:
            # Convert times like '08:30' directly
            time_str = pd.to_datetime(value, format='%H:%M', errors='coerce').strftime('%H:%M')
        
        elif len(value) == 4 and value.isdigit():
            # Handle 4-digit HHMM format (e.g., '0800', '2300')
            hours = int(value[:2])
            minutes = int(value[2:])
            # Adjust for 24-hour format
            if hours == 12:
                hours = 0  # Midnight case
            time_str = f"{hours:02d}:{minutes:02d}"
        
        else:
            # Convert value to float for decimal times
            float_value = float(value)
            
            if float_value >= 1000:
                # Handle HHMM format (e.g., 2300.0)
                hours = int(float_value) // 100
                minutes = int(float_value) % 100
            else:
                # Handle decimal hours format (e.g., 23.3, 0.3)
                hours = int(float_value)
                # Convert decimal part to minutes
                decimal_part = float_value - hours
                if decimal_part == 0.3:
                    minutes = 30
                elif decimal_part == 0.5:
                    minutes = 30
                else:
                    minutes = int(decimal_part * 60)  # Convert remaining decimal part to minutes
            
            # Handle edge cases for hours and minutes
            if hours >= 24:
                hours %= 24
            
            # Format the time string
            time_str = f"{hours:02d}:{minutes:02d}"
        
        # Convert to 24-hour format properly
        hours, minutes = map(int, time_str.split(':'))
        if hours == 12:
            hours = 0
        elif hours >= 12 and 'AM' in value.upper():
            hours -= 12
        elif hours < 12 and 'PM' in value.upper():
            hours += 12
        
        # Convert to 24-hour time string
        time_str = f"{hours:02d}:{minutes:02d}"

        return time_str
    
    except (ValueError, TypeError):
        return None  # Handle any unexpected values
#%%
# Define a function to map values to integers
def Q9_func(value):
    if value == 'Bastante mala':
        return 0
    elif value == 'Mala':
        return 1
    elif value == 'Buena':
        return 2
    elif value == 'Bastante Buena':
        return 3
    else:
        return None  # Handle any unexpected values
    
    #%%
    

# Define a function to map values to integers
def Q4_func(value):
    try:
        # Convert the value to a number if it is not already
        numeric_value = float(value)
    except ValueError:
        # Handle cases where the value is not convertible to a number
        return None
    
    # Map the numeric value to the corresponding integer based on the specified ranges
    if numeric_value > 7:
        return 0
    elif 6 <= numeric_value <= 7:
        return 1
    elif 5 <= numeric_value <= 6:
        return 2
    elif numeric_value < 5:
        return 3
    else:
        return None  # Handle any unexpected values
    #%% 
# Define a function to map numeric values to integers based on specified ranges
def Q2_func(value):
    try:
        # Convert the value to a number if it is not already
        numeric_value = float(value)
    except ValueError:
        # Handle cases where the value is not convertible to a number
        return None
    
    # Map the numeric value to the corresponding integer based on the specified ranges
    if numeric_value <= 15:
        return 0
    elif 16 <= numeric_value <= 30:
        return 1
    elif 31 <= numeric_value <= 60:
        return 2
    elif numeric_value > 60:
        return 3
    else:
        return None  # Handle any unexpected values
    
#%%


# Define a function to map numeric values to integers based on specified ranges
def Perc_func(value):
    try:
        # Convert the value to a number if it is not already
        numeric_value = float(value)
    except ValueError:
        # Handle cases where the value is not convertible to a number
        return None
    
    # Map the numeric value to the corresponding integer based on the specified ranges
    if numeric_value <= 65:
        return 3
    elif 65 <= numeric_value <= 74:
        return 2
    elif 75 <= numeric_value <= 84:
        return 1
    elif numeric_value > 85:
        return 0
    else:
        return None  # Handle any unexpected values
    
    
    
    #%%
    
    
    
# Define a function to map numeric values to integers based on specified ranges
def Comp2_func(value):
    try:
        # Convert the value to a number if it is not already
        numeric_value = float(value)
    except ValueError:
        # Handle cases where the value is not convertible to a number
        return None
    
    # Map the numeric value to the corresponding integer based on the specified ranges
    if numeric_value == 0:
        return 0
    elif 1 <= numeric_value <= 2:
        return 1
    elif 3 <= numeric_value <= 4:
        return 2
    elif 5 <= numeric_value <= 6:
        return 3
    else:
        return None  # Handle any unexpected values
    
    
    
        
    #%%
    
    
    
# Define a function to map numeric values to integers based on specified ranges
def Comp5_func(value):
    try:
        # Convert the value to a number if it is not already
        numeric_value = float(value)
    except ValueError:
        # Handle cases where the value is not convertible to a number
        return None
    
    # Map the numeric value to the corresponding integer based on the specified ranges
    if numeric_value == 0:
        return 0
    elif 1 <= numeric_value <= 9:
        return 1
    elif 10 <= numeric_value <= 18:
        return 2
    elif 19 <= numeric_value <= 27:
        return 3
    else:
        return None  # Handle any unexpected values
    
    
    
    #%%
    
    # Define a function to map values to integers
def Q5_func(value):
    if value == 'Ninguna vez en el ultimo mes':
        return 0
    elif value == 'Menos de una vez a la semana':
        return 1
    elif value == 'Una o dos veces a la semana':
        return 2
    elif value == 'Tres o más veces a la semana':
        return 3
    elif value == 'Tres or más veces a la semana':
        return 3
    else:
        return None  # Handle any unexpected values
        
    
    #%%
    
    # Define a function to map values to integers
def Q8_func(value):
    if value == 'Ningún problema':
        return 0
    elif value == 'Sólo un leve problema':
        return 1
    elif value == 'Un problema':
        return 2
    elif value == 'Un grave problema':
        return 3
    else:
        return None  # Handle any unexpected values
        
    
    
    #%%
# Apply the functions to create new columns based on existing columns

PSQI['Q1_standardized'] = PSQI['Q1'].apply(standardize_time)
PSQI['Q3_standardized'] = PSQI['Q3'].apply(standardize_time)



# Apply standardization function
PSQI['Q1_standardized'] = PSQI['Q1'].apply(standardize_time)
PSQI['Q3_standardized'] = PSQI['Q3'].apply(standardize_time)

# Convert standardized times to datetime for calculation
PSQI['Q1_datetime'] = pd.to_datetime(PSQI['Q1_standardized'], format='%H:%M')
PSQI['Q3_datetime'] = pd.to_datetime(PSQI['Q3_standardized'], format='%H:%M')

# Adjust wake-up time if it is earlier than sleep time
PSQI['Q3_datetime'] = PSQI.apply(lambda row: row['Q3_datetime'] + pd.DateOffset(days=1) if row['Q3_datetime'] < row['Q1_datetime'] else row['Q3_datetime'], axis=1)

# Calculate time in bed in hours
PSQI['time_in_bed'] = (PSQI['Q3_datetime'] - PSQI['Q1_datetime']).dt.total_seconds() / 3600


PSQI['sleep_efficiency'] = (PSQI['Q4'] / PSQI['time_in_bed']) * 100  #(# hours slept/# hours in bed) X 100% 
#%%

PSQI['2_scores'] = PSQI['Q2'].apply(Q2_func)
PSQI['4_scores'] = PSQI['Q4'].apply(Q4_func)
PSQI['9_scores'] = PSQI['Q9'].apply(Q9_func)
PSQI['5a_scores'] = PSQI['Q5a'].apply(Q5_func)
PSQI['5b_scores'] = PSQI['Q5b'].apply(Q5_func)
PSQI['5c_scores'] = PSQI['Q5c'].apply(Q5_func)
PSQI['5d_scores'] = PSQI['Q5d'].apply(Q5_func)
PSQI['5e_scores'] = PSQI['Q5e'].apply(Q5_func)
PSQI['5f_scores'] = PSQI['Q5f'].apply(Q5_func)
PSQI['5g_scores'] = PSQI['Q5g'].apply(Q5_func)
PSQI['5h_scores'] = PSQI['Q5h'].apply(Q5_func)
PSQI['5i_scores'] = PSQI['Q5i'].apply(Q5_func)
PSQI['6_scores'] = PSQI['Q6'].apply(Q5_func)
PSQI['7_scores'] = PSQI['Q7'].apply(Q5_func)
PSQI['8_scores'] = PSQI['Q8'].apply(Q8_func)


PSQI['calculating_comp2'] = PSQI['2_scores'] + PSQI['5a_scores']
PSQI['calculating_comp5'] = PSQI['5b_scores'] + PSQI['5c_scores'] + PSQI['5d_scores'] + PSQI['5e_scores'] + PSQI['5f_scores'] + PSQI['5g_scores'] + PSQI['5h_scores'] + PSQI['5i_scores']
PSQI['calculating_comp7'] = PSQI['7_scores'] + PSQI['8_scores']

#%% Calculating component weightings
PSQI['component_1'] = PSQI['9_scores']
PSQI['component_2'] = PSQI['calculating_comp2'].apply(Comp2_func)
PSQI['component_3'] = PSQI['4_scores']
PSQI['component_4'] = PSQI['sleep_efficiency'].apply(Perc_func)
PSQI['component_5'] = PSQI['calculating_comp5'].apply(Comp5_func)
PSQI['component_6'] = PSQI['6_scores']
PSQI['component_7'] = PSQI['calculating_comp7'].apply(Comp2_func)

# Calculate the PSQI score by summing the component columns
PSQI['PSQI_SCORE'] = (PSQI['component_1'] +
                      PSQI['component_2'] +
                      PSQI['component_3'] +
                      PSQI['component_4'] +
                      PSQI['component_5'] +
                      PSQI['component_6'] +
                      PSQI['component_7'])