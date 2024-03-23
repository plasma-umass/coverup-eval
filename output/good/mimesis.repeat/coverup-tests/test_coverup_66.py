# file mimesis/builtins/pl.py:20-23
# lines [20, 21, 23]
# branches []

import pytest
from mimesis.builtins.pl import PolandSpecProvider

def test_poland_spec_provider_meta():
    provider = PolandSpecProvider()
    assert provider.Meta.name == 'poland_provider'
