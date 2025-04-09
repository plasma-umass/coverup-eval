# file: lib/ansible/plugins/filter/mathstuff.py:128-137
# asked: {"lines": [128, 129, 130, 131, 133, 134, 136, 137], "branches": [[130, 131], [130, 133], [133, 134], [133, 136]]}
# gained: {"lines": [128, 129, 130, 133, 134, 136, 137], "branches": [[130, 133], [133, 134], [133, 136]]}

import pytest
from ansible.plugins.filter.mathstuff import min as ansible_min
from ansible.errors import AnsibleFilterError
from jinja2 import Environment

def test_min_with_kwargs(monkeypatch):
    # Mock HAS_MIN_MAX to be False to enter the else branch
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    # Create a mock environment
    env = Environment()
    
    # Test that providing kwargs raises an AnsibleFilterError
    with pytest.raises(AnsibleFilterError) as excinfo:
        ansible_min(env, [1, 2, 3], some_kwarg=True)
    
    assert "Ansible's min filter does not support any keyword arguments" in str(excinfo.value)

def test_min_without_kwargs(monkeypatch):
    # Mock HAS_MIN_MAX to be False to enter the else branch
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    # Create a mock environment
    env = Environment()
    
    # Test that the min function works without kwargs
    result = ansible_min(env, [1, 2, 3])
    
    assert result == 1
