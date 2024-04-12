# file mimesis/providers/base.py:157-165
# lines [157, 165]
# branches []

import pytest
from mimesis.providers.base import BaseDataProvider

class DummyProvider(BaseDataProvider):
    pass

def test_get_current_locale_default():
    provider = DummyProvider()
    assert provider.get_current_locale() == 'en', "Should return 'en' as default locale"

def test_get_current_locale_custom_locale():
    provider = DummyProvider(locale='es')
    assert provider.get_current_locale() == 'es', "Should return 'es' as custom locale"
