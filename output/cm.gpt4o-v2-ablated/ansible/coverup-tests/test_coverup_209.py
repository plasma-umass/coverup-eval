# file: lib/ansible/utils/color.py:96-101
# asked: {"lines": [96, 98, 99, 100, 101], "branches": [[99, 100], [99, 101]]}
# gained: {"lines": [96, 98, 99, 100, 101], "branches": [[99, 100], [99, 101]]}

import pytest
from ansible.utils.color import colorize

# Mocking ANSIBLE_COLOR and stringc
@pytest.fixture
def mock_ansible_color(monkeypatch):
    monkeypatch.setattr("ansible.utils.color.ANSIBLE_COLOR", True)

@pytest.fixture
def mock_stringc(monkeypatch):
    def mock_stringc(s, color):
        return f"colored({s}, {color})"
    monkeypatch.setattr("ansible.utils.color.stringc", mock_stringc)

def test_colorize_no_color():
    result = colorize("test", 0, None)
    assert result == "test=0   "

def test_colorize_with_color(mock_ansible_color, mock_stringc):
    result = colorize("test", 1, "red")
    assert result == "colored(test=1   , red)"

def test_colorize_no_ansible_color(monkeypatch):
    monkeypatch.setattr("ansible.utils.color.ANSIBLE_COLOR", False)
    result = colorize("test", 1, "red")
    assert result == "test=1   "

def test_colorize_no_color_with_nonzero_num(mock_ansible_color):
    result = colorize("test", 1, None)
    assert result == "test=1   "
