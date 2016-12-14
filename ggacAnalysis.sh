#!/bin/bash

# Generate angCorr.C macro for specific beam diameter
python replace2.py

# Run analysis
grsisort -l -q angCorr.C
