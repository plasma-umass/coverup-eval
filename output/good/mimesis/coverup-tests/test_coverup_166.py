# file mimesis/providers/base.py:89-103
# lines [97]
# branches ['96->97']

import pytest
from mimesis.exceptions import UnsupportedLocale
from mimesis.locales import DEFAULT_LOCALE, SUPPORTED_LOCALES
from mimesis.providers.base import BaseDataProvider

class TestBaseDataProvider:
    def test_setup_locale_with_empty_locale(self, mocker):
        # Mock the BaseDataProvider to isolate the test environment
        base_data_provider = BaseDataProvider()
        mocker.spy(base_data_provider, '_setup_locale')

        # Call the method with an empty string to trigger the missing branch
        base_data_provider._setup_locale("")

        # Check if the default locale was set
        assert base_data_provider.locale == DEFAULT_LOCALE
        # Ensure the method was called
        base_data_provider._setup_locale.assert_called_once_with("")

    def test_setup_locale_with_unsupported_locale(self):
        base_data_provider = BaseDataProvider()

        # Test with an unsupported locale
        with pytest.raises(UnsupportedLocale):
            base_data_provider._setup_locale("unsupported_locale")

    def test_setup_locale_with_supported_locale(self):
        base_data_provider = BaseDataProvider()

        # Test with a supported locale
        supported_locale = list(SUPPORTED_LOCALES)[0]
        base_data_provider._setup_locale(supported_locale)

        # Check if the supported locale was set correctly
        assert base_data_provider.locale == supported_locale.lower()
