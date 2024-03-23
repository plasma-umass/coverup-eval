# file lib/ansible/utils/unicode.py:28-33
# lines [28, 33]
# branches []

import pytest
from ansible.utils.unicode import unicode_wrap, to_text

def fake_func_returning_bytes():
    return b'byte_string'

def fake_func_returning_text():
    return 'text_string'

def fake_func_returning_nonstring():
    return 12345

@pytest.fixture
def mock_to_text(mocker):
    return mocker.patch('ansible.utils.unicode.to_text', side_effect=to_text)

def test_unicode_wrap_with_bytes(mock_to_text):
    result = unicode_wrap(fake_func_returning_bytes)
    assert result == 'byte_string'
    mock_to_text.assert_called_once_with(b'byte_string', nonstring='passthru')

def test_unicode_wrap_with_text(mock_to_text):
    result = unicode_wrap(fake_func_returning_text)
    assert result == 'text_string'
    mock_to_text.assert_called_once_with('text_string', nonstring='passthru')

def test_unicode_wrap_with_nonstring(mock_to_text):
    result = unicode_wrap(fake_func_returning_nonstring)
    assert result == 12345
    mock_to_text.assert_called_once_with(12345, nonstring='passthru')
