#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install it and try again."
    exit 1
fi

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install build
pip install build

# Build the package
python -m build

# Install the package (edit the path to the wheel file if needed)
pip install dist/cw_cli-0.1.0-py3-none-any.whl

# List the shortcuts
ls -l venv/bin/cw