# file lib/ansible/utils/color.py:73-93
# lines [73, 76, 77, 78, 79, 90, 91, 93]
# branches ['76->77', '76->93', '79->90', '79->91']

import pytest
from unittest.mock import patch

# Assuming the parsecolor function is defined in the same module and maps color names to ANSI codes
@pytest.fixture
def mock_parsecolor():
    with patch('ansible.utils.color.parsecolor') as mock:
        mock.side_effect = lambda color: {
            'red': '0;31',
            'green': '0;32',
            'blue': '0;34',
            'yellow': '0;33',
            'cyan': '0;36'
        }.get(color, '0')
        yield mock

@pytest.fixture
def mock_ansible_color():
    with patch('ansible.utils.color.ANSIBLE_COLOR', new=True):
        yield

# Assuming the stringc function is defined in the same module
from ansible.utils.color import stringc

def test_stringc_with_wrap_nonvisible_chars(mock_ansible_color, mock_parsecolor):
    text = "Test text"
    color = "red"
    result = stringc(text, color, wrap_nonvisible_chars=True)
    expected = "\001\033[0;31m\002Test text\001\033[0m\002"
    assert result == expected

def test_stringc_without_wrap_nonvisible_chars(mock_ansible_color, mock_parsecolor):
    text = "Test text"
    color = "green"
    result = stringc(text, color, wrap_nonvisible_chars=False)
    expected = "\033[0;32mTest text\033[0m"
    assert result == expected

def test_stringc_with_newlines_and_wrap_nonvisible_chars(mock_ansible_color, mock_parsecolor):
    text = "Test\ntext"
    color = "blue"
    result = stringc(text, color, wrap_nonvisible_chars=True)
    expected = "\001\033[0;34m\002Test\001\033[0m\002\n\001\033[0;34m\002text\001\033[0m\002"
    assert result == expected

def test_stringc_with_newlines_without_wrap_nonvisible_chars(mock_ansible_color, mock_parsecolor):
    text = "Test\ntext"
    color = "yellow"
    result = stringc(text, color, wrap_nonvisible_chars=False)
    expected = "\033[0;33mTest\033[0m\n\033[0;33mtext\033[0m"
    assert result == expected

def test_stringc_without_ansi_color():
    with patch('ansible.utils.color.ANSIBLE_COLOR', new=False):
        text = "Test text"
        color = "cyan"
        result = stringc(text, color)
        assert result == text
