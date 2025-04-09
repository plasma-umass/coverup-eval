# file: lib/ansible/plugins/filter/mathstuff.py:128-137
# asked: {"lines": [130, 131, 133, 134, 136, 137], "branches": [[130, 131], [130, 133], [133, 134], [133, 136]]}
# gained: {"lines": [130, 131, 133, 134, 136, 137], "branches": [[130, 131], [130, 133], [133, 134], [133, 136]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleFilterError
from jinja2.filters import do_min
from ansible.plugins.filter.mathstuff import min

def test_min_with_HAS_MIN_MAX(monkeypatch):
    # Mock HAS_MIN_MAX to be True
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', True)
    
    environment = MagicMock()
    a = [3, 1, 2]
    
    result = min(environment, a)
    
    assert result == 1

def test_min_without_HAS_MIN_MAX_no_kwargs(monkeypatch):
    # Mock HAS_MIN_MAX to be False
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    environment = MagicMock()
    a = [3, 1, 2]
    
    result = min(environment, a)
    
    assert result == 1

def test_min_without_HAS_MIN_MAX_with_kwargs(monkeypatch):
    # Mock HAS_MIN_MAX to be False
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    environment = MagicMock()
    a = [3, 1, 2]
    
    with pytest.raises(AnsibleFilterError) as excinfo:
        min(environment, a, key=lambda x: x)
    
    assert "Ansible's min filter does not support any keyword arguments" in str(excinfo.value)
