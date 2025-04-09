# file: lib/ansible/playbook/base.py:507-516
# asked: {"lines": [507, 508, 509, 510, 512, 513, 514, 515, 516], "branches": [[509, 510], [509, 512], [512, 513], [512, 514], [514, 515], [514, 516]]}
# gained: {"lines": [507, 508, 509, 510, 512, 513, 514, 515, 516], "branches": [[509, 510], [509, 512], [512, 513], [512, 514], [514, 515], [514, 516]]}

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.base import FieldAttributeBase, AnsibleParserError

@pytest.fixture
def mock_action_loader():
    with patch('ansible.playbook.base.action_loader') as mock_loader:
        yield mock_loader

@pytest.fixture
def mock_module_loader():
    with patch('ansible.playbook.base.module_loader') as mock_loader:
        yield mock_loader

@pytest.fixture
def mock_display():
    with patch('ansible.playbook.base.display') as mock_display:
        yield mock_display

def test_resolve_action_success_action_loader(mock_action_loader, mock_module_loader):
    mock_context = Mock()
    mock_context.resolved = True
    mock_context.resolved_fqcn = 'resolved_fqcn'
    mock_action_loader.find_plugin_with_context.return_value = mock_context

    field_attr_base = FieldAttributeBase()
    result = field_attr_base._resolve_action('test_action')

    assert result == 'resolved_fqcn'
    mock_action_loader.find_plugin_with_context.assert_called_once_with('test_action')
    mock_module_loader.find_plugin_with_context.assert_not_called()

def test_resolve_action_success_module_loader(mock_action_loader, mock_module_loader):
    mock_context_action = Mock()
    mock_context_action.resolved = False
    mock_action_loader.find_plugin_with_context.return_value = mock_context_action

    mock_context_module = Mock()
    mock_context_module.resolved = True
    mock_context_module.resolved_fqcn = 'resolved_fqcn'
    mock_module_loader.find_plugin_with_context.return_value = mock_context_module

    field_attr_base = FieldAttributeBase()
    result = field_attr_base._resolve_action('test_action')

    assert result == 'resolved_fqcn'
    mock_action_loader.find_plugin_with_context.assert_called_once_with('test_action')
    mock_module_loader.find_plugin_with_context.assert_called_once_with('test_action')

def test_resolve_action_failure_mandatory(mock_action_loader, mock_module_loader):
    mock_context_action = Mock()
    mock_context_action.resolved = False
    mock_action_loader.find_plugin_with_context.return_value = mock_context_action

    mock_context_module = Mock()
    mock_context_module.resolved = False
    mock_module_loader.find_plugin_with_context.return_value = mock_context_module

    field_attr_base = FieldAttributeBase()
    with pytest.raises(AnsibleParserError, match="Could not resolve action test_action in module_defaults"):
        field_attr_base._resolve_action('test_action')

    mock_action_loader.find_plugin_with_context.assert_called_once_with('test_action')
    mock_module_loader.find_plugin_with_context.assert_called_once_with('test_action')

def test_resolve_action_failure_non_mandatory(mock_action_loader, mock_module_loader, mock_display):
    mock_context_action = Mock()
    mock_context_action.resolved = False
    mock_action_loader.find_plugin_with_context.return_value = mock_context_action

    mock_context_module = Mock()
    mock_context_module.resolved = False
    mock_module_loader.find_plugin_with_context.return_value = mock_context_module

    field_attr_base = FieldAttributeBase()
    result = field_attr_base._resolve_action('test_action', mandatory=False)

    assert result is None
    mock_action_loader.find_plugin_with_context.assert_called_once_with('test_action')
    mock_module_loader.find_plugin_with_context.assert_called_once_with('test_action')
    mock_display.vvvvv.assert_called_once_with("Could not resolve action test_action in module_defaults")
