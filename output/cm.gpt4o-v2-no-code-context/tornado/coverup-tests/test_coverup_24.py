# file: tornado/locale.py:269-302
# asked: {"lines": [269, 270, 271, 272, 273, 274, 275, 276, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 294, 295, 296, 297, 298, 299, 300, 301], "branches": [[273, 274], [273, 279], [274, 273], [274, 275]]}
# gained: {"lines": [269, 270, 271, 272, 273, 274, 275, 276, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 294, 295, 296, 297, 298, 299, 300, 301], "branches": [[273, 274], [273, 279], [274, 273], [274, 275]]}

import pytest
from unittest.mock import patch

# Assuming the Locale class is imported from tornado.locale
from tornado.locale import Locale

@pytest.fixture
def mock_locale_names(monkeypatch):
    mock_data = {
        "en": {"name": "English"},
        "fa": {"name": "Farsi"},
        "ar": {"name": "Arabic"},
        "he": {"name": "Hebrew"},
    }
    monkeypatch.setattr("tornado.locale.LOCALE_NAMES", mock_data)

@pytest.fixture
def mock_translate(monkeypatch):
    def mock_translation(self, message, plural_message=None, count=None):
        return message
    monkeypatch.setattr(Locale, "translate", mock_translation)

def test_locale_initialization_english(mock_locale_names, mock_translate):
    locale = Locale("en")
    assert locale.code == "en"
    assert locale.name == "English"
    assert not locale.rtl
    assert locale._months == [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    assert locale._weekdays == [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]

def test_locale_initialization_farsi(mock_locale_names, mock_translate):
    locale = Locale("fa")
    assert locale.code == "fa"
    assert locale.name == "Farsi"
    assert locale.rtl
    assert locale._months == [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    assert locale._weekdays == [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]

def test_locale_initialization_arabic(mock_locale_names, mock_translate):
    locale = Locale("ar")
    assert locale.code == "ar"
    assert locale.name == "Arabic"
    assert locale.rtl
    assert locale._months == [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    assert locale._weekdays == [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]

def test_locale_initialization_hebrew(mock_locale_names, mock_translate):
    locale = Locale("he")
    assert locale.code == "he"
    assert locale.name == "Hebrew"
    assert locale.rtl
    assert locale._months == [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    assert locale._weekdays == [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]

def test_locale_initialization_unknown(mock_locale_names, mock_translate):
    locale = Locale("unknown")
    assert locale.code == "unknown"
    assert locale.name == "Unknown"
    assert not locale.rtl
    assert locale._months == [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    assert locale._weekdays == [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
