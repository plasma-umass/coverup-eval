# file lib/ansible/parsing/quoting.py:27-31
# lines [30]
# branches ['29->30']

import pytest
from ansible.parsing.quoting import unquote, is_quoted

@pytest.fixture
def quoted_strings():
    return {
        'single_quotes': "'single_quoted_string'",
        'double_quotes': '"double_quoted_string"',
        'unquoted': 'unquoted_string',
        'mismatched_quotes': "'mismatched_string\"",
        'empty_single_quotes': "''",
        'empty_double_quotes': '""'
    }

def test_unquote_with_quoted_strings(quoted_strings):
    # Test with single quotes
    assert unquote(quoted_strings['single_quotes']) == 'single_quoted_string'
    # Test with double quotes
    assert unquote(quoted_strings['double_quotes']) == 'double_quoted_string'
    # Test with empty single quotes
    assert unquote(quoted_strings['empty_single_quotes']) == ''
    # Test with empty double quotes
    assert unquote(quoted_strings['empty_double_quotes']) == ''

def test_unquote_with_unquoted_string(quoted_strings):
    # Test with unquoted string
    assert unquote(quoted_strings['unquoted']) == 'unquoted_string'

def test_unquote_with_mismatched_quotes(quoted_strings):
    # Test with mismatched quotes
    assert unquote(quoted_strings['mismatched_quotes']) == "'mismatched_string\""
