import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data.csv")

# Show first 5 rows
print(df.head())

# -----------------------------
# HISTOGRAM OF AGE DISTRIBUTION
# -----------------------------

plt.figure(figsize=(8,5))

sns.histplot(df['Age'].dropna(), bins=20, kde=True)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")

plt.show()

# -----------------------------
# BAR CHART OF GENDER
# -----------------------------

plt.figure(figsize=(6,4))

sns.countplot(x='Sex', data=df)

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.show()