# file lib/ansible/module_utils/common/parameters.py:793-799
# lines [796, 797, 798, 799]
# branches ['796->797', '796->799', '797->796', '797->798']

import os
import pytest
from ansible.module_utils.common.parameters import env_fallback, AnsibleFallbackNotFound

def test_env_fallback(mocker):
    # Mocking os.environ to control the environment variables
    mock_environ = mocker.patch.dict(os.environ, {"TEST_VAR": "test_value"}, clear=True)
    
    # Test case where the environment variable is found
    assert env_fallback("TEST_VAR") == "test_value"
    
    # Test case where the environment variable is not found
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback("NON_EXISTENT_VAR")
    
    # Clean up the mock
    mock_environ.clear()
