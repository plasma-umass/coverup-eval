# file lib/ansible/plugins/filter/mathstuff.py:140-149
# lines [143]
# branches ['142->143']

import pytest
from ansible.plugins.filter.mathstuff import max as ansible_max
from ansible.errors import AnsibleFilterError
from unittest.mock import patch

def test_max_with_kwargs(mocker):
    # Mock the environment and HAS_MIN_MAX to ensure the correct branch is taken
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', True)
    mocker.patch('ansible.plugins.filter.mathstuff.do_max', return_value=42)
    
    environment = mocker.Mock()
    a = [1, 2, 3]
    kwargs = {'key': lambda x: x}

    result = ansible_max(environment, a, **kwargs)
    
    assert result == 42

def test_max_without_kwargs(mocker):
    # Mock the environment and HAS_MIN_MAX to ensure the correct branch is taken
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    environment = mocker.Mock()
    a = [1, 2, 3]
    kwargs = {}

    result = ansible_max(environment, a, **kwargs)
    
    assert result == 3

def test_max_with_unsupported_kwargs(mocker):
    # Mock the environment and HAS_MIN_MAX to ensure the correct branch is taken
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    
    environment = mocker.Mock()
    a = [1, 2, 3]
    kwargs = {'key': lambda x: x}

    with pytest.raises(AnsibleFilterError) as excinfo:
        ansible_max(environment, a, **kwargs)
    
    assert "Ansible's max filter does not support any keyword arguments" in str(excinfo.value)
