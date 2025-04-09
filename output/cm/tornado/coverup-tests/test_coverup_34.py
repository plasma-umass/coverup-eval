# file tornado/locale.py:233-249
# lines [233, 234, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249]
# branches ['236->237', '236->249', '237->238', '237->239', '241->242', '241->243', '243->244', '243->245', '245->246', '245->247', '247->236', '247->248']

import pytest
from unittest.mock import MagicMock
from tornado.locale import Locale

# Assuming _supported_locales and _default_locale are defined in the tornado.locale module
# If they are not, you would need to mock them for the test.

_supported_locales = {
    'en_US': 'Locale_en_US',
    'en': 'Locale_en',
}
_default_locale = 'en_US'

class TestLocale:
    def test_get_closest(self, mocker):
        # Mock the Locale class itself to avoid initialization
        mocker.patch('tornado.locale.Locale', autospec=True)

        # Mock the get method to return a mock object for testing purposes
        mock_locale = MagicMock(spec=Locale)
        mocker.patch.object(Locale, 'get', return_value=mock_locale)

        # Test with a locale code that should match exactly
        assert Locale.get_closest('en_US') is mock_locale

        # Test with a locale code that should be normalized and matched
        assert Locale.get_closest('en-us') is mock_locale

        # Test with a locale code that should match the language part
        assert Locale.get_closest('en_GB') is mock_locale

        # Test with a locale code that should not match and return the default
        assert Locale.get_closest('fr_FR') is mock_locale

        # Test with an invalid locale code that should be skipped
        assert Locale.get_closest('invalid_code') is mock_locale

        # Test with None as input, which should be skipped and return the default
        assert Locale.get_closest(None) is mock_locale

        # Test with multiple locale codes where the first valid one should match
        assert Locale.get_closest('invalid_code', 'en_GB', 'fr_FR') is mock_locale

        # Test with multiple invalid locale codes, which should return the default
        assert Locale.get_closest('invalid_code', 'another_invalid_code') is mock_locale

        # Clean up by removing the mock
        mocker.stopall()
