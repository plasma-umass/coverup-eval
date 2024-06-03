# file lib/ansible/utils/color.py:73-93
# lines [73, 76, 77, 78, 79, 90, 91, 93]
# branches ['76->77', '76->93', '79->90', '79->91']

import pytest
from unittest import mock

# Assuming the following functions and variables are defined in ansible.utils.color
# from ansible.utils.color import stringc, ANSIBLE_COLOR, parsecolor

# Mocking the parsecolor function and ANSIBLE_COLOR variable for testing
@pytest.fixture
def mock_parsecolor(mocker):
    return mocker.patch('ansible.utils.color.parsecolor', return_value='31')

@pytest.fixture
def mock_ansible_color(mocker):
    return mocker.patch('ansible.utils.color.ANSIBLE_COLOR', True)

def test_stringc_with_color(mock_parsecolor, mock_ansible_color):
    from ansible.utils.color import stringc

    text = "Hello\nWorld"
    color = "red"
    result = stringc(text, color)
    expected = "\033[31mHello\033[0m\n\033[31mWorld\033[0m"
    assert result == expected

def test_stringc_with_wrap_nonvisible_chars(mock_parsecolor, mock_ansible_color):
    from ansible.utils.color import stringc

    text = "Hello\nWorld"
    color = "red"
    result = stringc(text, color, wrap_nonvisible_chars=True)
    expected = "\001\033[31m\002Hello\001\033[0m\002\n\001\033[31m\002World\001\033[0m\002"
    assert result == expected

def test_stringc_without_color(mocker):
    from ansible.utils.color import stringc

    mocker.patch('ansible.utils.color.ANSIBLE_COLOR', False)
    text = "Hello\nWorld"
    color = "red"
    result = stringc(text, color)
    expected = "Hello\nWorld"
    assert result == expected
