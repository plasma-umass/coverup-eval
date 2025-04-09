# file: string_utils/manipulation.py:250-277
# asked: {"lines": [261, 275], "branches": [[260, 261], [274, 275]]}
# gained: {"lines": [261, 275], "branches": [[260, 261], [274, 275]]}

import pytest
from string_utils.manipulation import __StringFormatter

@pytest.fixture
def string_formatter():
    class TestStringFormatter(__StringFormatter):
        def __init__(self, input_string):
            self.input_string = input_string

        def __placeholder_key(self):
            return f"__PLACEHOLDER_{len(self.input_string)}__"

        def __uppercase_first_char(self, match):
            return match.group(0).capitalize()

        def __remove_duplicates(self, match):
            return match.group(0)[0]

        def __ensure_right_space_only(self, match):
            return match.group(0).rstrip() + ' '

        def __ensure_left_space_only(self, match):
            return ' ' + match.group(0).lstrip()

        def __ensure_spaces_around(self, match):
            return ' ' + match.group(0).strip() + ' '

        def __remove_internal_spaces(self, match):
            return match.group(0).replace(' ', '')

        def __uppercase_first_letter_after_sign(self, match):
            return match.group(0)[0] + match.group(0)[1:].capitalize()

        def __fix_saxon_genitive(self, match):
            return match.group(0).replace("'", "’")

    return TestStringFormatter

def test_format_with_placeholders(string_formatter):
    input_string = "Check this link: http://example.com and email: test@example.com"
    formatter = string_formatter(input_string)
    formatted_string = formatter.format()
    assert "http://example.com" in formatted_string
    assert "test@example.com" in formatted_string

def test_format_with_prettify_rules(string_formatter):
    input_string = "this is a test.  this is only a test."
    formatter = string_formatter(input_string)
    formatted_string = formatter.format()
    assert formatted_string == "This is a test. This is only a test."

def test_format_with_combined_rules(string_formatter):
    input_string = "Check this link: http://example.com and email: test@example.com.  this is a test."
    formatter = string_formatter(input_string)
    formatted_string = formatter.format()
    assert "http://example.com" in formatted_string
    assert "test@example.com" in formatted_string
    assert "This is a test." in formatted_string
