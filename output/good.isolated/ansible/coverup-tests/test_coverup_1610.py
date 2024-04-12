# file lib/ansible/module_utils/common/parameters.py:793-799
# lines [796, 797, 798, 799]
# branches ['796->797', '796->799', '797->796', '797->798']

import os
import pytest
from ansible.module_utils.common.parameters import env_fallback
from ansible.module_utils.errors import AnsibleFallbackNotFound

def test_env_fallback_found(mocker):
    mocker.patch.dict(os.environ, {'TEST_ENV_VAR': 'test_value'})
    assert env_fallback('TEST_ENV_VAR') == 'test_value'

def test_env_fallback_not_found(mocker):
    mocker.patch.dict(os.environ, {}, clear=True)
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('NON_EXISTENT_VAR')
