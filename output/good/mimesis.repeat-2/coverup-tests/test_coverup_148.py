# file mimesis/providers/base.py:157-165
# lines [157, 165]
# branches []

import pytest
from mimesis.providers.base import BaseDataProvider

class DummyProvider(BaseDataProvider):
    def __init__(self, locale=None):
        self._locale = locale or 'en'
    
    @property
    def locale(self):
        return self._locale

@pytest.fixture
def dummy_provider():
    provider = DummyProvider()
    yield provider

def test_get_current_locale_default(dummy_provider):
    assert dummy_provider.get_current_locale() == 'en', "Should return 'en' as default locale"

def test_get_current_locale_set_locale():
    provider = DummyProvider(locale='es')
    assert provider.get_current_locale() == 'es', "Should return 'es' when locale is set"
