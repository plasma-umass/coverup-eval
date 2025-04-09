# file: lib/ansible/module_utils/common/parameters.py:793-799
# asked: {"lines": [793, 796, 797, 798, 799], "branches": [[796, 797], [796, 799], [797, 796], [797, 798]]}
# gained: {"lines": [793, 796, 797, 798, 799], "branches": [[796, 797], [796, 799], [797, 796], [797, 798]]}

import os
import pytest
from ansible.module_utils.common.parameters import env_fallback, AnsibleFallbackNotFound

def test_env_fallback_found(monkeypatch):
    # Setup the environment variable
    monkeypatch.setenv('TEST_ENV_VAR', 'test_value')
    
    # Call the function with the environment variable name
    result = env_fallback('TEST_ENV_VAR')
    
    # Assert the result is as expected
    assert result == 'test_value'
    
    # Cleanup
    monkeypatch.delenv('TEST_ENV_VAR', raising=False)

def test_env_fallback_not_found():
    # Ensure the environment variable is not set
    if 'NON_EXISTENT_ENV_VAR' in os.environ:
        del os.environ['NON_EXISTENT_ENV_VAR']
    
    # Call the function with a non-existent environment variable name and assert it raises the correct exception
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('NON_EXISTENT_ENV_VAR')
