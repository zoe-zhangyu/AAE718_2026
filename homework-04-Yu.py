#%%
import os
import pandas as pd
import matplotlib.pyplot as plt

#%%-1
def csv_files(directory):
    files = []
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            files.append(os.path.join(directory, file))
    return files

#%%-2
def load_emission_csv(file_path, year):
    df = pd.read_csv(file_path)
    df["year"] = year
    return df

#%%-3
def load_emissions(directory):
    all_files = csv_files(directory)
    dfs = []

    for file_path in all_files:
        file_name = os.path.basename(file_path)
        year = file_name.replace(".csv", "")
        df = load_emission_csv(file_path, year)
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)

#%%-4
def merge_emissions_country(emissions_directory, country_code_path):
    emissions = load_emissions(emissions_directory)
    country_codes = pd.read_csv(country_code_path)

    country_codes_small = country_codes[["name", "alpha-2", "region", "sub-region"]]

    merged = emissions.merge(
        country_codes_small,
        left_on="Country",
        right_on="name",
        how="left"
    )
    merged = merged.drop(columns=["name"])
    return merged

#%%-5
def emissions_graphs(df):
    df = df.copy()
    df["year"] = pd.to_numeric(df["year"])

    # Graph 1: Total CO2 emissions by region in the latest year
    latest_year = df["year"].max()
    latest = df[df["year"] == latest_year]

    region_total = (
        latest.groupby("region")["Emissions.Type.CO2"]
        .sum()
        .sort_values()
    )

    plt.figure(figsize=(10, 6))
    region_total.plot(kind="barh")
    plt.title(f"Total CO2 Emissions by Region in {latest_year}")
    plt.xlabel("CO2 Emissions")
    plt.ylabel("Region")
    plt.tight_layout()
    plt.savefig("graph1_region_total_co2.png")
    plt.close()

    # Graph 2: Average CO2 emissions by region over all years
    region_mean = (
        df.groupby("region")["Emissions.Type.CO2"]
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(10, 6))
    region_mean.plot(kind="barh")
    plt.title("Average CO2 Emissions by Region")
    plt.xlabel("Average CO2 Emissions")
    plt.ylabel("Region")
    plt.tight_layout()
    plt.savefig("graph2_region_average_co2.png")
    plt.close()

    # Graph 3: CO2 emissions trend for selected countries
    countries = ["United States", "China", "India"]

    trend = (
        df[df["Country"].isin(countries)]
        .groupby(["Country", "year"])["Emissions.Type.CO2"]
        .sum()
        .reset_index()
    )

    plt.figure(figsize=(10, 6))

    for country in countries:
        temp = trend[trend["Country"] == country].sort_values("year")
        plt.plot(temp["year"], temp["Emissions.Type.CO2"], label=country)

    plt.title("CO2 Emissions Trend for Selected Countries")
    plt.xlabel("Year")
    plt.ylabel("CO2 Emissions")
    plt.legend()
    plt.tight_layout()
    plt.savefig("graph3_country_trends_co2.png")
    plt.close()

#%%-6
def dirty_data(file_path):

    df = pd.read_csv(file_path)

    df = df.rename(columns={df.columns[0]: "order id"})

    segments = ["Consumer", "Corporate", "Home Office"]

    ship_modes = ["First Class", "Same Day", "Second Class", "Standard Class"]

    clean_parts = []

    for segment in segments:

        start_col = list(df.columns).index(segment)

        cols = df.columns[start_col:start_col + 4]

        temp = df[["order id"] + list(cols)].copy()

        temp.columns = ["order id"] + ship_modes

        temp = temp.melt(

            id_vars="order id",

            var_name="ship mode",

            value_name="sales"

        )

        temp["segment"] = segment

        clean_parts.append(temp)

    clean_df = pd.concat(clean_parts, ignore_index=True)
    clean_df = clean_df.dropna(subset=["order id", "sales"])
    clean_df = clean_df[clean_df["order id"] != "Order ID"]
    clean_df = clean_df[~clean_df["order id"].str.contains("Total", na=False)]
    clean_df["sales"] = pd.to_numeric(clean_df["sales"], errors="coerce")
    clean_df = clean_df.dropna(subset=["sales"])
    clean_df = clean_df[["order id", "segment", "ship mode", "sales"]]

    return clean_df
#%%-7
def school_data(file_path):
    colspecs = [
        (0, 2),  
        (3, 8),   
        (9, 81), 
        (82, 90), 
        (91, 99), 
        (100, 108),
        (109, 130) 
    ]

    col_names = [
        "state_fips",
        "district_id",
        "district_name",
        "total_population",
        "children_5_17",
        "children_5_17_poverty",
        "file_tag"
    ]

    df = pd.read_fwf(
        file_path,
        colspecs=colspecs,
        names=col_names,
        encoding="latin1"
    )

    df["state_fips"] = df["state_fips"].astype(str).str.zfill(2)
    df["district_id"] = df["district_id"].astype(str)

    numeric_cols = [
        "total_population",
        "children_5_17",
        "children_5_17_poverty"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df
