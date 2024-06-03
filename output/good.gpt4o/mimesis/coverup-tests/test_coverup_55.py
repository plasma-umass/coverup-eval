# file mimesis/providers/internet.py:220-236
# lines [220, 230, 231, 233, 234, 236]
# branches ['233->234', '233->236']

import pytest
from mimesis.providers.internet import Internet
from mimesis.data import HASHTAGS

def test_hashtags(mocker):
    internet = Internet()

    # Mock the random choice to control the output
    mocker.patch('mimesis.random.Random.choice', return_value='test')

    # Test with quantity = 1
    result = internet.hashtags(1)
    assert result == '#test', f"Expected '#test', but got {result}"

    # Test with quantity > 1
    result = internet.hashtags(3)
    assert result == ['#test', '#test', '#test'], f"Expected ['#test', '#test', '#test'], but got {result}"

    # Test with default quantity
    result = internet.hashtags()
    assert result == ['#test', '#test', '#test', '#test'], f"Expected ['#test', '#test', '#test', '#test'], but got {result}"

    # Clean up the mock
    mocker.stopall()
