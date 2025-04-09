# file tornado/locale.py:467-476
# lines [469, 470, 471, 472, 473, 474, 475, 476]
# branches ['469->470', '469->471', '473->474', '473->476']

import pytest
from tornado.locale import Locale

class TestLocale:
    class TestLocaleImplementation(Locale):
        def translate(self, message, plural_message=None, count=None):
            return message

    def test_friendly_number_non_english(self, mocker):
        # Create an instance of the test implementation with a non-English locale
        locale = self.TestLocaleImplementation('es')
        
        # Test the friendly_number method
        result = locale.friendly_number(1234567)
        
        # Assert that the result is the plain number as a string
        assert result == '1234567'

    def test_friendly_number_english(self, mocker):
        # Create an instance of the test implementation with an English locale
        locale = self.TestLocaleImplementation('en')

        # Test the friendly_number method
        result = locale.friendly_number(1234567)
        
        # Assert that the result is the comma-separated number
        assert result == '1,234,567'
