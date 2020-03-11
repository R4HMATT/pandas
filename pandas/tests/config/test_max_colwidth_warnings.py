import pytest

import pandas as pd
import numpy as np
import warnings

def test_NoWarnings():
    ''' 
    Function to test in cases where warnings will not occur
    '''
    with warnings.catch_warnings(record=True) as w:
        # create a DataFrame array to use for testing
        df = pd.DataFrame(np.array([['foo', 'bar', 'bim', 'uncomfortably long string']]))
        assert ("uncomfortably long string" in df[0:].__str__()) == True
        
        # Test for eclipsing 4+,5+,6+ for the max_colwidth
        pd.set_option("max_colwidth", 4)
        assert ("uncomfortably long string" in df[0:].__str__()) == False
        assert ("..." in df[0:].__str__()) == True
        
        pd.set_option("max_colwidth", 5)
        assert ("uncomfortably long string" in df[0:].__str__()) == False
        assert ("u..." in df[0:].__str__()) == True

        pd.set_option("max_colwidth", 6)
        assert ("uncomfortably long string" in df[0:].__str__()) == False
        assert ("un..." in df[0:].__str__()) == True
        
        # ensure that no warnings were raised
        assert len(w) == 0

def test_NegativeIntWarnings():
    ''' 
    Function to test in cases where a negative integer warning will occur
    '''
    with warnings.catch_warnings(record=True) as w:            
        # Test for eclipsing negative number for the max_colwidth
        pd.set_option("max_colwidth", -1)

        # ensure the length of w is 2
        assert(len(w) == 2)

        # ensure that no warnings were raised
        assert str(w[-2].message) == "Passing a negative integer is deprecated in version 1.0 and will not be supported in future version. Instead, use None to not limit the column width."

def test_InvalidIntWarnings():
    ''' 
    Function to test in cases where a user provides a number between 0-3 (inclusive).
    '''
    with warnings.catch_warnings(record=True) as w:            
        # Test for eclipsing negative number for the max_colwidth
        pd.set_option("max_colwidth", 0)
        
        # ensure that no warnings were raised
        assert str(w[-1].message) == "Passing a integer that is less than 4 will have no affect due to the string size of the ellipse size being 3."

    

