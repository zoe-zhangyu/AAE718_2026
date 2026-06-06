# Project 03: Climate Data
# AAE 718
# Yu Zhang

#%%
import pandas as pd
import matplotlib.pyplot as plt

#%%
def load_climate_data(file_path):
    df = pd.read_csv(file_path)

    # Convert date column
    df["DATE"] = pd.to_datetime(df["DATE"])

    # Use TMAX and TMIN to create daily average temperature
    # TAVG is missing in this dataset
    df["daily_avg_temp"] = (df["TMAX"] + df["TMIN"]) / 2

    # Create columns
    df["year"] = df["DATE"].dt.year
    df["month"] = df["DATE"].dt.month
    df = df[df["year"] <= 2023]

    # Simplify station names
    df["city"] = df["NAME"].replace({
        "CHICAGO OHARE INTERNATIONAL AIRPORT, IL US": "Chicago",
        "MILWAUKEE MITCHELL AIRPORT, WI US": "Milwaukee",
        "MADISON DANE CO REGIONAL AIRPORT, WI US": "Madison",
        "MINNEAPOLIS ST. PAUL INTERNATIONAL AIRPORT, MN US": "Minneapolis"
    })

    return df


def graph_annual_average_temperature(df):
    annual = (
        df.groupby(["year", "city"])["daily_avg_temp"]
        .mean()
        .reset_index()
    )

    plt.figure(figsize=(10, 6))

    for city in annual["city"].unique():
        city_data = annual[annual["city"] == city]
        plt.plot(
            city_data["year"],
            city_data["daily_avg_temp"],
            marker="o",
            label=city
        )

    plt.xlabel("Year")
    plt.ylabel("Average Temperature (F)")
    plt.title("Annual Average Temperature by City, 2014-2023")
    plt.legend()
    plt.tight_layout()
    plt.savefig("images/annual_average_temperature.png")
    plt.close()


def graph_freezing_days(df):
    # A freezing day is defined as a day with minimum temperature at or below 32 F
    df = df.copy()
    df["freezing_day"] = df["TMIN"] <= 32

    freezing = (
        df.groupby(["year", "city"])["freezing_day"]
        .sum()
        .reset_index()
    )

    plt.figure(figsize=(10, 6))

    for city in freezing["city"].unique():
        city_data = freezing[freezing["city"] == city]
        plt.plot(
            city_data["year"],
            city_data["freezing_day"],
            marker="o",
            label=city
        )

    plt.xlabel("Year")
    plt.ylabel("Number of Freezing Days")
    plt.title("Number of Freezing Days by City, 2014-2023")
    plt.legend()
    plt.tight_layout()
    plt.savefig("images/freezing_days.png")
    plt.close()


def graph_annual_snowfall(df):
    snowfall = (
        df.groupby(["year", "city"])["SNOW"]
        .sum()
        .reset_index()
    )

    plt.figure(figsize=(10, 6))

    for city in snowfall["city"].unique():
        city_data = snowfall[snowfall["city"] == city]
        plt.plot(
            city_data["year"],
            city_data["SNOW"],
            marker="o",
            label=city
        )

    plt.xlabel("Year")
    plt.ylabel("Total Snowfall (inches)")
    plt.title("Annual Snowfall by City, 2014-2023")
    plt.legend()
    plt.tight_layout()
    plt.savefig("images/annual_snowfall.png")
    plt.close()


def summarize_data(df):
    print("Rows and columns:", df.shape)
    print()
    print("Stations:")
    print(df["NAME"].unique())
    print()
    print("Date range:")
    print(df["DATE"].min(), "to", df["DATE"].max())
    print()
    print("Missing values:")
    print(df[["SNOW", "SNWD", "TAVG", "TMAX", "TMIN"]].isna().sum())
    print()
    print("Number of years by city:")
    print(df.groupby("city")["year"].nunique())


if __name__ == "__main__":
    file_path = "climate_project_data.csv"

    climate = load_climate_data(file_path)

    summarize_data(climate)

    graph_annual_average_temperature(climate)
    graph_freezing_days(climate)
    graph_annual_snowfall(climate)

    print("Graphs saved in the images folder.")