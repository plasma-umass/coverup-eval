# file mimesis/providers/text.py:16-24
# lines [16, 22, 23, 24]
# branches []

import pytest
from mimesis.providers.text import Text
from mimesis.exceptions import UnsupportedLocale

# Assuming the existence of a 'text.json' file with appropriate data for 'en' locale.

def test_text_init(mocker):
    # Mock the _pull method to ensure it's called with 'text.json'
    mocker.patch('mimesis.providers.text.BaseDataProvider._pull')

    # Create an instance of Text with 'en' locale
    text_provider = Text(locale='en')

    # Assert that _pull was called once with 'text.json'
    text_provider._pull.assert_called_once_with('text.json')

    # Clean up by deleting the instance
    del text_provider

# Test for unsupported locale which should raise UnsupportedLocale exception
def test_text_init_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        Text(locale='unsupported_locale')
