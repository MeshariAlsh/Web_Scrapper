# Scrapping Script 

## Current Status: Data Gathering

- **Progress**: Successfully scraped data using Playwright and stored it in a tidy CSV format using `pandas`.
- **Next Steps**: Move to the **Data Preprocessing** stage to clean and prepare the data for analysis and modeling.

## Datasets 

### Dataset 1: Fighter Statistics
Contains individual fighter profiles and performance metrics. Example columns:
- **Name**: Fighter's name.
- **Fighting Style**: Primary fighting style.
- **Age, Height, Weight**: Demographic and physical attributes.
- **Octagon Debut**: Date of UFC debut.
- **Reach, Leg Reach**: Physical reach measurements.
- **Performance Stats**: Includes metrics like strikes, takedowns, and submissions.
- **Career Record**: Wins, losses, and draws.

## Data Gathering Process

- **Tool Used**: [Playwright](https://playwright.dev) for web scraping.
- **Storage and Formatting**: Data is stored in CSV files using `pandas` for ease of analysis and manipulation.

### Challenges Faced

- Handling dynamic website content with Playwright.
- Structuring the raw data into meaningful and usable formats.

## Planned Next Steps: Data Preprocessing

1. **Data Cleaning**:
   - Handling missing or inconsistent values.
   - Formatting dates and numerical fields for analysis.

2. **Feature Engineering**:
   - Creating matchup-specific features (difference in reach, strike metrics).
   - Encoding categorical variables like fighting styles.

3. **Exploratory Data Analysis (EDA)**:
   - Visualizing data distributions and correlations to identify key trends.
   - Identifying features that strongly correlate with fight outcomes.


## Tech Stack

- **Scraping**: Playwright
- **Data Manipulation**: Pandas
