import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("hotel.csv")

df["is_canceled"] = df["booking status"].apply(lambda x: 1 if x == "Canceled" else 0)

cancellation_by_lead_time = df.groupby("lead time")["is_canceled"].mean().reset_index()
cancellation_by_lead_time.columns = ["Lead Time (Days)", "Cancellation Rate"]

plt.figure(figsize=(12, 7))
sns.set_style("whitegrid", {"grid.linestyle": ":", "grid.color": ".8"})
sns.lineplot(x="Lead Time (Days)", y="Cancellation Rate", data=cancellation_by_lead_time, marker=".", color="#483D8B")
plt.title("Cancellation Rate vs. Lead Time")

plt.tight_layout()
plt.show()  # 👈 shows the plot
# plt.savefig("cancellation_vs_lead_time.png")  # optional: save if you want
