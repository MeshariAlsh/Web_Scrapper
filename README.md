# Ultimate_Fighting_Predictor

## Overview

This project aims to predict the probability of a UFC fighter winning a match using machine learning. By analyzing fighter statistics and matchup data scraped from the official UFC website and [UFCStats](http://www.ufcstats.com), the model will provide insights into factors that influence fight outcomes.

## Current Status: Data Gathering

- **Progress**: Successfully scraped data using Playwright and stored it in a tidy CSV format using `pandas`.
- **Next Steps**: Move to the **Data Preprocessing** stage to clean and prepare the data for analysis and modeling.

## Datasets (Work in Progress)

### Dataset 1: Fighter Statistics
Contains individual fighter profiles and performance metrics. Example columns:
- **Name**: Fighter's name.
- **Fighting Style**: Primary fighting style.
- **Age, Height, Weight**: Demographic and physical attributes.
- **Octagon Debut**: Date of UFC debut.
- **Reach, Leg Reach**: Physical reach measurements.
- **Performance Stats**: Includes metrics like strikes, takedowns, and submissions.
- **Career Record**: Wins, losses, and draws.

### Dataset 2: Match Results 
Captures details of individual matchups. Example columns:
- **Fighter_A, Fighter_B**: Names of the competing fighters.
- **Method**: Method of victory.
- **Round, Time Ended**: Round and time when the fight ended.
- **Winner**: Name of the winning fighter.

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

## Planned Machine Learning Model

- **Algorithm**: Logistic Regression (initial choice for simplicity ).
- **Target output**: Binary outcome (Win/Loss).

## Tech Stack

- **Scraping**: Playwright
- **Data Manipulation**: Pandas
- **Machine Learning (Planned)**: Scikit-learn

## Project Roadmap

1. **Data Gathering**: *(Current Stage)* Scraping and storing raw data.
2. **Data Preprocessing**: Cleaning, transforming, and engineering features.
3. **EDA**: Identifying key trends and insights.
4. **Model Training**: Developing and evaluating the predictive model.
5. **Deployment**: Creating a demonstration interface for predictions.
