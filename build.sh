#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p staticfiles

# Collect static files
python manage.py collectstatic --no-input --clear

# Run migrations
python manage.py migrate