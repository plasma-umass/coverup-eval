# file: tornado/locale.py:479-512
# asked: {"lines": [483, 484, 492, 493, 494, 495, 496, 498, 500, 501, 510, 511, 512], "branches": [[492, 493], [492, 500], [494, 495], [494, 498], [510, 511], [510, 512]]}
# gained: {"lines": [483, 484, 492, 493, 494, 495, 496, 498, 500, 501, 510, 511, 512], "branches": [[492, 493], [492, 500], [494, 495], [494, 498], [510, 511]]}

import pytest
from tornado.locale import CSVLocale
from tornado.log import gen_log
from unittest.mock import patch

@pytest.fixture
def csv_locale():
    translations = {
        "singular": {"hello": "hola"},
        "plural": {"hello": "holas"},
        "unknown": {"hello": "hello"}
    }
    return CSVLocale("es", translations)

def test_csv_locale_init(csv_locale):
    assert csv_locale.translations == {
        "singular": {"hello": "hola"},
        "plural": {"hello": "holas"},
        "unknown": {"hello": "hello"}
    }

def test_translate_singular(csv_locale):
    assert csv_locale.translate("hello") == "hello"

def test_translate_plural(csv_locale):
    assert csv_locale.translate("hello", "hello", 2) == "holas"

def test_translate_singular_with_count(csv_locale):
    assert csv_locale.translate("hello", "hello", 1) == "hola"

def test_translate_unknown(csv_locale):
    assert csv_locale.translate("unknown_message") == "unknown_message"

def test_pgettext_warning(csv_locale):
    with patch.object(gen_log, 'warning') as mock_warning:
        csv_locale.pgettext("context", "hello")
        mock_warning.assert_called_once_with("pgettext is not supported by CSVLocale")

def test_pgettext_translation(csv_locale):
    assert csv_locale.pgettext("context", "hello") == "hello"
