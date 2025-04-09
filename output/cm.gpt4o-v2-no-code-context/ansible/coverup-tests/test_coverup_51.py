# file: lib/ansible/plugins/filter/mathstuff.py:54-88
# asked: {"lines": [54, 57, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 79, 80, 83, 84, 85, 86, 88], "branches": [[60, 0], [60, 61], [66, 67], [66, 76], [76, 79], [76, 88], [79, 80], [79, 83], [84, 85], [84, 88], [85, 84], [85, 86]]}
# gained: {"lines": [54, 57, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 76, 79, 83, 84, 85, 86, 88], "branches": [[60, 61], [66, 67], [66, 76], [76, 79], [76, 88], [79, 83], [84, 85], [84, 88], [85, 84], [85, 86]]}

import pytest
from ansible.plugins.filter.mathstuff import unique, AnsibleFilterError
from jinja2 import Environment

def test_unique_with_case_sensitive_false(monkeypatch):
    env = Environment()
    a = ['a', 'A', 'b', 'B']
    
    def mock_do_unique(*args, **kwargs):
        raise TypeError("Mocked TypeError for testing")
    
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.do_unique', mock_do_unique)
    
    with pytest.raises(AnsibleFilterError, match="Jinja2's unique filter failed and we cannot fall back to Ansible's version"):
        unique(env, a, case_sensitive=False)

def test_unique_with_attribute(monkeypatch):
    env = Environment()
    a = [{'name': 'a'}, {'name': 'A'}, {'name': 'b'}, {'name': 'B'}]
    
    def mock_do_unique(*args, **kwargs):
        raise TypeError("Mocked TypeError for testing")
    
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.do_unique', mock_do_unique)
    
    with pytest.raises(AnsibleFilterError, match="Jinja2's unique filter failed and we cannot fall back to Ansible's version"):
        unique(env, a, attribute='name')

def test_unique_fallback_no_unique_support(monkeypatch):
    env = Environment()
    a = ['a', 'b', 'a', 'c']
    
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_UNIQUE', False)
    
    result = unique(env, a)
    assert result == ['a', 'b', 'c']

def test_unique_fallback_with_error(monkeypatch):
    env = Environment()
    a = ['a', 'b', 'a', 'c']
    
    def mock_do_unique(*args, **kwargs):
        raise Exception("Mocked Exception for testing")
    
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.do_unique', mock_do_unique)
    
    with pytest.raises(AnsibleFilterError, match="Jinja2's unique filter failed and we cannot fall back to Ansible's version"):
        unique(env, a, case_sensitive=False, attribute='name')

def test_unique_no_error():
    env = Environment()
    a = ['a', 'b', 'a', 'c']
    result = unique(env, a)
    assert result == ['a', 'b', 'c']
