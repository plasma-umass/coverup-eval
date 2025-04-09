# file: lib/ansible/plugins/filter/mathstuff.py:54-88
# asked: {"lines": [59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 79, 80, 83, 84, 85, 86, 88], "branches": [[60, 0], [60, 61], [66, 67], [66, 76], [76, 79], [76, 88], [79, 80], [79, 83], [84, 85], [84, 88], [85, 84], [85, 86]]}
# gained: {"lines": [59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 79, 80, 83, 84, 85, 86, 88], "branches": [[60, 0], [60, 61], [66, 67], [66, 76], [76, 79], [79, 80], [79, 83], [84, 85], [84, 88], [85, 84], [85, 86]]}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.mathstuff import unique
from jinja2 import Environment

# Mocking HAS_UNIQUE and do_unique for testing purposes
HAS_UNIQUE = True

def do_unique(environment, a, case_sensitive, attribute):
    if attribute:
        raise TypeError("Mocked TypeError for attribute")
    if not case_sensitive:
        raise Exception("Mocked Exception for case_sensitive")
    return set(a)

@pytest.fixture
def environment():
    return Environment()

def test_unique_with_jinja2_unique(environment, monkeypatch):
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_UNIQUE', True)
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.do_unique', do_unique)
    
    result = unique(environment, [1, 2, 2, 3])
    assert result == [1, 2, 3]

def test_unique_with_jinja2_unique_type_error(environment, monkeypatch):
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_UNIQUE', True)
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.do_unique', do_unique)
    
    with pytest.raises(AnsibleFilterError):
        unique(environment, [1, 2, 2, 3], attribute='some_attr')

def test_unique_with_jinja2_unique_exception(environment, monkeypatch):
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_UNIQUE', True)
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.do_unique', do_unique)
    
    with pytest.raises(AnsibleFilterError):
        unique(environment, [1, 2, 2, 3], case_sensitive=False)

def test_unique_without_jinja2_unique(environment, monkeypatch):
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_UNIQUE', False)
    
    result = unique(environment, [1, 2, 2, 3])
    assert result == [1, 2, 3]

def test_unique_without_jinja2_unique_case_sensitive(environment, monkeypatch):
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_UNIQUE', False)
    
    with pytest.raises(AnsibleFilterError):
        unique(environment, [1, 2, 2, 3], case_sensitive=False)

def test_unique_without_jinja2_unique_attribute(environment, monkeypatch):
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.HAS_UNIQUE', False)
    
    with pytest.raises(AnsibleFilterError):
        unique(environment, [1, 2, 2, 3], attribute='some_attr')
