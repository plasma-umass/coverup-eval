# file: tornado/locale.py:518-523
# asked: {"lines": [518, 519, 520, 523], "branches": []}
# gained: {"lines": [518, 519, 520, 523], "branches": []}

import pytest
import gettext
from tornado.locale import Locale, GettextLocale

class MockTranslations(gettext.NullTranslations):
    def gettext(self, message):
        return f"translated {message}"

    def ngettext(self, msgid1, msgid2, n):
        return f"translated {msgid1}" if n == 1 else f"translated {msgid2}"

@pytest.fixture
def mock_translations():
    return MockTranslations()

@pytest.fixture
def gettext_locale(mock_translations):
    return GettextLocale("en", mock_translations)

def test_gettext_locale_initialization(gettext_locale):
    assert gettext_locale.code == "en"
    assert gettext_locale.gettext("test") == "translated test"
    assert gettext_locale.ngettext("singular", "plural", 1) == "translated singular"
    assert gettext_locale.ngettext("singular", "plural", 2) == "translated plural"

def test_gettext_locale_rtl():
    mock_translations = MockTranslations()
    rtl_locale = GettextLocale("ar", mock_translations)
    assert rtl_locale.rtl is True

def test_gettext_locale_months_and_weekdays(gettext_locale):
    months = ["translated January", "translated February", "translated March", "translated April", "translated May", "translated June", "translated July", "translated August", "translated September", "translated October", "translated November", "translated December"]
    weekdays = ["translated Monday", "translated Tuesday", "translated Wednesday", "translated Thursday", "translated Friday", "translated Saturday", "translated Sunday"]
    assert gettext_locale._months == months
    assert gettext_locale._weekdays == weekdays
