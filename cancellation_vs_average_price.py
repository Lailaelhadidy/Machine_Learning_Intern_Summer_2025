import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("hotel.csv")

df["is_canceled"] = df["booking status"].apply(lambda x: 1 if x == "Canceled" else 0)

plt.figure(figsize=(12, 7))
sns.set_style("whitegrid", {"grid.linestyle": ":", "grid.color": ".8"})
sns.scatterplot(x="average price ", y="is_canceled", hue="is_canceled", data=df, palette="coolwarm", alpha=0.6)
plt.yticks([0, 1], ["Not Canceled", "Canceled"])
plt.xlabel("Average Price per Room per Night")
plt.ylabel("Is Canceled (0=No, 1=Yes)")
plt.title("Cancellation Status vs. Average Price")
plt.tight_layout()
plt.show()  # 👈 shows the plot


