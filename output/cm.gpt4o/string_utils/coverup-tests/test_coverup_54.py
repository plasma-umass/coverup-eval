# file string_utils/manipulation.py:250-277
# lines [261, 275]
# branches ['260->261', '274->275']

import pytest
import re
from string_utils.manipulation import __StringFormatter

@pytest.fixture
def mock_formatter(mocker):
    mocker.patch('string_utils.manipulation.URLS_RE', re.compile(r'http://example\.com'))
    mocker.patch('string_utils.manipulation.EMAILS_RE', re.compile(r'test@example\.com'))
    mocker.patch('string_utils.manipulation.PRETTIFY_RE', {
        'UPPERCASE_FIRST_LETTER': mocker.Mock(sub=lambda func, text: text),
        'DUPLICATES': mocker.Mock(sub=lambda func, text: text),
        'RIGHT_SPACE': mocker.Mock(sub=lambda func, text: text),
        'LEFT_SPACE': mocker.Mock(sub=lambda func, text: text),
        'SPACES_AROUND': mocker.Mock(sub=lambda func, text: text),
        'SPACES_INSIDE': mocker.Mock(sub=lambda func, text: text),
        'UPPERCASE_AFTER_SIGN': mocker.Mock(sub=lambda func, text: text),
        'SAXON_GENITIVE': mocker.Mock(sub=lambda func, text: text),
    })
    return __StringFormatter("")

def test_format_with_placeholders(mock_formatter):
    mock_formatter.input_string = "Visit http://example.com or contact test@example.com"
    mock_formatter.__placeholder_key = lambda: "PLACEHOLDER"
    mock_formatter.__uppercase_first_char = lambda match: match.group(0)
    mock_formatter.__remove_duplicates = lambda match: match.group(0)
    mock_formatter.__ensure_right_space_only = lambda match: match.group(0)
    mock_formatter.__ensure_left_space_only = lambda match: match.group(0)
    mock_formatter.__ensure_spaces_around = lambda match: match.group(0)
    mock_formatter.__remove_internal_spaces = lambda match: match.group(0)
    mock_formatter.__uppercase_first_letter_after_sign = lambda match: match.group(0)
    mock_formatter.__fix_saxon_genitive = lambda match: match.group(0)

    result = mock_formatter.format()
    
    assert "http://example.com" in result
    assert "test@example.com" in result
