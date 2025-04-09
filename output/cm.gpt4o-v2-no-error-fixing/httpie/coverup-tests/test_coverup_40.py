# file: httpie/cli/definition.py:520-527
# asked: {"lines": [520, 523, 524, 526, 527], "branches": []}
# gained: {"lines": [520, 523, 524, 526, 527], "branches": []}

import pytest
from httpie.plugins.registry import plugin_manager
from httpie.cli.definition import _AuthTypeLazyChoices

@pytest.fixture
def mock_plugin_manager(mocker):
    mock = mocker.patch('httpie.plugins.registry.plugin_manager')
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
    choices = list(auth_choices)
    assert choices == ['basic', 'digest']
