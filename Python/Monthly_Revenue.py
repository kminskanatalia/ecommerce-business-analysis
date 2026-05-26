import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load data
monthly_data = pd.read_csv("revenue_by_month.csv")

# convert date
monthly_data["month"] = pd.to_datetime(monthly_data["month"])

# filter only 2017
monthly_data = monthly_data[monthly_data["month"].dt.year == 2017]

# create month columns
monthly_data["month_name"] = monthly_data["month"].dt.strftime("%b")
monthly_data["month_number"] = monthly_data["month"].dt.month

# sort chronologically
monthly_data = monthly_data.sort_values("month_number")

# style
sns.set_theme(style="white", palette="pastel")

plt.figure(figsize=(10,6))

ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, p: f'${int(y/1000)}K'))

sns.lineplot(
    data=monthly_data,
    x="month_name",
    y="monthly_revenue",
    marker="o",
    color="seagreen"
)

# quarter separators
plt.axvline(2.5, color='grey', linestyle='--', alpha=0.5)
plt.axvline(5.5, color='grey', linestyle='--', alpha=0.5)
plt.axvline(8.5, color='grey', linestyle='--', alpha=0.5)

plt.title("Monthly Revenue Trend (2017)")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()