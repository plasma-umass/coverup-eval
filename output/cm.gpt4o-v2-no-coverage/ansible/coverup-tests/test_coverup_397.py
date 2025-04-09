# file: lib/ansible/plugins/filter/mathstuff.py:128-137
# asked: {"lines": [128, 129, 130, 131, 133, 134, 136, 137], "branches": [[130, 131], [130, 133], [133, 134], [133, 136]]}
# gained: {"lines": [128, 129, 130, 131, 133, 134, 136, 137], "branches": [[130, 131], [130, 133], [133, 134], [133, 136]]}

import pytest
from jinja2 import Environment
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.mathstuff import min as ansible_min
from jinja2.filters import do_min

def test_min_with_jinja2_min(monkeypatch):
    def mock_do_min(environment, a, **kwargs):
        return "mocked_min_result"
    
    monkeypatch.setattr("ansible.plugins.filter.mathstuff.HAS_MIN_MAX", True)
    monkeypatch.setattr("ansible.plugins.filter.mathstuff.do_min", mock_do_min)
    
    env = Environment()
    result = ansible_min(env, [3, 1, 2])
    assert result == "mocked_min_result"

def test_min_without_jinja2_min_no_kwargs(monkeypatch):
    monkeypatch.setattr("ansible.plugins.filter.mathstuff.HAS_MIN_MAX", False)
    
    env = Environment()
    result = ansible_min(env, [3, 1, 2])
    assert result == 1

def test_min_without_jinja2_min_with_kwargs(monkeypatch):
    monkeypatch.setattr("ansible.plugins.filter.mathstuff.HAS_MIN_MAX", False)
    
    env = Environment()
    with pytest.raises(AnsibleFilterError, match="Ansible's min filter does not support any keyword arguments."):
        ansible_min(env, [3, 1, 2], some_kwarg=True)
