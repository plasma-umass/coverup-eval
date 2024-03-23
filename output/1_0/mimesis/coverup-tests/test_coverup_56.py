# file mimesis/providers/science.py:25-28
# lines [25, 26, 28]
# branches []

import pytest
from mimesis.providers.science import Science
from mimesis import Generic

@pytest.fixture
def science_provider():
    return Science()

def test_science_meta(science_provider):
    assert science_provider.Meta.name == 'science'
