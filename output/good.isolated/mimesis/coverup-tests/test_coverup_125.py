# file mimesis/providers/base.py:73-75
# lines [73, 74]
# branches []

import pytest
from mimesis.providers.base import BaseDataProvider

def test_base_data_provider_initialization():
    provider = BaseDataProvider()
    assert isinstance(provider, BaseDataProvider), "Object must be an instance of BaseDataProvider"
