# file tornado/locale.py:319-326
# lines [319, 323, 324, 326]
# branches []

import pytest
from tornado.locale import Locale

class MockLocale(Locale):
    def __init__(self):
        pass

class TestLocale:
    def test_pgettext_not_implemented(self):
        locale = MockLocale()
        with pytest.raises(NotImplementedError):
            locale.pgettext("context", "message")
