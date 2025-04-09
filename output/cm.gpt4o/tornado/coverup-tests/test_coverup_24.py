# file tornado/locale.py:269-302
# lines [269, 270, 271, 272, 273, 274, 275, 276, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 294, 295, 296, 297, 298, 299, 300, 301]
# branches ['273->274', '273->279', '274->273', '274->275']

import pytest
from unittest import mock

# Mock LOCALE_NAMES to control the environment for the test
LOCALE_NAMES = {
    "en": {"name": "English"},
    "fa": {"name": "Farsi"},
    "ar": {"name": "Arabic"},
    "he": {"name": "Hebrew"},
}

@pytest.fixture
def mock_locale_names(mocker):
    mocker.patch('tornado.locale.LOCALE_NAMES', LOCALE_NAMES)

@pytest.fixture
def mock_translate(mocker):
    mocker.patch('tornado.locale.Locale.translate', side_effect=lambda x: x)

def test_locale_initialization(mock_locale_names, mock_translate):
    from tornado.locale import Locale

    # Test for a locale that is not in LOCALE_NAMES
    locale_unknown = Locale("unknown")
    assert locale_unknown.code == "unknown"
    assert locale_unknown.name == "Unknown"
    assert locale_unknown.rtl is False

    # Test for a locale that is in LOCALE_NAMES and is not RTL
    locale_en = Locale("en")
    assert locale_en.code == "en"
    assert locale_en.name == "English"
    assert locale_en.rtl is False

    # Test for a locale that is in LOCALE_NAMES and is RTL
    locale_fa = Locale("fa")
    assert locale_fa.code == "fa"
    assert locale_fa.name == "Farsi"
    assert locale_fa.rtl is True

    # Test for another RTL locale
    locale_ar = Locale("ar")
    assert locale_ar.code == "ar"
    assert locale_ar.name == "Arabic"
    assert locale_ar.rtl is True

    # Test for another RTL locale
    locale_he = Locale("he")
    assert locale_he.code == "he"
    assert locale_he.name == "Hebrew"
    assert locale_he.rtl is True

    # Verify the months and weekdays are initialized correctly
    assert locale_en._months == [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    assert locale_en._weekdays == [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
