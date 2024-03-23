# file mimesis/providers/science.py:52-60
# lines [52, 60]
# branches []

import pytest
from mimesis.providers.science import Science
from mimesis import Generic

@pytest.fixture
def science_provider():
    return Science()

def test_atomic_number(science_provider):
    atomic_number = science_provider.atomic_number()
    assert isinstance(atomic_number, int)
    assert 1 <= atomic_number <= 119

    # Clean up is not necessary here as the test does not modify any external state
