# file mimesis/providers/base.py:167-175
# lines [167, 173, 174, 175]
# branches []

import pytest
from mimesis.providers.base import BaseDataProvider
from mimesis import locales
from unittest.mock import MagicMock

class TestBaseDataProvider:
    @pytest.fixture
    def provider(self):
        provider = BaseDataProvider()
        provider._pull = MagicMock()
        return provider

    def test_override_locale(self, provider):
        # Ensure the default locale is set before overriding
        assert provider.locale == locales.DEFAULT_LOCALE

        # Override the locale
        new_locale = locales.RU
        provider._override_locale(new_locale)

        # Check if the locale has been changed
        assert provider.locale == new_locale

        # Check if _pull was cleared and called
        provider._pull.cache_clear.assert_called_once()
        provider._pull.assert_called_once()

        # Clean up by resetting the locale
        provider._override_locale(locales.DEFAULT_LOCALE)
        assert provider.locale == locales.DEFAULT_LOCALE
