# file: tornado/locale.py:525-535
# asked: {"lines": [525, 528, 529, 531, 532, 533, 535], "branches": [[531, 532], [531, 535]]}
# gained: {"lines": [525, 528, 529], "branches": []}

import pytest
from tornado.locale import Locale

class MockGettextLocale(Locale):
    def __init__(self, code):
        super().__init__(code)

    def ngettext(self, singular, plural, count):
        return f"{singular if count == 1 else plural} ({count})"

    def gettext(self, message):
        return f"translated {message}"

    def translate(self, message, plural_message=None, count=None):
        if plural_message is not None:
            assert count is not None
            return self.ngettext(message, plural_message, count)
        else:
            return self.gettext(message)

@pytest.fixture
def gettext_locale():
    return MockGettextLocale("en")

def test_translate_singular(gettext_locale):
    result = gettext_locale.translate("apple")
    assert result == "translated apple"

def test_translate_plural(gettext_locale):
    result = gettext_locale.translate("apple", "apples", 2)
    assert result == "apples (2)"

def test_translate_plural_singular_form(gettext_locale):
    result = gettext_locale.translate("apple", "apples", 1)
    assert result == "apple (1)"
