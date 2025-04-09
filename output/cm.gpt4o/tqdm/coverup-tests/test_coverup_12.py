# file tqdm/_tqdm_pandas.py:7-24
# lines [7, 12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24]
# branches ['14->16', '14->21']

import pytest
from unittest.mock import MagicMock, patch
from tqdm import tqdm
import sys

def test_tqdm_pandas_deprecation_warning_delayed_adapter_case(mocker):
    from tqdm._tqdm_pandas import tqdm_pandas
    from tqdm import TqdmDeprecationWarning

    mock_tqdm_class = MagicMock()
    mock_tqdm_class.__name__ = 'tqdm_foo'
    mock_file = MagicMock()
    mocker.patch('sys.stderr.write')

    with patch('tqdm.TqdmDeprecationWarning', side_effect=lambda msg, fp_write: TqdmDeprecationWarning(msg)) as mock_warning:
        tqdm_pandas(mock_tqdm_class, file=mock_file)
        mock_warning.assert_called_once_with(
            "Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm, ...)`.",
            fp_write=mock_file.write
        )
        mock_tqdm_class.pandas.assert_called_once_with(file=mock_file)

def test_tqdm_pandas_deprecation_warning_instance_case(mocker):
    from tqdm._tqdm_pandas import tqdm_pandas
    from tqdm import TqdmDeprecationWarning

    mock_tqdm_instance = MagicMock()
    mock_tqdm_instance.fp = MagicMock()
    mock_tqdm_instance.__class__.pandas = MagicMock()
    mock_file = MagicMock()
    mocker.patch('sys.stderr.write')

    with patch('tqdm.TqdmDeprecationWarning', side_effect=lambda msg, fp_write: TqdmDeprecationWarning(msg)) as mock_warning:
        tqdm_pandas(mock_tqdm_instance)
        mock_warning.assert_called_once_with(
            "Please use `tqdm.pandas(...)` instead of `tqdm_pandas(tqdm(...))`.",
            fp_write=mock_tqdm_instance.fp.write
        )
        mock_tqdm_instance.__class__.pandas.assert_called_once_with(deprecated_t=mock_tqdm_instance)
