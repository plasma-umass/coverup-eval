# file tornado/locale.py:304-317
# lines [304, 307, 308, 317]
# branches []

import pytest
from tornado.locale import Locale

class TestLocale(Locale):
    def __init__(self):
        pass

def test_locale_translate_not_implemented():
    locale = TestLocale()
    with pytest.raises(NotImplementedError):
        locale.translate("test message")
    with pytest.raises(NotImplementedError):
        locale.translate("test message", "plural message", 2)
    with pytest.raises(NotImplementedError):
        locale.translate("test message", count=1)
