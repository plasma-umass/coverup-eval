# file lib/ansible/utils/color.py:96-101
# lines [96, 98, 99, 100, 101]
# branches ['99->100', '99->101']

import pytest
from ansible.utils.color import colorize, stringc

# Mocking the ANSIBLE_COLOR constant
@pytest.fixture
def mock_ansible_color(mocker):
    mocker.patch('ansible.utils.color.ANSIBLE_COLOR', True)

# Test function to cover the missing lines/branches
def test_colorize_with_color(mock_ansible_color):
    lead = "TestLead"
    num = 1
    color = "green"
    result = colorize(lead, num, color)
    expected = stringc(f"{lead}={num:<4}", color)
    assert result == expected

def test_colorize_without_color(mock_ansible_color):
    lead = "TestLead"
    num = 0
    color = None
    result = colorize(lead, num, color)
    expected = f"{lead}={num:<4}"
    assert result == expected
