# file: lib/ansible/plugins/filter/mathstuff.py:140-149
# asked: {"lines": [140, 141, 142, 143, 145, 146, 148, 149], "branches": [[142, 143], [142, 145], [145, 146], [145, 148]]}
# gained: {"lines": [140, 141, 142, 143, 145, 146, 148, 149], "branches": [[142, 143], [142, 145], [145, 146], [145, 148]]}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.mathstuff import max as ansible_max

def test_max_with_kwargs(monkeypatch):
    def mock_do_max(environment, a, **kwargs):
        return max(a)

    monkeypatch.setattr('ansible.plugins.filter.mathstuff.do_max', mock_do_max)
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', True)
    
    result = ansible_max(None, [1, 2, 3], key=lambda x: -x)
    assert result == 3

def test_max_without_kwargs(monkeypatch):
    def mock_do_max(environment, a, **kwargs):
        return max(a)

    monkeypatch.setattr('ansible.plugins.filter.mathstuff.do_max', mock_do_max)
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', True)
    
    result = ansible_max(None, [1, 2, 3])
    assert result == 3

def test_max_no_min_max_with_kwargs(monkeypatch):
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    with pytest.raises(AnsibleFilterError) as excinfo:
        ansible_max(None, [1, 2, 3], key=lambda x: -x)
    assert "Ansible's max filter does not support any keyword arguments." in str(excinfo.value)

def test_max_no_min_max_without_kwargs(monkeypatch):
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    result = ansible_max(None, [1, 2, 3])
    assert result == 3
