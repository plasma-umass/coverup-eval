# file: tornado/locale.py:269-302
# asked: {"lines": [275, 276], "branches": [[274, 275]]}
# gained: {"lines": [275, 276], "branches": [[274, 275]]}

import pytest
from tornado.locale import Locale
from typing import Optional

class TestLocale(Locale):
    def translate(self, message: str, plural_message: Optional[str]=None, count: Optional[int]=None) -> str:
        return message

@pytest.fixture
def locale_ar():
    return TestLocale("ar")

@pytest.fixture
def locale_fa():
    return TestLocale("fa")

@pytest.fixture
def locale_he():
    return TestLocale("he")

@pytest.fixture
def locale_en():
    return TestLocale("en")

def test_locale_rtl_arabic(locale_ar):
    assert locale_ar.rtl == True

def test_locale_rtl_farsi(locale_fa):
    assert locale_fa.rtl == True

def test_locale_rtl_hebrew(locale_he):
    assert locale_he.rtl == True

def test_locale_not_rtl(locale_en):
    assert locale_en.rtl == False
