# file: httpie/cli/definition.py:520-527
# asked: {"lines": [520, 523, 524, 526, 527], "branches": []}
# gained: {"lines": [520, 523, 524, 526, 527], "branches": []}

import pytest
from httpie.plugins.registry import plugin_manager
from httpie.cli.definition import _AuthTypeLazyChoices

@pytest.fixture
def setup_plugin_manager(monkeypatch):
    class MockPluginManager:
        def get_auth_plugin_mapping(self):
            return {
                'basic': 'BasicAuthPlugin',
                'digest': 'DigestAuthPlugin'
            }
    
    monkeypatch.setattr('httpie.plugins.registry.plugin_manager', MockPluginManager())

def test_contains(setup_plugin_manager):
    auth_choices = _AuthTypeLazyChoices()
    assert 'basic' in auth_choices
    assert 'digest' in auth_choices
    assert 'unknown' not in auth_choices

def test_iter(setup_plugin_manager):
    auth_choices = _AuthTypeLazyChoices()
    auth_list = list(auth_choices)
    assert auth_list == ['basic', 'digest']
