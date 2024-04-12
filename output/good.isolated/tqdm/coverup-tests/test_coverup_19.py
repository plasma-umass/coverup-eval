# file tqdm/_tqdm_pandas.py:7-24
# lines [15, 21, 22, 23, 24]
# branches ['14->21']

import pytest
from tqdm import tqdm
from tqdm._tqdm_pandas import tqdm_pandas
from unittest.mock import Mock
import sys

class MockTqdm:
    @classmethod
    def pandas(cls, **kwargs):
        pass

@pytest.fixture
def mock_pandas_module(mocker):
    pandas_mock = mocker.patch.dict('sys.modules', {
        'pandas': Mock(),
        'pandas.core': Mock(),
        'pandas.core.frame': Mock(),
        'pandas.core.series': Mock(),
        'pandas.core.groupby': Mock(),
        'pandas.core.groupby.DataFrameGroupBy': Mock(),
        'pandas.core.groupby.SeriesGroupBy': Mock(),
    })
    return pandas_mock

def test_tqdm_pandas_deprecation_warning(mocker, mock_pandas_module):
    # Mock the warning to check if it's called
    mock_warning = mocker.patch('tqdm.TqdmDeprecationWarning')

    # Case 1: tclass is a type and should trigger the first deprecation warning
    tqdm_pandas(MockTqdm, file=Mock(write=lambda x: x))
    mock_warning.assert_called_once_with(
        "Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`.",
        fp_write=mocker.ANY
    )
    mock_warning.reset_mock()

    # Case 2: tclass is an instance and should trigger the second deprecation warning
    tqdm_instance = tqdm(total=100)
    tqdm_instance.fp = Mock(write=lambda x: x)
    tqdm_pandas(tqdm_instance)
    mock_warning.assert_called_once_with(
        "Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm(...))`.",
        fp_write=mocker.ANY
    )

    # Clean up by closing the tqdm instance
    tqdm_instance.close()
