# file mimesis/providers/development.py:72-80
# lines [72, 80]
# branches []

import pytest
from mimesis.providers.development import Development

@pytest.fixture
def development_provider():
    return Development()

def test_os(development_provider):
    os_name = development_provider.os()
    assert os_name is not None
    assert isinstance(os_name, str)
