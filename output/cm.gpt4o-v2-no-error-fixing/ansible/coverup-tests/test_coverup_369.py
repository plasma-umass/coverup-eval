# file: lib/ansible/utils/color.py:96-101
# asked: {"lines": [96, 98, 99, 100, 101], "branches": [[99, 100], [99, 101]]}
# gained: {"lines": [96, 98, 99, 100, 101], "branches": [[99, 100], [99, 101]]}

import pytest
from ansible.utils.color import colorize, stringc, ANSIBLE_COLOR

def test_colorize_with_color(monkeypatch):
    # Ensure ANSIBLE_COLOR is True
    monkeypatch.setattr('ansible.utils.color.ANSIBLE_COLOR', True)
    
    lead = "test"
    num = 1
    color = "red"
    
    result = colorize(lead, num, color)
    
    # Check if the result is colorized
    assert result == stringc(f"{lead}={num:<4}", color)

def test_colorize_without_color(monkeypatch):
    # Ensure ANSIBLE_COLOR is True
    monkeypatch.setattr('ansible.utils.color.ANSIBLE_COLOR', True)
    
    lead = "test"
    num = 0
    color = "red"
    
    result = colorize(lead, num, color)
    
    # Check if the result is not colorized
    assert result == f"{lead}={num:<4}"

def test_colorize_ansible_color_off(monkeypatch):
    # Ensure ANSIBLE_COLOR is False
    monkeypatch.setattr('ansible.utils.color.ANSIBLE_COLOR', False)
    
    lead = "test"
    num = 1
    color = "red"
    
    result = colorize(lead, num, color)
    
    # Check if the result is not colorized
    assert result == f"{lead}={num:<4}"
