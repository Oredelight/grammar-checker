#!/bin/bash
set -e

# Update package manager and install Java
apt-get update
apt-get install -y default-jre

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
