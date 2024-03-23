# file mimesis/providers/address.py:151-156
# lines [151, 156]
# branches []

import pytest
from mimesis import Generic

@pytest.fixture
def address():
    generic = Generic('en')
    return generic.address

def test_prefecture(address):
    # Since prefecture is an alias for state, we do not compare their values
    # as they are randomly generated each time. We just check the type.
    prefecture = address.prefecture()
    assert prefecture is not None
    assert isinstance(prefecture, str)
