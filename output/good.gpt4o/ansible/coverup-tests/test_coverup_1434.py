# file lib/ansible/plugins/filter/mathstuff.py:54-88
# lines [71, 72, 73, 74]
# branches ['60->exit', '85->84']

import pytest
from ansible.plugins.filter.mathstuff import unique, AnsibleFilterError
from jinja2 import Environment

def test_unique_with_case_sensitive_false(mocker):
    env = Environment()
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', True)
    def mock_do_unique(*args, **kwargs):
        raise TypeError("Mocked TypeError")
    mocker.patch('ansible.plugins.filter.mathstuff.do_unique', mock_do_unique)
    with pytest.raises(AnsibleFilterError, match="Jinja2's unique filter failed and we cannot fall back to Ansible's version"):
        unique(env, [1, 2, 2, 3], case_sensitive=False)

def test_unique_with_attribute(mocker):
    env = Environment()
    class Obj:
        def __init__(self, attr):
            self.attr = attr

    objs = [Obj(1), Obj(2), Obj(2), Obj(3)]
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', True)
    def mock_do_unique(*args, **kwargs):
        raise TypeError("Mocked TypeError")
    mocker.patch('ansible.plugins.filter.mathstuff.do_unique', mock_do_unique)
    with pytest.raises(AnsibleFilterError, match="Jinja2's unique filter failed and we cannot fall back to Ansible's version"):
        unique(env, objs, attribute='attr')

def test_unique_fallback(mocker):
    env = Environment()
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', False)
    with pytest.raises(AnsibleFilterError, match="Ansible's unique filter does not support case_sensitive=False nor attribute parameters"):
        unique(env, [1, 2, 2, 3], case_sensitive=False)

    with pytest.raises(AnsibleFilterError, match="Ansible's unique filter does not support case_sensitive=False nor attribute parameters"):
        unique(env, [1, 2, 2, 3], attribute='attr')

def test_unique_no_jinja2_unique(mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', False)
    env = Environment()
    result = unique(env, [1, 2, 2, 3])
    assert result == [1, 2, 3]

def test_unique_jinja2_unique_fallback(mocker):
    def mock_do_unique(*args, **kwargs):
        raise Exception("Mocked exception")

    mocker.patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', True)
    mocker.patch('ansible.plugins.filter.mathstuff.do_unique', mock_do_unique)
    env = Environment()
    result = unique(env, [1, 2, 2, 3])
    assert result == [1, 2, 3]
