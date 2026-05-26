import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import seaborn as sns

# load data
volume = pd.read_csv("purchase_volume_monthly.csv")

volume["month"] = pd.to_datetime(volume["month"])

df = volume.rename(columns={
    "month": "ds",
    "order_count": "y"
})

model = Prophet(yearly_seasonality=True)


model.fit(df)
future = model.make_future_dataframe(periods=12, freq="MS")
forecast = model.predict(future)

actual = forecast[forecast["ds"] > "2017-12-31"]
future_forecast = forecast[forecast["ds"] > df["ds"].max()]

sns.set_theme(style="ticks")

plt.figure(figsize=(16,6))

sns.lineplot(
    data=actual,
    x="ds",
    y="yhat",
    label="Actual Purchases",
    color="royalblue",
    marker="o"
)

sns.lineplot(
    data=future_forecast,
    x="ds",
    y="yhat",
    label="Forecast",
    color="orange",
    linestyle="--",
    marker="o"
)

plt.title("Purchase Volume Forecast")
plt.xlabel("Month")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()