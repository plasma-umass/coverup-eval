# file httpie/cli/definition.py:520-527
# lines [520, 523, 524, 526, 527]
# branches []

import pytest
from httpie.cli.definition import _AuthTypeLazyChoices

# Mock plugin_manager to control the behavior of get_auth_plugin_mapping
@pytest.fixture
def mock_plugin_manager(mocker):
    mock = mocker.patch('httpie.cli.definition.plugin_manager')
    mock.get_auth_plugin_mapping.return_value = {'basic': 'BasicAuthPlugin', 'digest': 'DigestAuthPlugin'}
    return mock

def test_auth_type_lazy_choices_contains(mock_plugin_manager):
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in auth_type_lazy_choices
    assert 'digest' in auth_type_lazy_choices
    assert 'nonexistent' not in auth_type_lazy_choices

def test_auth_type_lazy_choices_iter(mock_plugin_manager):
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert list(auth_type_lazy_choices) == sorted(['basic', 'digest'])
