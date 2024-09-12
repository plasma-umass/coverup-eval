# file: tornado/locale.py:479-512
# asked: {"lines": [], "branches": [[510, 512]]}
# gained: {"lines": [], "branches": [[510, 512]]}

import pytest
from tornado.locale import CSVLocale
from tornado.log import gen_log
from unittest.mock import patch

@pytest.fixture
def csv_locale():
    translations = {
        "singular": {"hello": "hola"},
        "plural": {"apples": "manzanas"},
        "unknown": {"goodbye": "adios"}
    }
    return CSVLocale("es", translations)

def test_pgettext_with_translations(csv_locale):
    with patch.object(gen_log, 'warning') as mock_warning:
        result = csv_locale.pgettext("context", "goodbye")
        mock_warning.assert_called_once_with("pgettext is not supported by CSVLocale")
        assert result == "adios"

def test_pgettext_without_translations():
    csv_locale = CSVLocale("es", {})
    with patch.object(gen_log, 'warning') as mock_warning:
        result = csv_locale.pgettext("context", "goodbye")
        mock_warning.assert_not_called()
        assert result == "goodbye"
