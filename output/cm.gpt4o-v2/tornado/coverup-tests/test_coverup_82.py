# file: tornado/locale.py:525-535
# asked: {"lines": [525, 528, 529, 531, 532, 533, 535], "branches": [[531, 532], [531, 535]]}
# gained: {"lines": [525, 528, 529, 531, 532, 533, 535], "branches": [[531, 532], [531, 535]]}

import pytest
from unittest.mock import MagicMock, call
from tornado.locale import GettextLocale
import gettext

@pytest.fixture
def gettext_locale():
    translations = MagicMock(spec=gettext.NullTranslations)
    translations.ngettext = MagicMock(return_value="plural_translation")
    translations.gettext = MagicMock(return_value="singular_translation")
    locale = GettextLocale("en_US", translations)
    return locale

def test_translate_singular(gettext_locale):
    gettext_locale.gettext.reset_mock()
    result = gettext_locale.translate("message")
    gettext_locale.gettext.assert_called_with("message")
    assert result == "singular_translation"

def test_translate_plural(gettext_locale):
    gettext_locale.ngettext.reset_mock()
    result = gettext_locale.translate("message", "plural_message", 2)
    gettext_locale.ngettext.assert_called_with("message", "plural_message", 2)
    assert result == "plural_translation"

def test_translate_plural_without_count(gettext_locale):
    with pytest.raises(AssertionError):
        gettext_locale.translate("message", "plural_message")
