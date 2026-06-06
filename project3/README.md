# Climate Data Project

## Project Description

This project analyzes daily climate data from four Upper Midwest cities from 2014 to 2023. The main question is:

**Are winters and annual weather patterns changing in selected Upper Midwest cities?**

The four cities in this project are:

- Chicago, Illinois
- Madison, Wisconsin
- Milwaukee, Wisconsin
- Minneapolis, Minnesota

The project uses daily weather data to compare temperature, snowfall, and freezing days across these cities.

## Data

The data come from NOAA Daily Summaries. The four weather stations are:

- Chicago O'Hare International Airport, IL
- Madison Dane County Regional Airport, WI
- Milwaukee Mitchell Airport, WI
- Minneapolis St. Paul International Airport, MN

The data file is:

`climate_project_data.csv`

The dataset covers the ten complete years from 2014 to 2023. The downloaded file also included January 1, 2024, but I removed 2024 because it is not a complete year.

The main variables used are:

- `TMAX`: daily maximum temperature
- `TMIN`: daily minimum temperature
- `SNOW`: daily snowfall
- `SNWD`: daily snow depth

The `TAVG` column was missing for all observations, so I calculated daily average temperature as:

`daily_avg_temp = (TMAX + TMIN) / 2`

## Files in This Repository

- `Project3_Yu.py`: Python code for cleaning data and making graphs
- `climate_project_data.csv`: NOAA climate data used in the project
- `report.md`: written report in Markdown
- `README.md`: project description and instructions
- `.gitignore`: files ignored by Git
- `images/`: folder containing generated graphs

## How to Run the Code

1. Make sure `climate_project_data.csv` is in the project folder.
2. Make sure there is a folder called `images`.
3. Run the Python script:

```bash
python Project3_Yu.py