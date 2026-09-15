# Geospatial Data Engineering Pipeline

## Overview

A Python and PostgreSQL/PostGIS based data engineering pipeline for processing, validating, transforming, and analysing geographic location data.

The project demonstrates an end-to-end data engineering workflow including data ingestion, data quality validation, geospatial transformation, database loading, pipeline orchestration, logging, and spatial SQL analysis.

## Architecture

```text
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
