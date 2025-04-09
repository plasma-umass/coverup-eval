# file: lib/ansible/utils/color.py:96-101
# asked: {"lines": [100], "branches": [[99, 100]]}
# gained: {"lines": [100], "branches": [[99, 100]]}

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

def test_colorize_with_zero_num(monkeypatch):
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

def test_colorize_ansible_color_false(monkeypatch):
    # Setup
    lead = "test"
    num = 1
    color = "red"
    
    # Ensure ANSIBLE_COLOR is False
    monkeypatch.setattr("ansible.utils.color.ANSIBLE_COLOR", False)
    
    # Execute
    result = colorize(lead, num, color)
    
    # Verify
    expected = f"{lead}={num:<4}"
    assert result == expected
