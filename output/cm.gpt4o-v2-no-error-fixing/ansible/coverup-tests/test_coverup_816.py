# file: lib/ansible/utils/color.py:73-93
# asked: {"lines": [90], "branches": [[79, 90]]}
# gained: {"lines": [90], "branches": [[79, 90]]}

import pytest
from ansible.utils.color import stringc

def test_stringc_with_wrap_nonvisible_chars(monkeypatch):
    # Mock ANSIBLE_COLOR to be True
    monkeypatch.setattr('ansible.utils.color.ANSIBLE_COLOR', True)
    
    # Mock parsecolor to return a specific color code
    def mock_parsecolor(color):
        return '31'  # ANSI code for red
    monkeypatch.setattr('ansible.utils.color.parsecolor', mock_parsecolor)
    
    text = "Hello\nWorld"
    color = "red"
    result = stringc(text, color, wrap_nonvisible_chars=True)
    
    expected = "\001\033[31m\002Hello\001\033[0m\002\n\001\033[31m\002World\001\033[0m\002"
    assert result == expected
