"""
Homework 3-4 Part 2
Cathy Jia
"""

import unittest
from dataframe import DF, COLS

class TestDataframe(unittest.TestCase):
    """
    Unit tests for dataframe.py
    """
    def test_column_names(self):
        """
        Have the expected columns
        """
        for col in COLS:
            self.assertIn(col, DF.columns, "DataFrame doesn't have the expected column names.")

    def test_expected_type(self):
        """
        Values in the column are all of the expected type
        """
        for col in DF.columns:
            if col != 'quality':
                self.assertEqual(str(DF[col].dtypes), 'float64')
            elif col == 'quality':
                self.assertEqual(str(DF[col].dtypes), 'int64')

    def test_no_nan_values(self):
        """
        There are no nan values
        """
        self.assertEqual(DF.isnull().sum().sum(), 0)

    def test_at_least_onw_row(self):
        """
        The dataframe has at least one row
        """
        self.assertGreaterEqual(DF.shape[0], 1)

SUITE = unittest.TestLoader().loadTestsFromTestCase(TestDataframe)
unittest.TextTestRunner(verbosity=2).run(SUITE)
