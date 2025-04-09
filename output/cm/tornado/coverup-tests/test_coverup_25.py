# file tornado/locale.py:269-302
# lines [269, 270, 271, 272, 273, 274, 275, 276, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 294, 295, 296, 297, 298, 299, 300, 301]
# branches ['273->274', '273->279', '274->273', '274->275']

import pytest
from tornado.locale import Locale

# Assuming LOCALE_NAMES is a global variable in the tornado.locale module
# that contains a mapping of locale codes to their names and other properties.
# If it's not, you would need to mock it accordingly.

LOCALE_NAMES = {
    'en': {'name': 'English'},
    'fa': {'name': 'Farsi'},
    'ar': {'name': 'Arabic'},
    'he': {'name': 'Hebrew'},
}

@pytest.fixture
def mock_locale_names(mocker):
    mocker.patch('tornado.locale.LOCALE_NAMES', LOCALE_NAMES)

@pytest.fixture
def mock_translate(mocker):
    mocker.patch.object(Locale, 'translate', return_value='')

def test_locale_rtl_detection(mock_locale_names, mock_translate):
    # Test for a locale that should be right-to-left
    locale_fa = Locale('fa')
    assert locale_fa.rtl is True
    assert locale_fa.name == 'Farsi'

    # Test for a locale that should not be right-to-left
    locale_en = Locale('en')
    assert locale_en.rtl is False
    assert locale_en.name == 'English'

    # Test for a locale that is not in LOCALE_NAMES
    locale_unknown = Locale('xx')
    assert locale_unknown.rtl is False
    assert locale_unknown.name == 'Unknown'

    # Test for a locale that starts with a prefix that is not right-to-left
    locale_en_gb = Locale('en-GB')
    assert locale_en_gb.rtl is False
    assert locale_en_gb.name == 'Unknown'

    # Test for a locale that starts with a right-to-left prefix but is not in LOCALE_NAMES
    locale_ar_unknown = Locale('ar-XX')
    assert locale_ar_unknown.rtl is True
    assert locale_ar_unknown.name == 'Unknown'
