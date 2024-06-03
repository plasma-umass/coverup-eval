# file lib/ansible/plugins/filter/mathstuff.py:128-137
# lines [128, 129, 130, 131, 133, 134, 136, 137]
# branches ['130->131', '130->133', '133->134', '133->136']

import pytest
from ansible.plugins.filter.mathstuff import min as ansible_min, AnsibleFilterError
from jinja2 import Environment

def test_min_with_kwargs(mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    environment = Environment()
    with pytest.raises(AnsibleFilterError, match="Ansible's min filter does not support any keyword arguments."):
        ansible_min(environment, [1, 2, 3], some_kwarg=True)

def test_min_without_kwargs(mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    environment = Environment()
    result = ansible_min(environment, [1, 2, 3])
    assert result == 1
