# file tqdm/_tqdm_pandas.py:7-24
# lines [7, 12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24]
# branches ['14->16', '14->21']

import pytest
from tqdm import tqdm
from tqdm._tqdm_pandas import tqdm_pandas
from unittest.mock import Mock
import sys

class MockTqdm:
    @classmethod
    def pandas(cls, **kwargs):
        pass

def test_tqdm_pandas_with_class(mocker):
    mock_warning = mocker.patch('tqdm.TqdmDeprecationWarning')
    mock_write = Mock()
    tqdm_pandas(MockTqdm, file=Mock(write=mock_write))
    mock_warning.assert_called_once_with(
        "Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`.",
        fp_write=mock_write
    )

@pytest.fixture(autouse=True)
def clean_up():
    # This fixture is used to ensure that the tqdm global state is cleaned up after each test
    yield
    tqdm._instances.clear()

# Skip the test if pandas is not installed
@pytest.mark.skipif('pandas' not in sys.modules, reason="requires the pandas library")
def test_tqdm_pandas_with_instance(mocker):
    mock_warning = mocker.patch('tqdm.TqdmDeprecationWarning')
    mock_write = Mock()
    tqdm_instance = tqdm()
    tqdm_instance.fp = Mock(write=mock_write)
    tqdm_pandas(tqdm_instance)
    mock_warning.assert_called_once_with(
        "Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm(...))`.",
        fp_write=mock_write
    )
    tqdm_instance.close()
