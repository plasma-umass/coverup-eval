# file: lib/ansible/plugins/filter/mathstuff.py:128-137
# asked: {"lines": [131], "branches": [[130, 131]]}
# gained: {"lines": [131], "branches": [[130, 131]]}

import pytest
from ansible.plugins.filter.mathstuff import min as ansible_min
from ansible.errors import AnsibleFilterError

def test_min_with_kwargs(monkeypatch):
    # Mock HAS_MIN_MAX to be True to ensure line 131 is executed
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', True)
    
    # Mock do_min to verify it gets called
    def mock_do_min(environment, a, **kwargs):
        return "mocked_result"
    
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.do_min', mock_do_min)
    
    result = ansible_min(None, [1, 2, 3], some_kwarg="value")
    assert result == "mocked_result"

def test_min_without_kwargs(monkeypatch):
    # Mock HAS_MIN_MAX to be False to ensure the else branch is executed
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    result = ansible_min(None, [1, 2, 3])
    assert result == 1

def test_min_with_unsupported_kwargs(monkeypatch):
    # Mock HAS_MIN_MAX to be False to ensure the else branch is executed
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    with pytest.raises(AnsibleFilterError, match="Ansible's min filter does not support any keyword arguments."):
        ansible_min(None, [1, 2, 3], some_kwarg="value")
