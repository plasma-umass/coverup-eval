# file mimesis/providers/base.py:157-165
# lines [157, 165]
# branches []

import pytest
from mimesis.providers.base import BaseDataProvider

class DummyProvider(BaseDataProvider):
    def __init__(self, locale='en'):
        self.locale = locale

@pytest.fixture
def dummy_provider():
    return DummyProvider()

def test_get_current_locale_default(dummy_provider):
    assert dummy_provider.get_current_locale() == 'en', "Should return 'en' as default locale"

def test_get_current_locale_custom_locale():
    custom_locale = 'es'
    provider_with_locale = DummyProvider(locale=custom_locale)
    assert provider_with_locale.get_current_locale() == custom_locale, f"Should return '{custom_locale}' as custom locale"
