# file tornado/escape.py:380-392
# lines [387, 388]
# branches []

import pytest
from tornado.escape import _convert_entity
import re

# Assuming _HTML_UNICODE_MAP is a dictionary defined in the tornado.escape module
# If it's not accessible, you might need to mock it or adjust the test accordingly.

@pytest.fixture
def mock_html_unicode_map(mocker):
    mocker.patch('tornado.escape._HTML_UNICODE_MAP', new_callable=dict)

def test_convert_entity_with_invalid_numeric_entity(mock_html_unicode_map):
    # This regex pattern should match the pattern used in the actual tornado.escape code
    pattern = re.compile(r"&(#?)(\w+);")
    
    # Test with an invalid numeric entity
    invalid_numeric_entity = "&#xyz;"
    match = pattern.match(invalid_numeric_entity)
    assert match is not None
    
    # Call the function that uses the _convert_entity function
    result = _convert_entity(match)
    
    # Assert that the result is the original invalid numeric entity
    assert result == "&#xyz;"

    # Clean up is handled by pytest's fixture scope
