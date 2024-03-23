# file mimesis/builtins/en.py:20-23
# lines [20, 21, 23]
# branches []

import pytest
from mimesis.builtins.en import USASpecProvider

def test_usa_spec_provider_meta():
    provider = USASpecProvider()
    assert provider.Meta.name == 'usa_provider'
