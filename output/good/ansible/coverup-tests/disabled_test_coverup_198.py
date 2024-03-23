# file lib/ansible/vars/manager.py:80-108
# lines [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 95, 96, 99, 102, 103, 104, 107, 108]
# branches []

import os
import pytest
from hashlib import sha1
from collections import defaultdict
from ansible.errors import AnsibleError
from ansible.utils.display import Display
from ansible.vars.manager import VariableManager
from ansible.vars.fact_cache import FactCache

# Mocking the necessary functions and classes
def mock_load_options_vars(version_info):
    return {'basedir': '/some/safe/path'}

def mock_load_extra_vars(loader):
    return {'some_extra_var': 'value'}

def mock_fact_cache():
    raise AnsibleError("Bad cache plugin")

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.utils.display.Display.warning')

@pytest.fixture
def mock_fact_cache_plugin(mocker):
    mocker.patch('ansible.vars.manager.FactCache', side_effect=mock_fact_cache)

@pytest.fixture
def variable_manager(mocker):
    mocker.patch('ansible.vars.manager.load_options_vars', side_effect=mock_load_options_vars)
    mocker.patch('ansible.vars.manager.load_extra_vars', side_effect=mock_load_extra_vars)
    return VariableManager()

def test_variable_manager_with_bad_fact_cache_plugin(mock_display, mock_fact_cache_plugin, variable_manager):
    assert isinstance(variable_manager._fact_cache, dict), "Fact cache should fallback to a dict"
    mock_display.assert_called_once()  # Ensure that the warning was displayed exactly once
