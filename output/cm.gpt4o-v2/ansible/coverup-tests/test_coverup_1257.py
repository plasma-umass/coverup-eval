# file: lib/ansible/plugins/filter/mathstuff.py:128-137
# asked: {"lines": [131], "branches": [[130, 131]]}
# gained: {"lines": [131], "branches": [[130, 131]]}

import pytest
from unittest.mock import patch
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.mathstuff import min as ansible_min

def test_min_with_has_min_max(monkeypatch):
    # Mock HAS_MIN_MAX to be True
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', True)
    
    # Mock do_min to return a known value
    with patch('ansible.plugins.filter.mathstuff.do_min', return_value=1) as mock_do_min:
        result = ansible_min(None, [3, 1, 2])
        mock_do_min.assert_called_once_with(None, [3, 1, 2])
        assert result == 1

def test_min_without_has_min_max_no_kwargs(monkeypatch):
    # Mock HAS_MIN_MAX to be False
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    result = ansible_min(None, [3, 1, 2])
    assert result == 1

def test_min_without_has_min_max_with_kwargs(monkeypatch):
    # Mock HAS_MIN_MAX to be False
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    with pytest.raises(AnsibleFilterError, match="Ansible's min filter does not support any keyword arguments."):
        ansible_min(None, [3, 1, 2], some_kwarg=True)
