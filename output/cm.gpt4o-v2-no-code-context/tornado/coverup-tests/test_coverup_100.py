# file: tornado/locale.py:304-317
# asked: {"lines": [304, 307, 308, 317], "branches": []}
# gained: {"lines": [304, 307, 308, 317], "branches": []}

import pytest
from tornado.locale import Locale

class TestLocale:
    def test_translate_not_implemented(self, monkeypatch):
        class TestLocale(Locale):
            def __init__(self):
                pass

        locale = TestLocale()
        with pytest.raises(NotImplementedError):
            locale.translate("message")

    def test_translate_plural_not_implemented(self, monkeypatch):
        class TestLocale(Locale):
            def __init__(self):
                pass

        locale = TestLocale()
        with pytest.raises(NotImplementedError):
            locale.translate("message", "plural_message", 2)
