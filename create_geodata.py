import pandas as pd
import geopandas as gpd

# Read raw data
df = pd.read_csv("data/raw/locations.csv")

# Convert latitude and longitude into geographic points
gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df["longitude"], df["latitude"]),
    crs="EPSG:4326"
)

# Save processed geospatial data
output_path = "data/processed/locations.geojson"
gdf.to_file(output_path, driver="GeoJSON")

print("Geospatial transformation completed successfully!")
print(f"Saved processed data to: {output_path}")
print(f"Number of records: {len(gdf)}")