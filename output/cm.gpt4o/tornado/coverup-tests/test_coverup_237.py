# file tornado/locale.py:319-326
# lines [326]
# branches []

import pytest
from tornado.locale import Locale

class TestLocale(Locale):
    def __init__(self):
        pass

def test_locale_pgettext_not_implemented():
    locale = TestLocale()
    with pytest.raises(NotImplementedError):
        locale.pgettext("context", "message")
