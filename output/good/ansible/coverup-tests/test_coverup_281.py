# file lib/ansible/playbook/base.py:507-516
# lines [507, 508, 509, 510, 512, 513, 514, 515, 516]
# branches ['509->510', '509->512', '512->513', '512->514', '514->515', '514->516']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.base import FieldAttributeBase
from ansible.plugins.loader import action_loader, module_loader
from unittest.mock import MagicMock
from ansible.utils.display import Display

# Mock the action_loader and module_loader to control their behavior
@pytest.fixture
def mock_loaders(mocker):
    mocker.patch.object(action_loader, 'find_plugin_with_context', return_value=MagicMock(resolved=False))
    mocker.patch.object(module_loader, 'find_plugin_with_context', return_value=MagicMock(resolved=False))

def test_resolve_action_raises_error_when_mandatory_and_not_resolved(mock_loaders):
    base = FieldAttributeBase()
    with pytest.raises(AnsibleParserError):
        base._resolve_action('nonexistent_action')

def test_resolve_action_returns_none_when_not_mandatory_and_not_resolved(mock_loaders, mocker):
    base = FieldAttributeBase()
    mock_display_vvvvv = mocker.patch.object(Display, 'vvvvv')
    result = base._resolve_action('nonexistent_action', mandatory=False)
    assert result is None
    mock_display_vvvvv.assert_called_once_with("Could not resolve action nonexistent_action in module_defaults")

def test_resolve_action_returns_fqcn_when_resolved_by_action_loader(mocker):
    mock_context = MagicMock(resolved=True, resolved_fqcn='resolved.action.fqcn')
    mocker.patch.object(action_loader, 'find_plugin_with_context', return_value=mock_context)
    base = FieldAttributeBase()
    result = base._resolve_action('existent_action')
    assert result == 'resolved.action.fqcn'

def test_resolve_action_returns_fqcn_when_resolved_by_module_loader(mocker):
    mock_context_action = MagicMock(resolved=False)
    mock_context_module = MagicMock(resolved=True, resolved_fqcn='resolved.module.fqcn')
    mocker.patch.object(action_loader, 'find_plugin_with_context', return_value=mock_context_action)
    mocker.patch.object(module_loader, 'find_plugin_with_context', return_value=mock_context_module)
    base = FieldAttributeBase()
    result = base._resolve_action('existent_module')
    assert result == 'resolved.module.fqcn'
