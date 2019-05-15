"""
Homework 3-4 Part 1
Cathy Jia
"""

from hw2 import DF # Read dataframe from homework 2

# Generate ValueError exception if the dataframe doesn't have the expected the column names
COLS = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
        'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
        'pH', 'sulphates', 'alcohol', 'quality']
for col in COLS:
    if col not in DF.columns:
        raise ValueError("DataFrame doesn't have the expected column names.")
