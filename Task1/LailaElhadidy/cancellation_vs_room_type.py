import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("hotel.csv")

df["is_canceled"] = df["booking status"].apply(lambda x: 1 if x == "Canceled" else 0)

cancellation_by_room_type = df.groupby("room type")["is_canceled"].mean().reset_index()
cancellation_by_room_type.columns = ["Room Type", "Cancellation Rate"]
cancellation_by_room_type = cancellation_by_room_type.sort_values(by="Cancellation Rate", ascending=False)

plt.figure(figsize=(10, 6))
sns.set_style("whitegrid", {"grid.linestyle": ":", "grid.color": ".8"})
sns.barplot(
    x="Room Type",
    y="Cancellation Rate",
    data=cancellation_by_room_type,
    hue="Room Type",           # ✅ add this
    palette="magma",
    legend=False               # ✅ and this
)
plt.title("Cancellation Rate by Room Type")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
