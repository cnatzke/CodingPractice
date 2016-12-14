#!/bin/bash

# Generate angCorr.C macro for specific beam diameter
python replace2.py

echo "___________________________"
echo "Starting the Analysis"
echo "___________________________"
# Run analysis
grsisort -l -q angCorr.C

echo "___________________________"
echo "Cleaning up"
echo "___________________________"

rm AutoDict*

echo "___________________________"
echo "Done"
echo "___________________________"
