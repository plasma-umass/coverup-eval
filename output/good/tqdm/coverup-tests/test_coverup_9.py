# file tqdm/contrib/telegram.py:149-154
# lines [149, 154]
# branches []

import pytest
from unittest.mock import patch
from tqdm.contrib.telegram import tqdm_telegram, ttgrange

# Assuming _range is defined somewhere in the tqdm.contrib.telegram module
# If not, this mock will simulate the behavior of xrange in Python 2 or range in Python 3
with patch('tqdm.contrib.telegram._range', side_effect=range) as mock_range:
    def test_ttgrange():
        with patch('tqdm.contrib.telegram.tqdm_telegram') as mock_tqdm_telegram:
            # Call the function with some test arguments
            list(ttgrange(5))

            # Check if _range was called correctly
            mock_range.assert_called_once_with(5)

            # Check if tqdm_telegram was called correctly
            mock_tqdm_telegram.assert_called_once()

            # Check if tqdm_telegram was called with the result of _range
            args, kwargs = mock_tqdm_telegram.call_args
            assert list(args[0]) == list(range(5))

    # Run the test
    test_ttgrange()
