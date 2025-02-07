# file: lib/ansible/plugins/filter/mathstuff.py:140-149
# asked: {"lines": [140, 141, 142, 143, 145, 146, 148, 149], "branches": [[142, 143], [142, 145], [145, 146], [145, 148]]}
# gained: {"lines": [140, 141, 142, 143, 145, 146, 148, 149], "branches": [[142, 143], [142, 145], [145, 146], [145, 148]]}

import pytest
from ansible.errors import AnsibleFilterError
from jinja2.filters import do_max
from jinja2 import Environment
from ansible.plugins.filter.mathstuff import max as ansible_max

def test_max_with_jinja2(monkeypatch):
    # Mock HAS_MIN_MAX to be True
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', True)
    
    env = Environment()
    result = ansible_max(env, [1, 2, 3])
    assert result == 3

def test_max_without_jinja2_no_kwargs(monkeypatch):
    # Mock HAS_MIN_MAX to be False
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    env = Environment()
    result = ansible_max(env, [1, 2, 3])
    assert result == 3

def test_max_without_jinja2_with_kwargs(monkeypatch):
    # Mock HAS_MIN_MAX to be False
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    env = Environment()
    with pytest.raises(AnsibleFilterError) as excinfo:
        ansible_max(env, [1, 2, 3], some_kwarg=True)
    assert "Ansible's max filter does not support any keyword arguments" in str(excinfo.value)
