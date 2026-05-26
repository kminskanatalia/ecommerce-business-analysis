import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load data
repeat_purchases = pd.read_csv("repeat_purchases.csv")

# sort data
repeat_purchases = repeat_purchases.groupby("category")["purchase_count"].sum().reset_index()
repeat_purchases = repeat_purchases.sort_values("purchase_count", ascending=False)

# select top 10
top_purchases = repeat_purchases.head(10)

print(top_purchases)

# plot
sns.set_theme(style="ticks")

plt.figure(figsize=(10,6))

sns.barplot(data=top_purchases, x="category", y="purchase_count", palette="light:seagreen_r")

plt.title("Top 10 Categories by Purchase Count")
plt.xlabel("Category")
plt.ylabel("Purchase Count")

plt.xticks(rotation=45, ha ='right', rotation_mode='anchor')

plt.tight_layout()
plt.show()