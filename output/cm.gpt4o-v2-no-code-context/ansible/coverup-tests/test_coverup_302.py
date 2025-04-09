# file: lib/ansible/plugins/filter/mathstuff.py:140-149
# asked: {"lines": [140, 141, 142, 143, 145, 146, 148, 149], "branches": [[142, 143], [142, 145], [145, 146], [145, 148]]}
# gained: {"lines": [140, 141, 142, 145, 146, 148, 149], "branches": [[142, 145], [145, 146], [145, 148]]}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.mathstuff import max as ansible_max

def test_max_with_kwargs(monkeypatch):
    # Mock HAS_MIN_MAX to be False to enter the else branch
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    with pytest.raises(AnsibleFilterError) as excinfo:
        ansible_max(None, [1, 2, 3], some_kwarg=True)
    
    assert "Ansible's max filter does not support any keyword arguments" in str(excinfo.value)

def test_max_without_kwargs(monkeypatch):
    # Mock HAS_MIN_MAX to be False to enter the else branch
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    result = ansible_max(None, [1, 2, 3])
    
    assert result == 3
