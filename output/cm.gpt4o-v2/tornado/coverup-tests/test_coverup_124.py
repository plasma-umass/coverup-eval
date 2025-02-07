# file: tornado/locale.py:319-326
# asked: {"lines": [319, 323, 324, 326], "branches": []}
# gained: {"lines": [319, 323, 324, 326], "branches": []}

import pytest
from tornado.locale import Locale
from typing import Optional

class TestLocale(Locale):
    def translate(self, message: str, plural_message: Optional[str]=None, count: Optional[int]=None) -> str:
        return message if count == 1 else (plural_message or message)

def test_pgettext_not_implemented():
    locale = TestLocale("en_US")
    with pytest.raises(NotImplementedError):
        locale.pgettext("context", "message")

def test_pgettext_with_plural_not_implemented():
    locale = TestLocale("en_US")
    with pytest.raises(NotImplementedError):
        locale.pgettext("context", "message", "plural_message", 2)
