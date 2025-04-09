# file: lib/ansible/utils/color.py:73-93
# asked: {"lines": [73, 76, 77, 78, 79, 90, 91, 93], "branches": [[76, 77], [76, 93], [79, 90], [79, 91]]}
# gained: {"lines": [73, 76, 77, 78, 79, 90, 91, 93], "branches": [[76, 77], [76, 93], [79, 90], [79, 91]]}

import pytest
from ansible.utils.color import stringc

# Mocking ANSIBLE_COLOR and parsecolor
@pytest.fixture
def mock_ansible_color(monkeypatch):
    monkeypatch.setattr('ansible.utils.color.ANSIBLE_COLOR', True)
    monkeypatch.setattr('ansible.utils.color.parsecolor', lambda x: '31')  # Mocking parsecolor to return '31' for red color

def test_stringc_with_color(mock_ansible_color):
    result = stringc("Hello", "red")
    assert result == "\033[31mHello\033[0m"

def test_stringc_with_color_and_wrap_nonvisible_chars(mock_ansible_color):
    result = stringc("Hello", "red", wrap_nonvisible_chars=True)
    assert result == "\001\033[31m\002Hello\001\033[0m\002"

def test_stringc_without_color():
    result = stringc("Hello", "red")
    assert result == "Hello"
