# file: lib/ansible/plugins/filter/mathstuff.py:128-137
# asked: {"lines": [130, 131, 133, 134, 136, 137], "branches": [[130, 131], [130, 133], [133, 134], [133, 136]]}
# gained: {"lines": [130, 131, 133, 134, 136, 137], "branches": [[130, 131], [130, 133], [133, 134], [133, 136]]}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.mathstuff import min as ansible_min

def test_min_with_kwargs(monkeypatch):
    def mock_do_min(environment, a, **kwargs):
        return min(a)

    monkeypatch.setattr('ansible.plugins.filter.mathstuff.do_min', mock_do_min)
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', True)
    
    result = ansible_min(None, [3, 1, 2], key=lambda x: x)
    assert result == 1

def test_min_without_kwargs(monkeypatch):
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    result = ansible_min(None, [3, 1, 2])
    assert result == 1

def test_min_with_unsupported_kwargs(monkeypatch):
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    with pytest.raises(AnsibleFilterError) as excinfo:
        ansible_min(None, [3, 1, 2], key=lambda x: x)
    assert "Ansible's min filter does not support any keyword arguments" in str(excinfo.value)
