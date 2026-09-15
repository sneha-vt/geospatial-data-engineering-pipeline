# Geospatial Data Engineering Pipeline

## Overview

A Python and PostgreSQL/PostGIS based data engineering pipeline for processing, validating, transforming, and analysing geographic location data.

The project demonstrates an end-to-end data engineering workflow including data ingestion, data quality validation, geospatial transformation, database loading, pipeline orchestration, logging, and spatial SQL analysis.

## Architecture

Raw CSV
   ↓
Python / Pandas
   ↓
GeoPandas
   ↓
Data Quality Validation
   ↓
GeoJSON
   ↓
PostgreSQL + PostGIS
   ↓
Spatial SQL Analysis

## Technologies

- Python
- Pandas
- GeoPandas
- Shapely
- PyProj
- Fiona
- PostgreSQL
- PostGIS
- SQL

## Pipeline Steps

### 1. Data Ingestion

The pipeline reads location data from a CSV file containing:

- Location ID
- City
- Country
- Latitude
- Longitude

### 2. Geospatial Transformation

Latitude and longitude values are converted into geographic Point geometries using GeoPandas.

The project uses:

**EPSG:4326**

as the coordinate reference system.

The transformed data is stored as a GeoJSON file.

### 3. Data Quality Validation

The pipeline performs automated data quality checks including:

- Required column validation
- Missing value detection
- Latitude range validation
- Longitude range validation
- Duplicate location ID detection
- Geometry validity checks

### 4. PostgreSQL/PostGIS

The transformed geospatial data is loaded into PostgreSQL with PostGIS enabled.

The `locations` table contains:

- Location ID
- City
- Country
- Latitude
- Longitude
- Spatial geometry

The geometry column uses:

```text
geometry(Point, 4326)

## 5. Pipeline Orchestration

The `run_pipeline.py` script orchestrates the complete workflow in sequence:

1. Load raw data
2. Create geospatial data
3. Validate data quality
4. Load data into PostGIS

The pipeline includes error handling and execution logging. If a pipeline step fails, execution stops and the error is recorded in the log file.

## 6. Spatial SQL Analysis

PostGIS spatial functions are used to analyse geographic relationships between locations.

The project includes a spatial query to identify locations within **600 km of Berlin** using:

- `ST_Distance`
- `ST_DWithin`
- Geography-based distance calculations

### Example Result

| City | Country | Distance from Berlin |
|---|---|---:|
| Hamburg | Germany | 255.96 km |
| Copenhagen | Denmark | 355.53 km |
| Munich | Germany | 504.69 km |
| Amsterdam | Netherlands | 577.95 km |

## Project Structure

```text
geospatial-data-engineering-pipeline/
│
├── data/
│   ├── raw/
│   │   └── locations.csv
│   └── processed/
│       └── locations.geojson
│
├── src/
│   ├── create_geodata.py
│   ├── load_data.py
│   ├── load_to_postgis.py
│   ├── run_pipeline.py
│   ├── spatial_analysis.sql
│   ├── test_database.py
│   └── validate_data.py
│
├── .gitignore
└── README.md
