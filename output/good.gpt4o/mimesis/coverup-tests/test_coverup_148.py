# file mimesis/providers/base.py:68-70
# lines [68, 70]
# branches []

import pytest
from mimesis.providers.base import BaseProvider

def test_base_provider_str():
    # Create an instance of BaseProvider
    provider = BaseProvider()
    
    # Assert that the string representation is correct
    assert str(provider) == 'BaseProvider'
