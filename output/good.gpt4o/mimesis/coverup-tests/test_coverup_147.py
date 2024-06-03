# file mimesis/providers/base.py:73-75
# lines [73, 74]
# branches []

import pytest
from mimesis.providers.base import BaseProvider

class TestBaseDataProvider:
    def test_base_data_provider_initialization(self):
        class BaseDataProvider(BaseProvider):
            """This is a base class for all data providers."""
        
        provider = BaseDataProvider()
        assert isinstance(provider, BaseDataProvider)
        assert isinstance(provider, BaseProvider)
