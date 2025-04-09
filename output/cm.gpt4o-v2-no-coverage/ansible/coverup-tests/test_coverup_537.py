# file: lib/ansible/module_utils/common/parameters.py:793-799
# asked: {"lines": [793, 796, 797, 798, 799], "branches": [[796, 797], [796, 799], [797, 796], [797, 798]]}
# gained: {"lines": [793, 796, 797, 798, 799], "branches": [[796, 797], [796, 799], [797, 796], [797, 798]]}

import os
import pytest
from ansible.module_utils.errors import AnsibleFallbackNotFound
from ansible.module_utils.common.parameters import env_fallback

def test_env_fallback_found(monkeypatch):
    # Setup
    monkeypatch.setenv('TEST_ENV_VAR', 'test_value')
    
    # Test
    result = env_fallback('TEST_ENV_VAR')
    
    # Assert
    assert result == 'test_value'
    
    # Cleanup
    monkeypatch.delenv('TEST_ENV_VAR', raising=False)

def test_env_fallback_not_found():
    # Test and Assert
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('NON_EXISTENT_ENV_VAR')
