import pytest
from pandas.core.internals.blocks import Block, ExtensionBlock
import pandas as pd
import pandas._testing as tm
import numpy as np
from pandas.arrays import StringArray, IntegerArray
from pandas.core.construction import array

class TestFix32450:
    def test_astype_string_no_NA(self):
        # create np array with no NA
        test_data = np.array(['1','2'], dtype='object')
        # create a extension block StringArray
        block = ExtensionBlock(StringArray(test_data),placement=np.arange(len(test_data)))
        # convert to Int64
        block = block.astype('Int64')
        result = block.values
        v = np.array([1, 2])
        m = np.array([False, False])
        # Expected is a IntegerArray
        expected = IntegerArray(values = v, mask = m)
        tm.assert_extension_array_equal(result,expected)

    def test_astype_string_NA(self):
        # create np array with NA
        test_data = np.array(['1', pd.NA, '2']) 
        # create a extension block StringArray
        block = ExtensionBlock(StringArray(test_data),placement=np.arange(len(test_data)))
         # convert to Int64
        block = block.astype('Int64')
        result = block.values
        v = np.array([1, 0, 2])
        m = np.array([False, True, False])
        # Expected is a IntegerArray
        expected = IntegerArray(values = v, mask = m)
        tm.assert_extension_array_equal(result,expected)
    
    def test_astype_object_NA(self):
        # create np array with NA
        test_data = np.array(['1', pd.NA, '2'])
        # create a extension block Object Array
        block = ExtensionBlock(array(test_data),placement=np.arange(len(test_data)))
        # convert to Int64
        block = block.astype('Int64')
        result = block.values
        v = np.array([1, 0, 2])
        m = np.array([False, True, False])
        # Expected is a IntegerArray
        expected = IntegerArray(values = v, mask = m)
        tm.assert_extension_array_equal(result,expected)
    
    def test_astype_object_No_NA(self):
        # create np array with no NA
        test_data = np.array(['1','2'], dtype='object')
        # create a extension block Object Array
        block = ExtensionBlock(array(test_data),placement=np.arange(len(test_data)))
        # convert to Int64
        block = block.astype('Int64')
        result = block.values
        v = np.array([1, 2])
        m = np.array([False, False])
        # Expected is a IntegerArray
        expected = IntegerArray(values = v, mask = m)
        tm.assert_extension_array_equal(result,expected)