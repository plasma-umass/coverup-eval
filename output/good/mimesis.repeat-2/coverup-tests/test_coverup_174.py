# file mimesis/providers/base.py:177-197
# lines [191, 192, 194]
# branches []

import pytest
from mimesis.providers.base import BaseDataProvider
from mimesis import locales

class DummyProvider(BaseDataProvider):
    def __init__(self, locale):
        self.locale = locale

    def _override_locale(self, locale):
        if not hasattr(self, 'locale'):
            raise AttributeError("DummyProvider has no attribute 'locale'")
        self.locale = locale

def test_override_locale():
    provider = DummyProvider(locale=locales.EN)

    with provider.override_locale(locales.RU) as overridden_provider:
        assert overridden_provider.locale == locales.RU

    assert provider.locale == locales.EN

    # Test the AttributeError branch
    del provider.locale
    with pytest.raises(ValueError) as exc_info:
        with provider.override_locale(locales.RU):
            pass
    assert '«DummyProvider» has not locale dependent' in str(exc_info.value)
