import pytest

import pandas as pd
import warnings

class TestSetMaxColWidth:

    """
    0 warning -> good

    1 warning -> maxwidthcol < 4
              -> maxwidthcol < 0
    
    2 warning -> maxwidthcol < 4 and maxwidthcol < 0
    """


    def TestNoWarnings(self):
        with warnings.catch_warnings() as w:
            df = pd.DataFrame(np.array([['foo', 'bar', 'bim', 'uncomfortably long string']]))
            assert ("uncomfortably long string" in df[0].__str__()) == True)
            
            pd.set_options("max_colwidth", 4)
            assert ("uncomfortably long string" in df[0].__str__()) == False)
            assert ("..." in df[0].__str__()) == True)
            
            pd.set_options("max_colwidth", 5)
            assert ("uncomfortably long string" in df[0].__str__()) == False)
            assert ("u..." in df[0].__str__()) == True)

            pd.set_options("max_colwidth", 6)
            assert ("uncomfortably long string" in df[0].__str__()) == False)
            assert ("un..." in df[0].__str__()) == True)
            
            assert len(w) == 0

    def TestWidthLessThanFourWarning:
        

