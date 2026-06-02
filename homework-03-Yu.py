import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%-1
# I keep all work inside functions so this file can be imported without
# automatically running code or printing output.

#%%-2
def methane(file_path):
    df = pd.read_csv(file_path)
    df = df.drop(columns=["Unnamed: 0"])
    return df

#%%-3
def methane_aggregation(df):
    subset = df[(df["region"] != "World") & (df["type"] != "Agriculture")]
    subset_sum = subset["emissions"].sum()
    world_total = df[(df["region"] == "World") & (df["type"] != "Agriculture")]["emissions"].sum()
    return subset_sum - world_total

#%%-4
def problem_03(df):
    subset = df[(df["region"] != "World") & (df["type"] == "Agriculture")]
    return subset["segment"].unique()

#%%-5
def region_mean(df):
    return df.groupby("region")["emissions"].mean().reset_index()

#%%-6
def region_total_mean(df):
    total_df = df[df["segment"] == "Total"]
    return total_df.groupby("region")["emissions"].mean().reset_index()

#%%-7
def methane_graphs(df):
    # 1. Aggregated by region
    plt.figure(figsize=(10, 8))
    df.boxplot(column="emissions", by="region", vert=False)
    plt.title("Emissions by Region")
    plt.suptitle("")
    plt.xlabel("Emissions")
    plt.savefig("boxplot_region.png", bbox_inches="tight")
    plt.close()

    # 2. Aggregated by region, excluding World
    df_no_world = df[df["region"] != "World"]
    plt.figure(figsize=(10, 8))
    df_no_world.boxplot(column="emissions", by="region", vert=False)
    plt.title("Emissions by Region, Excluding World")
    plt.suptitle("")
    plt.xlabel("Emissions")
    plt.savefig("boxplot_region_no_world.png", bbox_inches="tight")
    plt.close()

    # 3. Aggregated by region, excluding World and only including Total
    df_total_no_world = df[(df["region"] != "World") & (df["segment"] == "Total")]
    plt.figure(figsize=(10, 8))
    df_total_no_world.boxplot(column="emissions", by="region", vert=False)
    plt.title("Total Emissions by Region, Excluding World")
    plt.suptitle("")
    plt.xlabel("Emissions")
    plt.savefig("boxplot_region_total_no_world.png", bbox_inches="tight")
    plt.close()

    # 4. Aggregated by segment, excluding World and Total
    df_segment = df[(df["region"] != "World") & (df["segment"] != "Total")]
    plt.figure(figsize=(10, 8))
    df_segment.boxplot(column="emissions", by="segment", vert=False)
    plt.title("Emissions by Segment, Excluding World and Total")
    plt.suptitle("")
    plt.xlabel("Emissions")
    plt.savefig("boxplot_segment_no_world_no_total.png", bbox_inches="tight")
    plt.close()

    # 5. One interesting graph: Agriculture only, excluding World
    df_ag = df[(df["region"] != "World") & (df["type"] == "Agriculture")]
    plt.figure(figsize=(10, 8))
    df_ag.boxplot(column="emissions", by="region", vert=False)
    plt.title("Agriculture Emissions by Region, Excluding World")
    plt.suptitle("")
    plt.xlabel("Emissions")
    plt.savefig("boxplot_agriculture_region.png", bbox_inches="tight")
    plt.close()

#%%-8
def animal_crossing(file_path):
    df = pd.read_csv(file_path)
    return df

#%%-9
def sell_price(df):
    row = df.loc[df["Sell"].idxmax()]
    return row["Name"]

#%%-10
def smallest_diff(df):
    df_copy = df.copy()
    df_copy["Buy_numeric"] = pd.to_numeric(df_copy["Buy"], errors="coerce")
    df_copy = df_copy.dropna(subset=["Buy_numeric"])
    df_copy["diff"] = abs(df_copy["Buy_numeric"] - df_copy["Sell"])
    row = df_copy.loc[df_copy["diff"].idxmin()]
    return row["Name"]
