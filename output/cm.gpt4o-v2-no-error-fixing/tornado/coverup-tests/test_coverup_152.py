# file: tornado/locale.py:518-523
# asked: {"lines": [519, 520, 523], "branches": []}
# gained: {"lines": [519, 520, 523], "branches": []}

import pytest
import gettext
from tornado.locale import Locale, GettextLocale

class MockTranslations(gettext.NullTranslations):
    def ngettext(self, singular, plural, n):
        return singular if n == 1 else plural

    def gettext(self, message):
        return message

@pytest.fixture
def mock_translations():
    return MockTranslations()

def test_gettext_locale_initialization(mock_translations):
    code = 'en'
    locale = GettextLocale(code, mock_translations)
    
    assert locale.ngettext == mock_translations.ngettext
    assert locale.gettext == mock_translations.gettext
    assert locale.code == code
    assert locale.name == 'Unknown'
    assert locale.rtl == False
    assert hasattr(locale, '_months')
    assert hasattr(locale, '_weekdays')
