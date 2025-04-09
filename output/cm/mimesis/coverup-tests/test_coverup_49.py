# file mimesis/builtins/pt_br.py:18-21
# lines [18, 19, 21]
# branches []

import pytest
from mimesis.builtins.pt_br import BrazilSpecProvider

def test_brazil_spec_provider_meta():
    provider = BrazilSpecProvider()
    assert provider.Meta.name == 'brazil_provider'
