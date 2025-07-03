import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("hotel.csv")

df["is_canceled"] = df["booking status"].apply(lambda x: 1 if x == "Canceled" else 0)
df["date of reservation"] = pd.to_datetime(df["date of reservation"], errors="coerce")
df["reservation_month"] = df["date of reservation"].dt.month_name().str.slice(stop=3)

month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

cancellation_by_month = df.groupby("reservation_month")["is_canceled"].mean().reindex(month_order).reset_index()
cancellation_by_month.columns = ["Month", "Cancellation Rate"]

plt.figure(figsize=(12, 7))
sns.set_style("whitegrid", {"grid.linestyle": ":", "grid.color": ".8"})
sns.lineplot(x="Month", y="Cancellation Rate", data=cancellation_by_month, marker="o", color="#2E8B57")
plt.title("Cancellation Rate by Reservation Month")
plt.tight_layout()
plt.show()  # 👈 shows the plot


