# file: lib/ansible/utils/color.py:96-101
# asked: {"lines": [96, 98, 99, 100, 101], "branches": [[99, 100], [99, 101]]}
# gained: {"lines": [96, 98, 99, 100, 101], "branches": [[99, 100], [99, 101]]}

import pytest
from ansible.utils.color import colorize, stringc, ANSIBLE_COLOR

def test_colorize_with_color(monkeypatch):
    # Setup
    lead = "test"
    num = 1
    color = "red"
    
    # Ensure ANSIBLE_COLOR is True
    monkeypatch.setattr("ansible.utils.color.ANSIBLE_COLOR", True)
    
    # Execute
    result = colorize(lead, num, color)
    
    # Verify
    expected = stringc(f"{lead}={num:<4}", color)
    assert result == expected

def test_colorize_without_color(monkeypatch):
    # Setup
    lead = "test"
    num = 1
    color = None
    
    # Ensure ANSIBLE_COLOR is True
    monkeypatch.setattr("ansible.utils.color.ANSIBLE_COLOR", True)
    
    # Execute
    result = colorize(lead, num, color)
    
    # Verify
    expected = f"{lead}={num:<4}"
    assert result == expected

def test_colorize_num_zero(monkeypatch):
    # Setup
    lead = "test"
    num = 0
    color = "red"
    
    # Ensure ANSIBLE_COLOR is True
    monkeypatch.setattr("ansible.utils.color.ANSIBLE_COLOR", True)
    
    # Execute
    result = colorize(lead, num, color)
    
    # Verify
    expected = f"{lead}={num:<4}"
    assert result == expected
