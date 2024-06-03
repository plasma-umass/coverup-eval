# file mimesis/builtins/pl.py:13-15
# lines [13, 14]
# branches []

import pytest
from mimesis.builtins.pl import PolandSpecProvider

def test_poland_spec_provider_initialization():
    provider = PolandSpecProvider()
    assert isinstance(provider, PolandSpecProvider)
    assert provider.__class__.__name__ == "PolandSpecProvider"
