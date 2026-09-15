import pandas as pd
import geopandas as gpd

# Read processed geospatial data
gdf = gpd.read_file("data/processed/locations.geojson")

print("Starting data quality checks...\n")

# 1. Check required columns
required_columns = [
    "location_id",
    "city",
    "country",
    "latitude",
    "longitude",
    "geometry"
]

missing_columns = [
    column for column in required_columns
    if column not in gdf.columns
]

if missing_columns:
    print("FAIL: Missing columns:", missing_columns)
else:
    print("PASS: Required columns are present")

# 2. Check missing values
missing_values = gdf[
    ["location_id", "city", "country", "latitude", "longitude"]
].isnull().sum()

print("\nMissing values:")
print(missing_values)

# 3. Check coordinate ranges
invalid_latitude = ~gdf["latitude"].between(-90, 90)
invalid_longitude = ~gdf["longitude"].between(-180, 180)

print("\nInvalid latitude records:", invalid_latitude.sum())
print("Invalid longitude records:", invalid_longitude.sum())

# 4. Check duplicate IDs
duplicate_ids = gdf["location_id"].duplicated().sum()

print("Duplicate location IDs:", duplicate_ids)

# 5. Check geometry validity
invalid_geometry = (~gdf.geometry.is_valid).sum()

print("Invalid geometries:", invalid_geometry)

print("\nData quality checks completed.")
