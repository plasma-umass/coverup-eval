# file lib/ansible/module_utils/common/parameters.py:793-799
# lines [793, 796, 797, 798, 799]
# branches ['796->797', '796->799', '797->796', '797->798']

import os
import pytest
from ansible.module_utils.common.parameters import AnsibleFallbackNotFound

def env_fallback(*args, **kwargs):
    """Load value from environment variable"""
    for arg in args:
        if arg in os.environ:
            return os.environ[arg]
    raise AnsibleFallbackNotFound

def test_env_fallback_found(mocker):
    mocker.patch.dict(os.environ, {'TEST_VAR': 'test_value'})
    assert env_fallback('TEST_VAR') == 'test_value'

def test_env_fallback_not_found(mocker):
    mocker.patch.dict(os.environ, {}, clear=True)
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('NON_EXISTENT_VAR')
