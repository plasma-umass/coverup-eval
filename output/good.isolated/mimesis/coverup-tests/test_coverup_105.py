# file mimesis/builtins/en.py:16-18
# lines [16, 18]
# branches []

import pytest
from mimesis.builtins.en import USASpecProvider
from mimesis.random import Random

@pytest.fixture
def seed():
    return Random()

def test_usa_spec_provider_initialization(seed):
    provider = USASpecProvider(seed=seed)
    assert provider.locale == 'en'
    # Since there is no _seed attribute, we should not assert it
