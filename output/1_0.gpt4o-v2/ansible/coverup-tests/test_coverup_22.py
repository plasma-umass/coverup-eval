# file: lib/ansible/plugins/lookup/env.py:52-60
# asked: {"lines": [52, 53, 54, 56, 57, 58, 60], "branches": [[56, 57], [56, 60]]}
# gained: {"lines": [52, 53, 54, 56, 57, 58, 60], "branches": [[56, 57], [56, 60]]}

import os
import pytest
from ansible.plugins.lookup.env import LookupModule
from ansible.utils import py3compat

@pytest.fixture
def setup_env(monkeypatch):
    # Setup environment variables for the test
    monkeypatch.setattr(py3compat.environ, 'get', lambda key, default='': os.environ.get(key, default))
    os.environ['TEST_VAR'] = 'test_value'
    yield
    # Cleanup environment variables after the test
    del os.environ['TEST_VAR']

def test_lookup_module_run(setup_env):
    lookup = LookupModule()
    terms = ['TEST_VAR']
    variables = {}
    result = lookup.run(terms, variables)
    assert result == ['test_value']

def test_lookup_module_run_with_default(setup_env):
    lookup = LookupModule()
    terms = ['NON_EXISTENT_VAR']
    variables = {}
    result = lookup.run(terms, variables)
    assert result == ['']
