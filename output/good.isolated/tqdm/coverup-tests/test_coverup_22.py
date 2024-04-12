# file tqdm/contrib/itertools.py:14-36
# lines [14, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36]
# branches ['30->31', '30->32', '34->exit', '34->35']

import pytest
from unittest.mock import Mock
from tqdm.contrib.itertools import product
from tqdm import tqdm

# Mock tqdm to avoid printing during tests
@pytest.fixture
def mock_tqdm(mocker):
    mock = mocker.patch('tqdm.contrib.itertools.tqdm_auto', autospec=True)
    mock.return_value.__enter__.return_value.update = Mock()
    return mock

def test_product_with_non_sized_iterables(mock_tqdm):
    # Create a generator which does not support len()
    def gen():
        for i in range(3):
            yield i

    # Convert the generator to an iterable that does not support len()
    non_sized_iterable = (x for x in gen())

    # Expected result from itertools.product
    expected_result = list((i,) for i in range(3))

    # Run the product function with the non_sized_iterable
    result = list(product(non_sized_iterable))

    # Assert that the result matches the expected result
    assert result == expected_result

    # Assert that tqdm was called without a total since len() is not supported
    mock_tqdm.assert_called_once_with()

    # Assert that the update method was called the correct number of times
    assert mock_tqdm.return_value.__enter__.return_value.update.call_count == len(expected_result)
