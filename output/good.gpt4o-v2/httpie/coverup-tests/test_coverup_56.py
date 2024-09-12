# file: httpie/cli/definition.py:520-527
# asked: {"lines": [520, 523, 524, 526, 527], "branches": []}
# gained: {"lines": [520, 523, 524, 526, 527], "branches": []}

import pytest
from httpie.cli.definition import _AuthTypeLazyChoices
from httpie.plugins.registry import plugin_manager

class MockPluginManager:
    def __init__(self, auth_plugins):
        self.auth_plugins = auth_plugins

    def get_auth_plugin_mapping(self):
        return self.auth_plugins

@pytest.fixture
def mock_plugin_manager(monkeypatch):
    auth_plugins = {
        'basic': 'BasicAuthPlugin',
        'digest': 'DigestAuthPlugin'
    }
    mock_manager = MockPluginManager(auth_plugins)
    monkeypatch.setattr('httpie.plugins.registry.plugin_manager', mock_manager)
    return mock_manager

def test_auth_type_lazy_choices_contains(mock_plugin_manager):
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'digest' in choices
    assert 'unknown' not in choices

def test_auth_type_lazy_choices_iter(mock_plugin_manager):
    choices = _AuthTypeLazyChoices()
    plugins = list(choices)
    assert plugins == ['basic', 'digest']
