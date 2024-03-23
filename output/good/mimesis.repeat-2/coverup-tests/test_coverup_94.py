# file mimesis/builtins/pt_br.py:11-13
# lines [11, 12]
# branches []

import pytest
from mimesis.builtins.pt_br import BrazilSpecProvider

def test_brazil_spec_provider_initialization():
    provider = BrazilSpecProvider()
    assert provider is not None
