# file mimesis/providers/base.py:68-70
# lines [68, 70]
# branches []

import pytest
from mimesis.providers.base import BaseProvider

class DummyProvider(BaseProvider):
    pass

def test_base_provider_str_representation():
    provider = DummyProvider()
    assert str(provider) == 'DummyProvider'
