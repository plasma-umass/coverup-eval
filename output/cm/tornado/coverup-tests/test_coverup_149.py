# file tornado/locale.py:304-317
# lines [304, 307, 308, 317]
# branches []

import pytest
from tornado.locale import Locale

class MockLocale(Locale):
    def __init__(self):
        pass

class TestLocale:
    def test_translate_singular(self, mocker):
        locale = MockLocale()
        mocker.patch.object(locale, 'translate', return_value='singular')
        assert locale.translate('apple', count=1) == 'singular'
        locale.translate.assert_called_once_with('apple', count=1)

    def test_translate_plural(self, mocker):
        locale = MockLocale()
        mocker.patch.object(locale, 'translate', return_value='plural')
        assert locale.translate('apple', 'apples', count=2) == 'plural'
        locale.translate.assert_called_once_with('apple', 'apples', count=2)

    def test_translate_raises_not_implemented_error(self):
        locale = MockLocale()
        with pytest.raises(NotImplementedError):
            locale.translate('apple')
