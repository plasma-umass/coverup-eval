# file tornado/locale.py:251-267
# lines [261, 263]
# branches ['257->267', '260->261', '262->263']

import pytest
from tornado.locale import Locale, _supported_locales, _translations, _use_gettext, CSVLocale, GettextLocale
import gettext

# Assuming the existence of CSVLocale and GettextLocale classes and _supported_locales, _translations, _use_gettext variables

class TestLocale:
    def test_get_unsupported_locale(self, mocker):
        # Setup: Add a locale code that is not in the _supported_locales and not in the _translations
        unsupported_locale_code = 'xx_XX'
        mocker.patch('tornado.locale._supported_locales', _supported_locales | {unsupported_locale_code})
        _translations.pop(unsupported_locale_code, None)
        mocker.patch.object(Locale, '_cache', new={})

        # Test: Try to get the unsupported locale, which should trigger the creation of a CSVLocale
        locale = Locale.get(unsupported_locale_code)
        assert isinstance(locale, CSVLocale)
        assert locale.code == unsupported_locale_code

    def test_get_supported_locale_with_gettext(self, mocker):
        # Setup: Add a locale code that is in the _supported_locales and in the _translations
        supported_locale_code = 'en_US'
        mocker.patch('tornado.locale._supported_locales', _supported_locales | {supported_locale_code})
        mock_translations = gettext.NullTranslations()
        _translations[supported_locale_code] = mock_translations
        mocker.patch.object(Locale, '_cache', new={})
        mocker.patch('tornado.locale._use_gettext', new=True)

        # Test: Try to get the supported locale with _use_gettext set to True, which should trigger the creation of a GettextLocale
        locale = Locale.get(supported_locale_code)
        assert isinstance(locale, GettextLocale)
        assert locale.code == supported_locale_code

        # Cleanup: Remove the supported locale code from _translations
        _translations.pop(supported_locale_code, None)
