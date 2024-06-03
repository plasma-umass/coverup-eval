# file lib/ansible/plugins/filter/mathstuff.py:128-137
# lines [131]
# branches ['130->131']

import pytest
from unittest import mock
from ansible.plugins.filter.mathstuff import min, AnsibleFilterError

@pytest.fixture
def mock_environmentfilter(mocker):
    return mocker.patch('ansible.plugins.filter.mathstuff.environmentfilter', lambda x: x)

@pytest.fixture
def mock_do_min(mocker):
    return mocker.patch('ansible.plugins.filter.mathstuff.do_min')

@pytest.fixture
def mock_has_min_max(mocker):
    return mocker.patch('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', True)

def test_min_with_has_min_max(mock_environmentfilter, mock_do_min, mock_has_min_max):
    environment = mock.Mock()
    a = [3, 1, 2]
    kwargs = {'key': lambda x: x}
    
    result = min(environment, a, **kwargs)
    
    mock_do_min.assert_called_once_with(environment, a, **kwargs)
    assert result == mock_do_min.return_value

def test_min_without_has_min_max_no_kwargs(mock_environmentfilter, mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    environment = mock.Mock()
    a = [3, 1, 2]
    
    result = min(environment, a)
    
    assert result == 1

def test_min_without_has_min_max_with_kwargs(mock_environmentfilter, mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)
    environment = mock.Mock()
    a = [3, 1, 2]
    kwargs = {'key': lambda x: x}
    
    with pytest.raises(AnsibleFilterError, match="Ansible's min filter does not support any keyword arguments."):
        min(environment, a, **kwargs)
