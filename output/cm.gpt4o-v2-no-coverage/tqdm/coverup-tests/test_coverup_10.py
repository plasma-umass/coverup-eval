# file: tqdm/contrib/itertools.py:14-36
# asked: {"lines": [14, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36], "branches": [[30, 31], [30, 32], [34, 0], [34, 35]]}
# gained: {"lines": [14, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36], "branches": [[30, 31], [30, 32], [34, 0], [34, 35]]}

import pytest
from unittest.mock import MagicMock
from tqdm.contrib.itertools import product

def test_product_with_lengths(mocker):
    mock_tqdm = mocker.patch('tqdm.auto.tqdm', autospec=True)
    mock_tqdm.return_value.__enter__.return_value = mock_tqdm
    iter1 = [1, 2]
    iter2 = [3, 4]
    result = list(product(iter1, iter2, tqdm_class=mock_tqdm))
    assert result == [(1, 3), (1, 4), (2, 3), (2, 4)]
    assert mock_tqdm.update.call_count == 4
    mock_tqdm.assert_called_once()
    assert mock_tqdm.call_args[1]['total'] == 4

def test_product_without_lengths(mocker):
    mock_tqdm = mocker.patch('tqdm.auto.tqdm', autospec=True)
    mock_tqdm.return_value.__enter__.return_value = mock_tqdm
    iter1 = iter([1, 2])
    iter2 = iter([3, 4])
    result = list(product(iter1, iter2, tqdm_class=mock_tqdm))
    assert result == [(1, 3), (1, 4), (2, 3), (2, 4)]
    assert mock_tqdm.update.call_count == 4
    mock_tqdm.assert_called_once()
    assert 'total' not in mock_tqdm.call_args[1]
