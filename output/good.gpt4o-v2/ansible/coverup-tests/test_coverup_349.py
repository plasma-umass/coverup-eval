# file: lib/ansible/utils/color.py:73-93
# asked: {"lines": [73, 76, 77, 78, 79, 90, 91, 93], "branches": [[76, 77], [76, 93], [79, 90], [79, 91]]}
# gained: {"lines": [73, 76, 77, 78, 79, 90, 91, 93], "branches": [[76, 77], [76, 93], [79, 90], [79, 91]]}

import pytest
from ansible.utils.color import stringc, ANSIBLE_COLOR
from ansible.utils.color import parsecolor

@pytest.fixture
def enable_ansible_color(monkeypatch):
    monkeypatch.setattr("ansible.utils.color.ANSIBLE_COLOR", True)
    yield
    monkeypatch.undo()

def test_stringc_with_color(enable_ansible_color):
    text = "Hello, World!"
    color = "red"
    expected_color_code = parsecolor(color)
    expected_output = f"\033[{expected_color_code}m{text}\033[0m"
    assert stringc(text, color) == expected_output

def test_stringc_without_color(monkeypatch):
    monkeypatch.setattr("ansible.utils.color.ANSIBLE_COLOR", False)
    text = "Hello, World!"
    color = "red"
    assert stringc(text, color) == text

def test_stringc_with_wrap_nonvisible_chars(enable_ansible_color):
    text = "Hello, World!"
    color = "red"
    expected_color_code = parsecolor(color)
    expected_output = f"\001\033[{expected_color_code}m\002{text}\001\033[0m\002"
    assert stringc(text, color, wrap_nonvisible_chars=True) == expected_output

def test_stringc_multiline_text(enable_ansible_color):
    text = "Hello\nWorld"
    color = "red"
    expected_color_code = parsecolor(color)
    expected_output = f"\033[{expected_color_code}mHello\033[0m\n\033[{expected_color_code}mWorld\033[0m"
    assert stringc(text, color) == expected_output
