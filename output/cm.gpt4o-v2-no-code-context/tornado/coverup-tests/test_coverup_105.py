# file: tornado/locale.py:319-326
# asked: {"lines": [319, 323, 324, 326], "branches": []}
# gained: {"lines": [319, 323, 324, 326], "branches": []}

import pytest
from tornado.locale import Locale

class TestLocale(Locale):
    def translate(self, message, plural_message=None, count=None):
        return message

def test_locale_pgettext_not_implemented():
    locale = TestLocale("en")
    with pytest.raises(NotImplementedError):
        locale.pgettext("context", "message")

    with pytest.raises(NotImplementedError):
        locale.pgettext("context", "message", "plural_message")

    with pytest.raises(NotImplementedError):
        locale.pgettext("context", "message", "plural_message", 1)
