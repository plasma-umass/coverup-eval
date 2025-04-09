# file lib/ansible/plugins/filter/mathstuff.py:140-149
# lines [140, 141, 142, 143, 145, 146, 148, 149]
# branches ['142->143', '142->145', '145->146', '145->148']

import pytest
from ansible.plugins.filter.mathstuff import max as ansible_max, AnsibleFilterError
from jinja2 import Environment

def test_max_with_kwargs(mocker):
    # Mocking the environment and HAS_MIN_MAX
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    environment = Environment()

    with pytest.raises(AnsibleFilterError) as excinfo:
        ansible_max(environment, [1, 2, 3], some_kwarg=True)
    assert "Ansible's max filter does not support any keyword arguments" in str(excinfo.value)

def test_max_without_kwargs(mocker):
    # Mocking the environment and HAS_MIN_MAX
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    environment = Environment()

    result = ansible_max(environment, [1, 2, 3])
    assert result == 3
