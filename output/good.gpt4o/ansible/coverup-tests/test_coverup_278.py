# file lib/ansible/playbook/base.py:507-516
# lines [507, 508, 509, 510, 512, 513, 514, 515, 516]
# branches ['509->510', '509->512', '512->513', '512->514', '514->515', '514->516']

import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError

@pytest.fixture
def mock_action_loader(mocker):
    return mocker.patch('ansible.playbook.base.action_loader')

@pytest.fixture
def mock_module_loader(mocker):
    return mocker.patch('ansible.playbook.base.module_loader')

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.playbook.base.display')

def test_resolve_action_success(mock_action_loader, mock_module_loader):
    mock_context = MagicMock()
    mock_context.resolved = True
    mock_context.resolved_fqcn = 'resolved_fqcn'
    mock_action_loader.find_plugin_with_context.return_value = mock_context

    field_attr_base = FieldAttributeBase()
    result = field_attr_base._resolve_action('test_action')
    assert result == 'resolved_fqcn'

def test_resolve_action_fallback_success(mock_action_loader, mock_module_loader):
    mock_action_loader.find_plugin_with_context.return_value.resolved = False
    mock_context = MagicMock()
    mock_context.resolved = True
    mock_context.resolved_fqcn = 'resolved_fqcn'
    mock_module_loader.find_plugin_with_context.return_value = mock_context

    field_attr_base = FieldAttributeBase()
    result = field_attr_base._resolve_action('test_action')
    assert result == 'resolved_fqcn'

def test_resolve_action_failure_mandatory(mock_action_loader, mock_module_loader):
    mock_action_loader.find_plugin_with_context.return_value.resolved = False
    mock_module_loader.find_plugin_with_context.return_value.resolved = False

    field_attr_base = FieldAttributeBase()
    with pytest.raises(AnsibleParserError, match="Could not resolve action test_action in module_defaults"):
        field_attr_base._resolve_action('test_action')

def test_resolve_action_failure_non_mandatory(mock_action_loader, mock_module_loader, mock_display):
    mock_action_loader.find_plugin_with_context.return_value.resolved = False
    mock_module_loader.find_plugin_with_context.return_value.resolved = False

    field_attr_base = FieldAttributeBase()
    result = field_attr_base._resolve_action('test_action', mandatory=False)
    assert result is None
    mock_display.vvvvv.assert_called_once_with("Could not resolve action test_action in module_defaults")
