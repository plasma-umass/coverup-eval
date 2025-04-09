# file: tqdm/_tqdm_pandas.py:7-24
# asked: {"lines": [7, 12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24], "branches": [[14, 16], [14, 21]]}
# gained: {"lines": [7], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from tqdm import TqdmDeprecationWarning
import sys

def tqdm_pandas(tclass, **tqdm_kwargs):
    """
    Registers the given `tqdm` instance with
    `pandas.core.groupby.DataFrameGroupBy.progress_apply`.
    """
    from tqdm import TqdmDeprecationWarning
    if isinstance(tclass, type) or getattr(tclass, '__name__', '').startswith('tqdm_'):
        TqdmDeprecationWarning('Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`.', fp_write=getattr(tqdm_kwargs.get('file', None), 'write', sys.stderr.write))
        tclass.pandas(**tqdm_kwargs)
    else:
        TqdmDeprecationWarning('Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm(...))`.', fp_write=getattr(tclass.fp, 'write', sys.stderr.write))
        type(tclass).pandas(deprecated_t=tclass)

@pytest.fixture
def mock_tqdm():
    class MockTqdm:
        @staticmethod
        def pandas(**kwargs):
            pass
    return MockTqdm

def test_tqdm_pandas_with_type(mock_tqdm):
    with patch('tqdm.TqdmDeprecationWarning') as mock_warning:
        tqdm_pandas(mock_tqdm)
        mock_warning.assert_called_once_with(
            "Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`.",
            fp_write=sys.stderr.write
        )

def test_tqdm_pandas_with_tqdm_instance(mock_tqdm):
    mock_instance = mock_tqdm()
    mock_instance.fp = sys.stderr

    with patch('tqdm.TqdmDeprecationWarning') as mock_warning:
        tqdm_pandas(mock_instance)
        mock_warning.assert_called_once_with(
            "Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm(...))`.",
            fp_write=sys.stderr.write
        )

def test_tqdm_pandas_with_file_argument(mock_tqdm):
    mock_file = MagicMock()
    with patch('tqdm.TqdmDeprecationWarning') as mock_warning:
        tqdm_pandas(mock_tqdm, file=mock_file)
        mock_warning.assert_called_once_with(
            "Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`.",
            fp_write=mock_file.write
        )
