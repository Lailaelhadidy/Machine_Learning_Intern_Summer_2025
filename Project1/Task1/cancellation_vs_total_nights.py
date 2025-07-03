
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("hotel.csv")

df["is_canceled"] = df["booking status"].apply(lambda x: 1 if x == "Canceled" else 0)
df["total_nights"] = df["number of weekend nights"] + df["number of week nights"]

cancellation_by_nights = df.groupby("total_nights")["is_canceled"].mean().reset_index()
cancellation_by_nights.columns = ["Total Number of Nights", "Cancellation Rate"]

plt.figure(figsize=(12, 7))
sns.set_style("whitegrid", {"grid.linestyle": ":", "grid.color": ".8"})
sns.barplot(x="Total Number of Nights", y="Cancellation Rate", data=cancellation_by_nights, palette="magma")
plt.title("Cancellation Rate by Total Number of Nights")
plt.tight_layout()
plt.tight_layout()
plt.show()  # 👈 shows the plot

