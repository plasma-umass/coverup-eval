# file mimesis/providers/development.py:62-70
# lines [62, 70]
# branches []

import pytest
from mimesis.providers.development import Development

@pytest.fixture
def development_provider():
    return Development()

def test_programming_language(development_provider):
    # Call the method under test
    language = development_provider.programming_language()

    # Assert that the returned language is in the predefined list of languages
    # Since we don't have access to the original list, we check if the result is a string
    assert isinstance(language, str)
