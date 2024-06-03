# file mimesis/providers/base.py:157-165
# lines [165]
# branches []

import pytest
from mimesis.providers.base import BaseDataProvider

def test_get_current_locale(mocker):
    # Mock the locale attribute of BaseDataProvider
    mock_locale = 'es'
    provider = BaseDataProvider()
    mocker.patch.object(provider, 'locale', mock_locale)
    
    # Call the method and assert the result
    result = provider.get_current_locale()
    assert result == mock_locale
