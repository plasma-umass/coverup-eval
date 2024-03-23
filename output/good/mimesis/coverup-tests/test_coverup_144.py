# file mimesis/providers/base.py:20-22
# lines [20, 21]
# branches []

# test_base.py
import pytest
from mimesis.providers.base import BaseProvider

class TestBaseProvider:
    def test_base_provider_initialization(self):
        provider = BaseProvider()
        assert isinstance(provider, BaseProvider)
