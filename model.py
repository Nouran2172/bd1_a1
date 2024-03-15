from sklearn.cluster import KMeans
import pandas as pd


def k_means(dataframe):
    # Example: Implement K-means algorithm
 # Select columns suitable for K-means
    selected_columns = ['Survived', 'Pclass','SibSp','Parch','Fare', 'Sex_female','Sex_male','Embarked_C','Embarked_Q','Embarked_S']

# Apply K-means algorithm
    k = 3
    kmeans = KMeans(n_clusters=k, random_state=0).fit(dataframe[selected_columns])

# Get the labels of the clusters
    labels = kmeans.labels_

# Count the number of records in each cluster
    cluster_counts = pd.Series(labels).value_counts()
    
    # Save cluster counts to text file
    with open('k.txt', 'w') as f:
        for cluster, count in cluster_counts.items():
            f.write(f"Cluster {cluster}: {count} records\n")

def main():
    # Load the dataset
    dataframe = pd.read_csv('res_dpre.csv')
    
    # Implement K-means
    k_means(dataframe)

if __name__ == "__main__":
    main()