# file: string_utils/manipulation.py:250-277
# asked: {"lines": [261, 275], "branches": [[260, 261], [274, 275]]}
# gained: {"lines": [261, 275], "branches": [[260, 261], [274, 275]]}

import pytest
from string_utils.manipulation import __StringFormatter

@pytest.fixture
def formatter():
    class TestFormatter(__StringFormatter):
        def __init__(self, input_string):
            self.input_string = input_string
        def __placeholder_key(self):
            return "PLACEHOLDER"
    return TestFormatter

def test_format_with_urls(formatter):
    input_string = "Check this link: http://example.com and this one: https://example.org"
    fmt = formatter(input_string)
    result = fmt.format()
    assert "http://example.com" in result
    assert "https://example.org" in result

def test_format_with_emails(formatter):
    input_string = "Contact us at test@example.com or support@example.org"
    fmt = formatter(input_string)
    result = fmt.format()
    assert "test@example.com" in result
    assert "support@example.org" in result

def test_format_with_placeholders(formatter):
    input_string = "Visit http://example.com and email test@example.com"
    fmt = formatter(input_string)
    result = fmt.format()
    assert "http://example.com" in result
    assert "test@example.com" in result
