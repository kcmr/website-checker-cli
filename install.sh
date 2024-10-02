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

# Install the dependencies and the package
pip install -e .

# Create an alias for the cw command
echo "alias cw='$(pwd)/venv/bin/cw'" >> ~/.bashrc

echo "Installation completed. Please restart your terminal or run 'source ~/.bashrc' to use the 'cw' command."