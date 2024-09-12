# file: lib/ansible/plugins/filter/mathstuff.py:128-137
# asked: {"lines": [128, 129, 130, 131, 133, 134, 136, 137], "branches": [[130, 131], [130, 133], [133, 134], [133, 136]]}
# gained: {"lines": [128, 129, 130, 133, 134, 136, 137], "branches": [[130, 133], [133, 134], [133, 136]]}

import pytest
from jinja2 import Environment
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.mathstuff import min as ansible_min

def test_min_with_kwargs(monkeypatch):
    env = Environment()
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    with pytest.raises(AnsibleFilterError, match="Ansible's min filter does not support any keyword arguments. You need Jinja2 2.10 or later that provides their version of the filter."):
        ansible_min(env, [1, 2, 3], some_kwarg=True)

def test_min_without_kwargs(monkeypatch):
    env = Environment()
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    result = ansible_min(env, [1, 2, 3])
    assert result == 1
