import pytest

import pandas as pd
import pandas._testing as tm

import warnings

class TestDataFrameToJsonCompressionWarnings:

    # testing that to_json with a path and compression specified does not cause any warnings
    def test_warning_compression_with_paths(self):
        with warnings.catch_warnings(record=True) as w:
            with tm.ensure_clean() as path:
                df = pd.DataFrame({"a": [1, 2, 3, 4], "b": ["A", "B", "C", "D"],})
                json_df = df.to_json(path, compression="gzip")
            assert len(w) == 0
    
    # test that to_json does generate the specified warning, when compression is specified and path is not
    def test_warning_compression_without_path(self):
        with warnings.catch_warnings(record=True) as w: 
            df = pd.DataFrame({"a": [1, 2, 3, 4], "b": ["A", "B", "C", "D"],})
            json_df = df.to_json(compression="gzip")
            assert len(w) == 1
            assert issubclass(w[0].category, Warning)
            assert "without compression" in str(w[0].message)
    
    # test that to_json without compression but path specified generates no warning
    def test_warning_path_without_compression(self):
        with warnings.catch_warnings(record=True) as w: 
            df = pd.DataFrame({"a": [1, 2, 3, 4], "b": ["A", "B", "C", "D"],})
            with tm.ensure_clean() as path:
                json_df = df.to_json(path)
        assert len(w) == 0


class TestSeriesToJsonCompressionWarnings:
    # testing that to_json with a path and compression specified does not cause any warnings
    def test_warning_compression_with_paths(self):
        with warnings.catch_warnings(record=True) as w:
            with tm.ensure_clean() as path:
                s = pd.Series([1, 2, 3, 4])
                json_df = s.to_json(path, compression="gzip")
            assert len(w) == 0

    # test that to_json does generate the specified warning, when compression is specified and path is not
    def test_warning_compression_without_path(self):
        with warnings.catch_warnings(record=True) as w:
            s = pd.Series([1, 2, 3, 4])
            json_df = s.to_json(compression="gzip")
            assert len(w) == 1
            assert issubclass(w[0].category, Warning)
            assert "without compression" in str(w[0].message)

    # test that to_json without compression but path specified generates no warning
    def test_warning_path_without_compression(self):
        with warnings.catch_warnings(record=True) as w: 
            s = pd.Series([1, 2, 3, 4])
            with tm.ensure_clean() as path:
                json_s = s.to_json(path)
        assert len(w) == 0


