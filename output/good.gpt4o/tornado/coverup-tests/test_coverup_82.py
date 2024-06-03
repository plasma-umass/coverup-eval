# file tornado/locale.py:525-535
# lines [525, 528, 529, 531, 532, 533, 535]
# branches ['531->532', '531->535']

import pytest
from tornado.locale import Locale

class MockGettextLocale(Locale):
    def __init__(self, code):
        super().__init__(code)

    def ngettext(self, singular, plural, count):
        return plural if count != 1 else singular

    def gettext(self, message):
        return message

    def translate(self, message, plural_message=None, count=None):
        if plural_message is not None:
            assert count is not None
            return self.ngettext(message, plural_message, count)
        else:
            return self.gettext(message)

@pytest.fixture
def gettext_locale():
    return MockGettextLocale("en")

def test_translate_plural_message(gettext_locale):
    result = gettext_locale.translate("apple", "apples", 2)
    assert result == "apples"

def test_translate_singular_message(gettext_locale):
    result = gettext_locale.translate("apple", "apples", 1)
    assert result == "apple"

def test_translate_no_plural_message(gettext_locale):
    result = gettext_locale.translate("apple")
    assert result == "apple"
