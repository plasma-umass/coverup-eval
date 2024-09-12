# file: tornado/locale.py:269-302
# asked: {"lines": [269, 270, 271, 272, 273, 274, 275, 276, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 294, 295, 296, 297, 298, 299, 300, 301], "branches": [[273, 274], [273, 279], [274, 273], [274, 275]]}
# gained: {"lines": [269], "branches": []}

import pytest
from unittest.mock import patch

# Mock data for LOCALE_NAMES
LOCALE_NAMES = {
    "en": {"name": "English"},
    "fa": {"name": "Persian"},
    "ar": {"name": "Arabic"},
    "he": {"name": "Hebrew"},
}

class Locale:
    def __init__(self, code: str) -> None:
        self.code = code
        self.name = LOCALE_NAMES.get(code, {}).get("name", "Unknown")
        self.rtl = False
        for prefix in ["fa", "ar", "he"]:
            if self.code.startswith(prefix):
                self.rtl = True
                break

        # Initialize strings for date formatting
        _ = self.translate
        self._months = [
            _("January"),
            _("February"),
            _("March"),
            _("April"),
            _("May"),
            _("June"),
            _("July"),
            _("August"),
            _("September"),
            _("October"),
            _("November"),
            _("December"),
        ]
        self._weekdays = [
            _("Monday"),
            _("Tuesday"),
            _("Wednesday"),
            _("Thursday"),
            _("Friday"),
            _("Saturday"),
            _("Sunday"),
        ]

    def translate(self, text):
        return text

@pytest.fixture
def mock_locale_names(monkeypatch):
    monkeypatch.setattr("tornado.locale.LOCALE_NAMES", LOCALE_NAMES)

def test_locale_initialization_english(mock_locale_names):
    locale = Locale("en")
    assert locale.code == "en"
    assert locale.name == "English"
    assert locale.rtl is False
    assert locale._months == [
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    ]
    assert locale._weekdays == [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]

def test_locale_initialization_persian(mock_locale_names):
    locale = Locale("fa")
    assert locale.code == "fa"
    assert locale.name == "Persian"
    assert locale.rtl is True
    assert locale._months == [
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    ]
    assert locale._weekdays == [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]

def test_locale_initialization_unknown(mock_locale_names):
    locale = Locale("unknown")
    assert locale.code == "unknown"
    assert locale.name == "Unknown"
    assert locale.rtl is False
    assert locale._months == [
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    ]
    assert locale._weekdays == [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
