# file: tornado/locale.py:518-523
# asked: {"lines": [518, 519, 520, 523], "branches": []}
# gained: {"lines": [518, 519, 520, 523], "branches": []}

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

def test_gettext_locale_init(mock_translations):
    code = 'en'
    locale = GettextLocale(code, mock_translations)
    
    assert locale.code == code
    assert locale.gettext('test') == 'test'
    assert locale.ngettext('singular', 'plural', 1) == 'singular'
    assert locale.ngettext('singular', 'plural', 2) == 'plural'
