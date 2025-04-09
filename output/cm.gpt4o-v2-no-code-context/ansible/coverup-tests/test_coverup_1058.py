# file: lib/ansible/plugins/filter/mathstuff.py:140-149
# asked: {"lines": [143], "branches": [[142, 143]]}
# gained: {"lines": [143], "branches": [[142, 143]]}

import pytest
from ansible.plugins.filter.mathstuff import max as ansible_max, AnsibleFilterError

def test_max_with_kwargs(monkeypatch):
    def mock_do_max(environment, a, **kwargs):
        return "mocked"

    monkeypatch.setattr('ansible.plugins.filter.mathstuff.do_max', mock_do_max)
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', True)

    result = ansible_max(None, [1, 2, 3], some_kwarg=True)
    assert result == "mocked"

def test_max_without_kwargs(monkeypatch):
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)

    result = ansible_max(None, [1, 2, 3])
    assert result == 3

def test_max_with_unsupported_kwargs(monkeypatch):
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)

    with pytest.raises(AnsibleFilterError) as excinfo:
        ansible_max(None, [1, 2, 3], some_kwarg=True)
    assert "Ansible's max filter does not support any keyword arguments" in str(excinfo.value)
