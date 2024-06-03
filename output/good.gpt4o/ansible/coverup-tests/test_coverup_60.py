# file lib/ansible/plugins/filter/mathstuff.py:54-88
# lines [54, 57, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 79, 80, 83, 84, 85, 86, 88]
# branches ['60->exit', '60->61', '66->67', '66->76', '76->79', '76->88', '79->80', '79->83', '84->85', '84->88', '85->84', '85->86']

import pytest
from ansible.plugins.filter.mathstuff import unique, AnsibleFilterError
from jinja2 import Environment

@pytest.fixture
def environment():
    return Environment()

def test_unique_with_case_sensitive_false(environment, mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', True)
    mocker.patch('ansible.plugins.filter.mathstuff.do_unique', side_effect=TypeError("Mocked TypeError"))
    with pytest.raises(AnsibleFilterError, match="Jinja2's unique filter failed and we cannot fall back to Ansible's version"):
        unique(environment, ['a', 'A', 'b', 'B'], case_sensitive=False)

def test_unique_with_attribute(environment, mocker):
    class TestObj:
        def __init__(self, attr):
            self.attr = attr

    mocker.patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', True)
    mocker.patch('ansible.plugins.filter.mathstuff.do_unique', side_effect=TypeError("Mocked TypeError"))
    with pytest.raises(AnsibleFilterError, match="Jinja2's unique filter failed and we cannot fall back to Ansible's version"):
        unique(environment, [TestObj('a'), TestObj('A'), TestObj('b')], attribute='attr')

def test_unique_fallback_to_ansible(environment, mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', False)
    result = unique(environment, ['a', 'A', 'b', 'B'])
    assert result == ['a', 'A', 'b', 'B']

def test_unique_ansible_filter_error(environment, mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', False)
    with pytest.raises(AnsibleFilterError, match="Ansible's unique filter does not support case_sensitive=False nor attribute parameters"):
        unique(environment, ['a', 'A', 'b', 'B'], case_sensitive=False)

def test_unique_ansible_filter_error_with_attribute(environment, mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', False)
    class TestObj:
        def __init__(self, attr):
            self.attr = attr

    with pytest.raises(AnsibleFilterError, match="Ansible's unique filter does not support case_sensitive=False nor attribute parameters"):
        unique(environment, [TestObj('a'), TestObj('A'), TestObj('b')], attribute='attr')
