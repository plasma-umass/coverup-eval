# file lib/ansible/parsing/quoting.py:27-31
# lines [27, 29, 30, 31]
# branches ['29->30', '29->31']

import pytest
from ansible.parsing.quoting import unquote, is_quoted

@pytest.mark.parametrize("input_string, expected_output", [
    ('"double_quoted_string"', 'double_quoted_string'),
    ("'single_quoted_string'", 'single_quoted_string'),
    ('unquoted_string', 'unquoted_string'),
    ('"mismatched_quotes', '"mismatched_quotes'),
    ("mismatched_quotes'", "mismatched_quotes'"),
    ('"embedded "quotes""', 'embedded "quotes"'),
    ("'embedded 'quotes''", "embedded 'quotes'"),
])
def test_unquote(input_string, expected_output):
    assert unquote(input_string) == expected_output
