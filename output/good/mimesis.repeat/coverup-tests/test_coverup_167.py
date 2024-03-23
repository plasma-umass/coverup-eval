# file mimesis/providers/address.py:151-156
# lines [156]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address():
    return Address()

def test_prefecture(address):
    prefecture = address.prefecture()
    assert prefecture is not None
    assert isinstance(prefecture, str)
    # Ensure that prefecture is one of the states provided by mimesis
    assert prefecture in address._data['state']['name']
