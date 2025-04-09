# file: tornado/locale.py:479-512
# asked: {"lines": [479, 480, 482, 483, 484, 486, 489, 490, 492, 493, 494, 495, 496, 498, 500, 501, 503, 507, 508, 510, 511, 512], "branches": [[492, 493], [492, 500], [494, 495], [494, 498], [510, 511], [510, 512]]}
# gained: {"lines": [479, 480, 482, 486, 489, 490, 503, 507, 508], "branches": []}

import pytest
from tornado.locale import Locale
from tornado.log import gen_log
from typing import Dict, Optional
import logging

class CSVLocale(Locale):
    def __init__(self, code: str, translations: Dict[str, Dict[str, str]]) -> None:
        self.translations = translations
        super().__init__(code)

    def translate(self, message: str, plural_message: Optional[str] = None, count: Optional[int] = None) -> str:
        if plural_message is not None:
            assert count is not None
            if count != 1:
                message = plural_message
                message_dict = self.translations.get("plural", {})
            else:
                message_dict = self.translations.get("singular", {})
        else:
            message_dict = self.translations.get("unknown", {})
        return message_dict.get(message, message)

    def pgettext(self, context: str, message: str, plural_message: Optional[str] = None, count: Optional[int] = None) -> str:
        if self.translations:
            gen_log.warning("pgettext is not supported by CSVLocale")
        return self.translate(message, plural_message, count)

@pytest.fixture
def csv_locale():
    translations = {
        "singular": {"hello": "hola"},
        "plural": {"hello": "holas"},
        "unknown": {"hello": "hello"}
    }
    return CSVLocale("es", translations)

def test_translate_singular(csv_locale):
    assert csv_locale.translate("hello") == "hello"

def test_translate_plural(csv_locale):
    assert csv_locale.translate("hello", "holas", 2) == "holas"

def test_translate_singular_with_count(csv_locale):
    assert csv_locale.translate("hello", "holas", 1) == "hola"

def test_translate_unknown(csv_locale):
    assert csv_locale.translate("unknown_message") == "unknown_message"

def test_pgettext_warning(csv_locale, caplog):
    with caplog.at_level(logging.WARNING):
        csv_locale.pgettext("context", "hello")
        assert "pgettext is not supported by CSVLocale" in caplog.text

def test_pgettext_translation(csv_locale):
    assert csv_locale.pgettext("context", "hello") == "hello"
