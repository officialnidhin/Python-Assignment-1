import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("taxis")

print(df.head())
print(df.info())
print(df.isnull().sum())

# Fill missing numeric values with the median
numeric_columns = df.select_dtypes(include="number").columns
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill missing text values with the most common value
categorical_columns = df.select_dtypes(include="object").columns
for column in categorical_columns:
    if df[column].notna().any():
        df[column] = df[column].fillna(df[column].mode()[0])

# Convert pickup time to datetime
df["pickup"] = pd.to_datetime(df["pickup"], errors="coerce")

# Remove rows missing information needed for the charts
needed_columns = [
    "pickup", "fare", "pickup_borough", "payment",
    "distance", "tip", "total", "pickup_zone"
]
df = df.dropna(subset=needed_columns)

print(df.isnull().sum())

# Fill missing numeric values with the median
numeric_columns = df.select_dtypes(include="number").columns
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill missing text values with the most common value
categorical_columns = df.select_dtypes(include="object").columns
for column in categorical_columns:
    if df[column].notna().any():
        df[column] = df[column].fillna(df[column].mode()[0])

# Convert pickup time to datetime
df["pickup"] = pd.to_datetime(df["pickup"], errors="coerce")

# Remove rows missing information needed for the charts
needed_columns = [
    "pickup", "fare", "pickup_borough", "payment",
    "distance", "tip", "total", "pickup_zone"
]
df = df.dropna(subset=needed_columns)

print(df.isnull().sum())

df_sorted = df.sort_values("pickup")

plt.figure(figsize=(10, 5))
plt.plot(df_sorted["pickup"], df_sorted["fare"])
plt.title("Fare Over Pickup Time")
plt.xlabel("Pickup time")
plt.ylabel("Fare")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

fare_by_borough = df.groupby("pickup_borough")["fare"].sum()

fare_by_borough.plot(kind="bar", figsize=(8, 5), color="skyblue")
plt.title("Total Fare by Pickup Borough")
plt.xlabel("Pickup borough")
plt.ylabel("Total fare")
plt.tight_layout()
plt.show()

payment_counts = df["payment"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(payment_counts, labels=payment_counts.index, autopct="%1.1f%%")
plt.title("Trips by Payment Method")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["distance"], bins=20, edgecolor="black")
plt.title("Distribution of Trip Distance")
plt.xlabel("Distance")
plt.ylabel("Number of trips")
plt.tight_layout()
plt.show()

sns.countplot(data=df, x="pickup_borough")
plt.title("Number of Trips by Pickup Borough")
plt.xlabel("Pickup borough")
plt.ylabel("Number of trips")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

sns.scatterplot(
    data=df,
    x="distance",
    y="fare",
    hue="pickup_borough",
    alpha=0.6
)
plt.title("Distance and Fare by Pickup Borough")
plt.tight_layout()
plt.show()

sns.scatterplot(
    data=df,
    x="distance",
    y="fare",
    hue="pickup_borough",
    alpha=0.6
)
plt.title("Distance and Fare by Pickup Borough")
plt.tight_layout()
plt.show()

corr_columns = ["distance", "fare", "tip", "tolls", "total"]
correlation = df[corr_columns].corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Trip Variables")
plt.tight_layout()
plt.show()

sns.pairplot(
    data=df,
    vars=["distance", "fare", "tip", "total"],
    hue="pickup_zone"
)
plt.show()                           

sns.violinplot(data=df, x="payment", y="fare")
plt.title("Fare Distribution by Payment Method")
plt.xlabel("Payment method")
plt.ylabel("Fare")
plt.tight_layout()
plt.show()
