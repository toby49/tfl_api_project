# TfL BikePoint Data Extractor

This script retrieves live Santander Cycle docking station (BikePoint) data from the Transport for London (TfL) API and saves it locally as timestamped JSON files. Each record in the dataset is tagged with the exact extraction time for traceability and time-series analysis.

## Purpose

- Pulls the latest BikePoint data from the TfL API
- Automatically retries failed requests due to rate limiting or temporary server errors
- Saves the full JSON response with a timestamp in the filename
- Appends the extraction timestamp to each BikePoint record for auditing/analysis

## Requirements

Install dependencies before running:
    pip install requests
