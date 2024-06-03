# file httpie/cli/definition.py:520-527
# lines [524, 527]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the _AuthTypeLazyChoices class is imported from httpie.cli.definition
from httpie.cli.definition import _AuthTypeLazyChoices

@pytest.fixture
def mock_plugin_manager(mocker):
    mock = mocker.patch('httpie.cli.definition.plugin_manager')
    mock.get_auth_plugin_mapping.return_value = {
        'basic': 'BasicAuthPlugin',
        'digest': 'DigestAuthPlugin'
    }
    return mock

def test_auth_type_lazy_choices_contains(mock_plugin_manager):
    auth_choices = _AuthTypeLazyChoices()
    assert 'basic' in auth_choices
    assert 'digest' in auth_choices
    assert 'unknown' not in auth_choices

def test_auth_type_lazy_choices_iter(mock_plugin_manager):
    auth_choices = _AuthTypeLazyChoices()
    assert list(auth_choices) == ['basic', 'digest']
