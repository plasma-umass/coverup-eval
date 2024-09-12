# file: tornado/locale.py:467-476
# asked: {"lines": [467, 469, 470, 471, 472, 473, 474, 475, 476], "branches": [[469, 470], [469, 471], [473, 474], [473, 476]]}
# gained: {"lines": [467, 469, 470, 471, 472, 473, 474, 475, 476], "branches": [[469, 470], [469, 471], [473, 474], [473, 476]]}

import pytest
from tornado.locale import Locale
from typing import Optional

class TestLocale(Locale):
    def translate(self, message: str, plural_message: Optional[str] = None, count: Optional[int] = None) -> str:
        return message

@pytest.fixture
def locale_en():
    return TestLocale("en")

@pytest.fixture
def locale_fr():
    return TestLocale("fr")

def test_friendly_number_en(locale_en):
    result = locale_en.friendly_number(1234567)
    assert result == "1,234,567"

def test_friendly_number_fr(locale_fr):
    result = locale_fr.friendly_number(1234567)
    assert result == "1234567"

def test_friendly_number_small(locale_en):
    result = locale_en.friendly_number(123)
    assert result == "123"

def test_friendly_number_zero(locale_en):
    result = locale_en.friendly_number(0)
    assert result == "0"
