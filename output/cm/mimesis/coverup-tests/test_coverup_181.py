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
        self.locale = locale

@pytest.fixture
def dummy_provider():
    return DummyProvider(locale=locales.EN)

def test_override_locale_context_manager(dummy_provider):
    with dummy_provider.override_locale(locales.RU) as provider:
        assert provider.locale == locales.RU
    assert dummy_provider.locale == locales.EN

def test_override_locale_context_manager_with_exception(mocker, dummy_provider):
    mocker.patch.object(dummy_provider, '_override_locale', side_effect=AttributeError)
    with pytest.raises(ValueError) as exc_info:
        with dummy_provider.override_locale(locales.RU):
            pass
    assert '«DummyProvider» has not locale dependent' in str(exc_info.value)
