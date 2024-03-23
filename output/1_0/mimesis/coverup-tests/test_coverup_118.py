# file mimesis/providers/code.py:36-44
# lines [44]
# branches []

import pytest
from mimesis.providers.code import Code

# Assuming LOCALE_CODES is a list of locale code strings.
# Since it's not provided in the question, we'll mock it for the test.
LOCALE_CODES = ['en-US', 'fr-FR', 'es-ES', 'de-DE', 'ru-RU']

# Mocking the random.choice method in the Code class to return a specific value
@pytest.fixture
def code_provider(mocker):
    mocker.patch('mimesis.random.Random.choice', return_value='en-US')
    return Code()

def test_locale_code(code_provider):
    # Test that locale_code() returns the mocked value
    locale_code = code_provider.locale_code()
    assert locale_code == 'en-US'
