```python
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

def create_clusters(num_techs, geocoded_cache):
    # Load geocoded data
    df = pd.read_csv(geocoded_cache)

    # Extract latitude and longitude
    X = df[['latitude', 'longitude']].values

    # Create KMeans instance
    kmeans = KMeans(n_clusters=num_techs, random_state=0)

    # Fit and predict clusters
    df['cluster'] = kmeans.fit_predict(X)

    # Calculate cluster centers
    centers = kmeans.cluster_centers_

    # Create a DataFrame for cluster centers
    df_centers = pd.DataFrame(centers, columns=['latitude', 'longitude'])

    # Save clusters and centers to csv files
    df.to_csv('clusters.csv', index=False)
    df_centers.to_csv('centers.csv', index=False)

    return 'clusters.csv', 'centers.csv'
```