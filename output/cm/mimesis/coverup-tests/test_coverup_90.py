# file mimesis/builtins/en.py:13-15
# lines [13, 14]
# branches []

import pytest
from mimesis.builtins.en import USASpecProvider

def test_usa_spec_provider_initialization():
    provider = USASpecProvider()
    assert provider is not None
