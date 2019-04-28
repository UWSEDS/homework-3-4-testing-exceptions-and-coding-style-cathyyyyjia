"""
HW2
Cathy Jia
"""

import pandas as pd

# 1

# Find an online data source
URL = 'https://archive.ics.uci.edu/ml/machine-learning'
URL += '-databases/wine-quality/winequality-red.csv'

# Read the online file and create a data frame
DF = pd.read_csv(URL, sep=';', header=0)

# Red wine quality data from UCI machine learning repo
# 1599 rows (observations) * 12 columns (attributes)
# Columns               Data Type
# fixed acidity         'float64'
# volatile acidity      'float64'
# citric acid           'float64'
# residual sugar        'float64'
# chlorides             'float64'
# free sulfur dioxide   'float64'
# total sulfur dioxide  'float64'
# density               'float64'
# pH                    'float64'
# sulphates             'float64'
# alcohol               'float64'
# quality               'int64'


# 2

def test_create_dataframe(df):
    """
    Input - a pandas DataFrame
    Output - return True if the following conditions hold:
             i.   The DataFrame contains only the columns that you specified in #1.
             ii.  The columns contain the correct data type
             iii. There are at least 10 rows in the DataFrame
             else return Falsse
    """

    # i.   The DataFrame contains only the columns that you specified in #1
    # ii.  The columns contain the correct data type
    COLS = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
            'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol',
            'quality']
    for col in df.columns:
        # Check with cols (columns specified in #1)
        if col not in COLS:
            return False
        # All columns should be 'float64' except for 'quality' which is 'int64'
        if col != 'quality':
            if df[col].dtypes != 'float64':
                return False
        else:
            if df[col].dtypes != 'int64':
                return False

    # iii. There are at least 10 rows in the DataFrame
    if len(df) < 10:
        return False

    # All three conditions satisfied
    return True
