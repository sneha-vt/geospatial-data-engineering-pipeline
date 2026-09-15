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