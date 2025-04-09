# file: tqdm/contrib/telegram.py:149-154
# asked: {"lines": [154], "branches": []}
# gained: {"lines": [154], "branches": []}

import pytest
from unittest.mock import patch
from tqdm.contrib.telegram import ttgrange

@pytest.mark.parametrize("args, kwargs, expected", [
    ((10,), {}, list(range(10))),
    ((1, 10), {}, list(range(1, 10))),
    ((1, 10, 2), {}, list(range(1, 10, 2))),
])
def test_ttgrange(args, kwargs, expected):
    with patch('tqdm.contrib.telegram.tqdm_telegram') as mock_tqdm_telegram:
        mock_tqdm_telegram.return_value = iter(expected)
        result = list(ttgrange(*args, **kwargs))
        mock_tqdm_telegram.assert_called_once_with(range(*args), **kwargs)
        assert result == expected
