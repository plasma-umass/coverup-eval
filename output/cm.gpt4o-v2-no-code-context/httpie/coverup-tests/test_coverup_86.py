# file: httpie/cli/definition.py:520-527
# asked: {"lines": [524, 527], "branches": []}
# gained: {"lines": [524, 527], "branches": []}

import pytest
from unittest.mock import MagicMock

# Assuming plugin_manager is a global or imported object in the module
# where _AuthTypeLazyChoices is defined.
import httpie.cli.definition as definition

@pytest.fixture
def mock_plugin_manager(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr(definition, 'plugin_manager', mock)
    return mock

def test_auth_type_lazy_choices_contains(mock_plugin_manager):
    mock_plugin_manager.get_auth_plugin_mapping.return_value = {'basic': 'BasicAuthPlugin'}
    auth_choices = definition._AuthTypeLazyChoices()
    
    assert 'basic' in auth_choices
    assert 'digest' not in auth_choices

def test_auth_type_lazy_choices_iter(mock_plugin_manager):
    mock_plugin_manager.get_auth_plugin_mapping.return_value = {'basic': 'BasicAuthPlugin', 'digest': 'DigestAuthPlugin'}
    auth_choices = definition._AuthTypeLazyChoices()
    
    assert list(auth_choices) == ['basic', 'digest']
