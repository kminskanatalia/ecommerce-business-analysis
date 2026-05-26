import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import seaborn as sns

# load data
month_data = pd.read_csv("revenue_by_month.csv")

month_data["month"] = pd.to_datetime(month_data["month"])

# rename for prophet
df = month_data.rename(columns={
    "month": "ds",
    "monthly_revenue": "y"
})

month_data["month_name"] = month_data["month"].dt.strftime("%Y%b")
month_data["month_number"] = month_data["month"].dt.month
month_data = month_data.sort_values("month_number")

# create model
model = Prophet()
model.fit(df)

# future months
future = model.make_future_dataframe(periods=12, freq="MS")

forecast = model.predict(future)

# split actual vs forecast
actual = forecast[forecast["ds"] > "2017-12-31"]
future_forecast = forecast[forecast["ds"] > df["ds"].max()]

sns.set_theme(style="ticks")

plt.figure(figsize=(16,6))

# actual data
sns.lineplot(
    data=actual,
    x="ds",
    y="yhat",
    label="Actual Revenue",
    color="seagreen",
    marker="o"
)

# forecast
sns.lineplot(
    data=future_forecast,
    x="ds",
    y="yhat",
    label="Forecast",
    color="salmon",
    linestyle="--",
    marker="o"
)

plt.title("Revenue Forecast (Next 12 Months)")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.gca().yaxis.set_major_formatter(
    plt.FuncFormatter(lambda y, _: f'${int(y/1000)}K')
)

plt.tight_layout()
plt.show()