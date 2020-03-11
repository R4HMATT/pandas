import pytest

import pandas as pd
import pandas._testing as tm

import warnings

class TestToJsonWarnings:

    def test_compression_with_paths(self):
        with warnings.catch_warnings(record=True) as w:
            with tm.ensure_clean() as path:
                df = pd.DataFrame({"a": [1, 2, 3, 4], "b": ["A", "B", "C", "D"],})
                json_df = df.to_json(path, compression="gzip")
            assert len(w) == 0
    
    def test_compression_without_path(self):
        with warnings.catch_warnings(record=True) as w: 
            df = pd.DataFrame({"a": [1, 2, 3, 4], "b": ["A", "B", "C", "D"],})
            json_df = df.to_json(compression="gzip")
            assert len(w) == 1
            assert issubclass(w[0].category, Warning)
            assert "without compression" in str(w[0].message)


