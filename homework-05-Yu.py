#%% Import
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%-1
def problem_1(file_path):
    df = pd.read_csv(file_path)

    # Matplotlib scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(df["Height(Inches)"], df["Weight(Pounds)"], alpha=0.4)
    plt.xlabel("Height (Inches)")
    plt.ylabel("Weight (Pounds)")
    plt.title("Height and Weight Scatter Plot: Matplotlib")
    plt.tight_layout()
    plt.savefig("problem1_matplotlib_scatter.png")
    plt.close()

    # Seaborn scatter plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="Height(Inches)", y="Weight(Pounds)", alpha=0.4)
    plt.xlabel("Height (Inches)")
    plt.ylabel("Weight (Pounds)")
    plt.title("Height and Weight Scatter Plot: Seaborn")
    plt.tight_layout()
    plt.savefig("problem1_seaborn_scatter.png")
    plt.close()

#%%-2
def problem_2(file_path):
    df = pd.read_csv(file_path)

    height_sd = df["Height(Inches)"].std()
    weight_sd = df["Weight(Pounds)"].std()

    # Matplotlib histograms
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].hist(df["Height(Inches)"], bins=30, edgecolor="black")
    axes[0].set_title("Height Histogram: Matplotlib")
    axes[0].set_xlabel("Height (Inches)")
    axes[0].set_ylabel("Count")

    axes[1].hist(df["Weight(Pounds)"], bins=30, edgecolor="black")
    axes[1].set_title("Weight Histogram: Matplotlib")
    axes[1].set_xlabel("Weight (Pounds)")
    axes[1].set_ylabel("Count")

    plt.tight_layout()
    plt.savefig("problem2_matplotlib_histograms.png")
    plt.close()

    # Seaborn histograms
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    sns.histplot(data=df, x="Height(Inches)", bins=30, ax=axes[0])
    axes[0].set_title("Height Histogram: Seaborn")
    axes[0].set_xlabel("Height (Inches)")

    sns.histplot(data=df, x="Weight(Pounds)", bins=30, ax=axes[1])
    axes[1].set_title("Weight Histogram: Seaborn")
    axes[1].set_xlabel("Weight (Pounds)")

    plt.tight_layout()
    plt.savefig("problem2_seaborn_histograms.png")
    plt.close()

    return height_sd, weight_sd

#%%-3
def problem_3(file_path):
    df = pd.read_csv(file_path)

    plt.figure(figsize=(9, 6))

    sns.scatterplot(
        data=df,
        x="Height(Inches)",
        y="Weight(Pounds)",
        color="black",
        alpha=0.4,
        s=15
    )

    sns.regplot(
        data=df,
        x="Height(Inches)",
        y="Weight(Pounds)",
        scatter=False,
        color="blue",
        line_kws={"linewidth": 2}
    )

    plt.xlabel("Height (Inches)")
    plt.ylabel("Weight (Pounds)")
    plt.title("Height and Weight with Smooth Line: Seaborn")
    plt.tight_layout()
    plt.savefig("problem3_seaborn_smooth.png")
    plt.close()

#%%-4
def problem_4(file_path):
    df = pd.read_csv(file_path)

    # 1. Total profit over months
    plt.figure(figsize=(8, 5))
    plt.plot(df["month_number"], df["total_profit"], marker="o")
    plt.xlabel("Month")
    plt.ylabel("Total Profit")
    plt.title("Total Profit by Month")
    plt.tight_layout()
    plt.savefig("problem4_total_profit.png")
    plt.close()

    # 2. Product sales over time
    products = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]

    plt.figure(figsize=(10, 6))
    for product in products:
        plt.plot(df["month_number"], df[product], marker="o", label=product)

    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.title("Product Sales Over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig("problem4_product_sales.png")
    plt.close()

    # 3. Relationship between facecream and facewash
    plt.figure(figsize=(7, 5))
    plt.scatter(df["facecream"], df["facewash"])
    plt.xlabel("Facecream Sales")
    plt.ylabel("Facewash Sales")
    plt.title("Relationship between Facecream and Facewash Sales")
    plt.tight_layout()
    plt.savefig("problem4_facecream_facewash.png")
    plt.close()

#%%-5
def problem_5(file_path):
    df = pd.read_csv(file_path)

    # Graph 1: Average crop value by subject
    plt.figure(figsize=(9, 6))
    sns.barplot(
        data=df,
        x="Value",
        y="SUBJECT",
        estimator="mean",
        errorbar=None
    )
    plt.xlabel("Average Value")
    plt.ylabel("Crop")
    plt.title("Average Crop Production/Yield Value by Subject")
    plt.tight_layout()
    plt.savefig("problem5_average_by_crop.png")
    plt.close()

    # Graph 2: Rice value over time for selected locations
    selected = df[
        (df["SUBJECT"] == "RICE") &
        (df["LOCATION"].isin(["USA", "CHN", "IND"]))
    ]

    plt.figure(figsize=(9, 6))
    sns.lineplot(
        data=selected,
        x="TIME",
        y="Value",
        hue="LOCATION",
        errorbar=None
    )
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.title("Rice Value Over Time for Selected Countries")
    plt.tight_layout()
    plt.savefig("problem5_rice_trend.png")
    plt.close()

    # Graph 3: Distribution of values by crop
    plt.figure(figsize=(9, 6))
    sns.boxplot(
        data=df,
        x="Value",
        y="SUBJECT"
    )
    plt.xlabel("Value")
    plt.ylabel("Crop")
    plt.title("Distribution of Crop Values by Subject")
    plt.tight_layout()
    plt.savefig("problem5_boxplot_crop.png")
    plt.close()

#%% Outcome
if __name__ == "__main__":
    problem_1("SOCR-HeightWeight.csv")
    problem_2("SOCR-HeightWeight.csv")
    problem_3("SOCR-HeightWeight.csv")
    problem_4("company_sales_data.csv")
    problem_5("crop_production.csv")
