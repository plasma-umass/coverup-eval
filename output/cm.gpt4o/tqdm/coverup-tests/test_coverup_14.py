# file tqdm/contrib/itertools.py:14-36
# lines [14, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36]
# branches ['30->31', '30->32', '34->exit', '34->35']

import pytest
from unittest import mock
from tqdm.contrib.itertools import product
import itertools
from tqdm import tqdm

def test_product_with_len():
    iterables = [[1, 2], [3, 4]]
    tqdm_kwargs = {'tqdm_class': tqdm, 'desc': 'test'}
    
    result = list(product(*iterables, **tqdm_kwargs))
    
    assert result == [(1, 3), (1, 4), (2, 3), (2, 4)]

def test_product_without_len():
    iterables = [iter([1, 2]), iter([3, 4])]
    tqdm_kwargs = {'tqdm_class': tqdm, 'desc': 'test'}
    
    result = list(product(*iterables, **tqdm_kwargs))
    
    assert result == [(1, 3), (1, 4), (2, 3), (2, 4)]

@pytest.fixture
def mock_tqdm(mocker):
    return mocker.patch('tqdm.contrib.itertools.tqdm_auto', wraps=tqdm)

def test_product_with_mock_tqdm(mock_tqdm):
    iterables = [[1, 2], [3, 4]]
    tqdm_kwargs = {'desc': 'test'}
    
    result = list(product(*iterables, **tqdm_kwargs))
    
    assert result == [(1, 3), (1, 4), (2, 3), (2, 4)]
    assert mock_tqdm.called
    assert mock_tqdm.call_args[1]['total'] == 4
