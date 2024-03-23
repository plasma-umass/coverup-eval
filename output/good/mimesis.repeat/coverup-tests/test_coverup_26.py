# file mimesis/providers/base.py:177-197
# lines [177, 178, 188, 189, 190, 191, 192, 194, 195, 196, 197]
# branches []

import pytest
from mimesis.providers.base import BaseDataProvider
from mimesis import locales

class DummyProvider(BaseDataProvider):
    def __init__(self, locale=locales.EN):
        super().__init__(locale)
        self.locale = locale

    def _override_locale(self, locale):
        self.locale = locale

def test_override_locale():
    provider = DummyProvider()

    with provider.override_locale(locales.RU) as overridden:
        assert overridden.locale == locales.RU

    assert provider.locale == locales.EN

def test_override_locale_with_no_locale_attribute():
    provider = DummyProvider()

    # Remove the locale attribute to simulate the AttributeError
    del provider.locale

    with pytest.raises(ValueError) as exc_info:
        with provider.override_locale(locales.RU):
            pass

    assert '«DummyProvider» has not locale dependent' in str(exc_info.value)
