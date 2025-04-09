# file tornado/locale.py:518-523
# lines [518, 519, 520, 523]
# branches []

import pytest
from unittest import mock
import gettext
from tornado.locale import Locale

class GettextLocale(Locale):
    def __init__(self, code: str, translations: gettext.NullTranslations) -> None:
        self.ngettext = translations.ngettext
        self.gettext = translations.gettext
        super().__init__(code)

    def translate(self, message: str, plural_message: str = None, count: int = None) -> str:
        if plural_message and count is not None:
            return self.ngettext(message, plural_message, count)
        return self.gettext(message)

def test_gettextlocale_initialization(mocker):
    mock_translations = mocker.Mock(spec=gettext.NullTranslations)
    mock_translations.ngettext = mocker.Mock(return_value="plural_translation")
    mock_translations.gettext = mocker.Mock(return_value="translation")

    locale_code = 'en_US'
    locale_instance = GettextLocale(locale_code, mock_translations)

    assert locale_instance.ngettext == mock_translations.ngettext
    assert locale_instance.gettext == mock_translations.gettext
    assert locale_instance.code == locale_code

    # Test the translate method
    assert locale_instance.translate("message") == "translation"
    assert locale_instance.translate("message", "plural_message", 2) == "plural_translation"
