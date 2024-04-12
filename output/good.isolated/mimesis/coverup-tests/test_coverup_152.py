# file mimesis/providers/base.py:177-197
# lines [188, 189, 190, 191, 192, 194, 195, 196, 197]
# branches []

import pytest
from mimesis.providers.base import BaseDataProvider
from mimesis import locales

class DummyProvider(BaseDataProvider):
    def __init__(self, locale):
        self.locale = locale

    def _override_locale(self, locale):
        self.locale = locale

def test_override_locale_exception(mocker):
    provider = DummyProvider(locale=locales.EN)

    # Mock the _override_locale method to raise AttributeError
    mocker.patch.object(provider, '_override_locale', side_effect=AttributeError)

    with pytest.raises(ValueError) as exc_info:
        with provider.override_locale(locale=locales.RU):
            pass

    assert '«DummyProvider» has not locale dependent' in str(exc_info.value)
