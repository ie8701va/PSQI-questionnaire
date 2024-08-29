# PSQI-questionnaire
Python script for automating the extraction, transformation, and scoring of data from the Pittsburgh Sleep Quality Index (PSQI) questionnaire

# PSQI Data Processing Script

## Overview

This Python script automates the extraction, transformation, and scoring of data from the Pittsburgh Sleep Quality Index (PSQI) questionnaire, which has been collected via Google Forms. The script is designed to standardize the raw data, convert time fields to a consistent format, calculate various components of the PSQI, and ultimately generate a total PSQI score for each respondent.

## Features

- **Data Loading:** The script begins by loading the raw PSQI data from an Excel file.
- **Data Cleaning:**
  - Removes unnecessary columns (e.g., '8remove').
  - Converts and standardizes time-related data to ensure consistency.
- **Component Calculation:**
  - Standardizes and processes various time and numeric fields.
  - Applies predefined scoring functions to each component of the PSQI, including sleep duration, sleep latency, sleep efficiency, and more.
- **PSQI Score Calculation:** Combines the calculated components to derive the overall PSQI score for each respondent.

## Detailed Workflow

1. **Load the Data:**
   - The script imports the dataset from an Excel file using the `pandas` library.
   - It then verifies the column names to ensure accuracy.

2. **Data Cleaning:**
   - Removes extraneous columns that are not needed for PSQI calculations.
   - Converts specific fields (e.g., `Q3`) to strings to facilitate further processing.

3. **Standardize Time Fields:**
   - A custom function, `standardize_time`, is used to normalize time entries, accounting for various input formats (e.g., HH:MM, HHMM, decimal hours).
   - The script handles special cases, such as converting ambiguous or inconsistent time formats into a standard 24-hour format.

4. **Score Calculation:**
   - Custom functions (`Q9_func`, `Q4_func`, `Q2_func`, etc.) map questionnaire responses to numerical scores based on predefined rules.
   - These functions address a range of responses, from subjective sleep quality to the frequency of sleep disturbances.

5. **Component Weightings:**
   - The script calculates each PSQI component based on the processed data.
   - Components such as sleep duration, latency, and efficiency are computed, standardized, and weighted.

6. **Final PSQI Score:**
   - The individual component scores are summed to produce the final PSQI score for each respondent, providing a quantifiable measure of sleep quality.

## Requirements

- Python 3.x
- `pandas` library

## Usage

1. Clone this repository to your local machine.
2. Place your PSQI dataset in the specified directory.
3. Run the script using your preferred Python environment.
4. The script will output a processed dataset with PSQI scores ready for analysis.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Author

- **Ieva Valaviciute**
