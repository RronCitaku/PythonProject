
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archive/weather.csv")

df["Date"] = pd.to_datetime(
    df["year"].astype(str) + "/" + df["day"],
    format="%Y/%m/%d"
)

print(df.head())

average_temperature = df["temperature"].mean()

print("Average temperature:", round(average_temperature, 2))

df["Month"] = df["Date"].dt.month

monthly_average = df.groupby("Month")["temperature"].mean()

print(monthly_average)

monthly_average.plot(kind="bar", title="Monthly Average Temperature")

plt.xlabel("Month")
plt.ylabel("Average Temperature")
plt.show()

hottest_day = df.loc[df["temperature"].idxmax()]
coldest_day = df.loc[df["temperature"].idxmin()]

print("Hottest day:", hottest_day)
print("Coldest day:", coldest_day)

df = df.sort_values("Date")

plt.figure(figsize=(10, 5))

plt.plot(df["Date"], df["temperature"])

plt.title("Temperature Changes Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Fall"

df["Season"] = df["Date"].dt.month.apply(get_season)

seasonal_average = df.groupby("Season")["temperature"].mean()

season_order = ["Winter", "Spring", "Summer", "Fall"]

seasonal_average = seasonal_average.reindex(season_order)

print(seasonal_average)

plt.plot(seasonal_average.index, seasonal_average.values, marker="o")

plt.title("Seasonal Average Temperature")
plt.xlabel("Season")
plt.ylabel("Average Temperature")

plt.show()
