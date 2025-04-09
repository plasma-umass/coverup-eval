# file: lib/ansible/utils/color.py:73-93
# asked: {"lines": [77, 78, 79, 90, 91], "branches": [[76, 77], [79, 90], [79, 91]]}
# gained: {"lines": [77, 78, 79, 90, 91], "branches": [[76, 77], [79, 90], [79, 91]]}

import pytest
from unittest.mock import patch

# Assuming the ANSIBLE_COLOR and parsecolor are defined somewhere in the module
# For the purpose of this test, we will mock them

# Mocking ANSIBLE_COLOR and parsecolor
@pytest.fixture
def mock_ansible_color(monkeypatch):
    monkeypatch.setattr("ansible.utils.color.ANSIBLE_COLOR", True)

@pytest.fixture
def mock_parsecolor(monkeypatch):
    def mock_parsecolor_func(color):
        return "31"  # ANSI code for red
    monkeypatch.setattr("ansible.utils.color.parsecolor", mock_parsecolor_func)

def test_stringc_with_color(mock_ansible_color, mock_parsecolor):
    from ansible.utils.color import stringc

    text = "Hello, World!"
    color = "red"
    result = stringc(text, color)
    expected = "\033[31mHello, World!\033[0m"
    assert result == expected

def test_stringc_without_color(monkeypatch):
    from ansible.utils.color import stringc

    monkeypatch.setattr("ansible.utils.color.ANSIBLE_COLOR", False)
    text = "Hello, World!"
    color = "red"
    result = stringc(text, color)
    assert result == text

def test_stringc_with_wrap_nonvisible_chars(mock_ansible_color, mock_parsecolor):
    from ansible.utils.color import stringc

    text = "Hello, World!"
    color = "red"
    result = stringc(text, color, wrap_nonvisible_chars=True)
    expected = "\001\033[31m\002Hello, World!\001\033[0m\002"
    assert result == expected

def test_stringc_multiline_with_color(mock_ansible_color, mock_parsecolor):
    from ansible.utils.color import stringc

    text = "Hello,\nWorld!"
    color = "red"
    result = stringc(text, color)
    expected = "\033[31mHello,\033[0m\n\033[31mWorld!\033[0m"
    assert result == expected

def test_stringc_multiline_with_wrap_nonvisible_chars(mock_ansible_color, mock_parsecolor):
    from ansible.utils.color import stringc

    text = "Hello,\nWorld!"
    color = "red"
    result = stringc(text, color, wrap_nonvisible_chars=True)
    expected = "\001\033[31m\002Hello,\001\033[0m\002\n\001\033[31m\002World!\001\033[0m\002"
    assert result == expected
