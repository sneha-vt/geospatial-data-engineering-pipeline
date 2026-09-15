import os
import geopandas as gpd
import psycopg
from dotenv import load_dotenv

load_dotenv()

# Read processed GeoJSON
gdf = gpd.read_file("data/processed/locations.geojson")

# Connect to PostgreSQL/PostGIS
connection = psycopg.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = connection.cursor()

# Insert each record into PostGIS
for _, row in gdf.iterrows():
    cursor.execute(
        """
        INSERT INTO locations
        (location_id, city, country, latitude, longitude, geometry)
        VALUES (%s, %s, %s, %s, %s,
                ST_SetSRID(ST_GeomFromText(%s), 4326))
        ON CONFLICT (location_id) DO NOTHING;
        """,
        (
            int(row["location_id"]),
            row["city"],
            row["country"],
            float(row["latitude"]),
            float(row["longitude"]),
            row["geometry"].wkt
        )
    )

connection.commit()

cursor.close()
connection.close()

print(f"Successfully loaded {len(gdf)} records into PostGIS.")
