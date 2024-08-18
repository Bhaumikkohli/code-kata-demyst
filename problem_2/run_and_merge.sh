#!/bin/bash

# Set the script to exit immediately if any command fails
set -e

# Build and run the csv_generator services
echo "Building and running csv_generator services..."
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up
echo "csv_generator services are running..."

# Wait for the csv_generator services to complete
echo "Waiting for csv_generator services to complete..."
docker-compose -f docker-compose.gen.yml down
echo "csv_generator services have completed."

# Total size of generated CSV based on generated content.
echo "Total size of generated CSV to be parsed is: 2 GB"

# Cleanup
echo "Cleaning up data directory..."
find data -type f ! -name 'output_anonymize_merged.csv' ! -name 'output_gen_merged.csv' -exec rm -f {} +
echo "Cleanup completed."

echo "All tasks completed successfully."
