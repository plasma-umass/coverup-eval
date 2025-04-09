# file: tornado/locale.py:467-476
# asked: {"lines": [467, 469, 470, 471, 472, 473, 474, 475, 476], "branches": [[469, 470], [469, 471], [473, 474], [473, 476]]}
# gained: {"lines": [467, 469, 470, 471, 472, 473, 474, 475, 476], "branches": [[469, 470], [469, 471], [473, 474], [473, 476]]}

import pytest
from tornado.locale import Locale

class TestLocale:
    class TestLocaleImplementation(Locale):
        def translate(self, message, plural_message=None, count=None):
            return message

    @pytest.fixture
    def locale_en(self):
        locale = self.TestLocaleImplementation("en")
        return locale

    @pytest.fixture
    def locale_en_us(self):
        locale = self.TestLocaleImplementation("en_US")
        return locale

    @pytest.fixture
    def locale_other(self):
        locale = self.TestLocaleImplementation("fr")
        return locale

    def test_friendly_number_en(self, locale_en):
        result = locale_en.friendly_number(1234567)
        assert result == "1,234,567"

    def test_friendly_number_en_us(self, locale_en_us):
        result = locale_en_us.friendly_number(1234567)
        assert result == "1,234,567"

    def test_friendly_number_other(self, locale_other):
        result = locale_other.friendly_number(1234567)
        assert result == "1234567"
