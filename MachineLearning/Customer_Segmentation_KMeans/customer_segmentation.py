import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def main():
    # Step 1: Load the data
    df = pd.read_csv("Mall_Customers.csv")

    print("Dataset loaded successfully")
    print(df.head())

    print("\nMissing values:")
    print(df.isnull().sum())

    # Step 2: Feature selection
    income_col = next(
        (col for col in df.columns
         if "annual" in col.lower() and "income" in col.lower()),
        None
    )

    spending_col = next(
        (col for col in df.columns
         if "spending" in col.lower() and "score" in col.lower()),
        None
    )

    if income_col is None or spending_col is None:
        raise ValueError(
            f"Could not identify income and spending columns. "
            f"Available columns: {list(df.columns)}"
        )

    X = df[[income_col, spending_col]].copy()

    if X.isnull().any().any():
        raise ValueError("Selected features contain missing values.")

    print("\nSelected features:")
    print(X.head())

    # Step 3: Scale the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("\nScaled data:")
    print(X_scaled[:5])

    # Step 4: Elbow method
    wcss = []

    for k in range(1, 11):
        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(X_scaled)
        wcss.append(model.inertia_)

    print("\nWCSS values:")
    for k, value in enumerate(wcss, start=1):
        print(f"{k} clusters: {value:.2f}")

    # Step 5: Visualize the elbow method
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, 11), wcss, marker="o")
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("WCSS")
    plt.title("Elbow Method for Customer Segmentation")
    plt.xticks(range(1, 11))
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Step 6: Train the final model
    # Four clusters are used as the chosen example.
    model = KMeans(
        n_clusters=4,
        random_state=42,
        n_init=10
    )

    clusters = model.fit_predict(X_scaled)
    df["Cluster"] = clusters

    print("\nDataset with cluster labels:")
    print(df.head(10))

    # Step 7: Visualize customer segments
    plt.figure(figsize=(8, 5))
    plt.scatter(
        X[income_col],
        X[spending_col],
        c=clusters,
        cmap="viridis",
        s=50
    )
    plt.xlabel(income_col)
    plt.ylabel(spending_col)
    plt.title("Customer Segmentation Using K-Means")
    plt.tight_layout()
    plt.show()

    # Step 8: Save the results
    df.to_csv("customer_segments.csv", index=False)
    print("\nClustered dataset saved to customer_segments.csv")


if __name__ == "__main__":
    main()