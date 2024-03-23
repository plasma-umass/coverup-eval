# file tornado/locale.py:467-476
# lines [467, 469, 470, 471, 472, 473, 474, 475, 476]
# branches ['469->470', '469->471', '473->474', '473->476']

import pytest
from tornado.locale import Locale

class TestLocale:
    @pytest.fixture
    def en_locale(self, mocker):
        mocker.patch.object(Locale, '__init__', return_value=None)
        locale = Locale()
        locale.code = 'en'
        return locale

    @pytest.fixture
    def non_en_locale(self, mocker):
        mocker.patch.object(Locale, '__init__', return_value=None)
        locale = Locale()
        locale.code = 'fr'
        return locale

    def test_friendly_number_en_locale(self, en_locale):
        assert en_locale.friendly_number(1234567) == '1,234,567'
        assert en_locale.friendly_number(123) == '123'
        assert en_locale.friendly_number(0) == '0'

    def test_friendly_number_non_en_locale(self, non_en_locale):
        assert non_en_locale.friendly_number(1234567) == '1234567'
        assert non_en_locale.friendly_number(123) == '123'
        assert non_en_locale.friendly_number(0) == '0'
