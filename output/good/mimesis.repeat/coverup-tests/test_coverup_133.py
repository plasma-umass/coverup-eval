# file mimesis/providers/base.py:20-22
# lines [20, 21]
# branches []

import pytest
from mimesis.providers.base import BaseProvider

def test_base_provider_initialization():
    provider = BaseProvider()
    assert isinstance(provider, BaseProvider), "Object must be an instance of BaseProvider"
