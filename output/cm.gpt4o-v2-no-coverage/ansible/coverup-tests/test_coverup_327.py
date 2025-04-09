# file: lib/ansible/playbook/base.py:507-516
# asked: {"lines": [507, 508, 509, 510, 512, 513, 514, 515, 516], "branches": [[509, 510], [509, 512], [512, 513], [512, 514], [514, 515], [514, 516]]}
# gained: {"lines": [507, 508, 509, 510, 512, 513, 514, 515, 516], "branches": [[509, 510], [509, 512], [512, 513], [512, 514], [514, 515], [514, 516]]}

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError
from ansible.plugins.loader import module_loader, action_loader
from unittest.mock import patch, MagicMock

class TestFieldAttributeBase:

    @patch('ansible.plugins.loader.action_loader.find_plugin_with_context')
    @patch('ansible.plugins.loader.module_loader.find_plugin_with_context')
    def test_resolve_action_success_action_loader(self, mock_module_loader, mock_action_loader):
        instance = FieldAttributeBase()
        mock_action_loader.return_value.resolved = True
        mock_action_loader.return_value.resolved_fqcn = 'resolved.action'

        result = instance._resolve_action('test_action')

        assert result == 'resolved.action'
        mock_action_loader.assert_called_once_with('test_action')
        mock_module_loader.assert_not_called()

    @patch('ansible.plugins.loader.action_loader.find_plugin_with_context')
    @patch('ansible.plugins.loader.module_loader.find_plugin_with_context')
    def test_resolve_action_success_module_loader(self, mock_module_loader, mock_action_loader):
        instance = FieldAttributeBase()
        mock_action_loader.return_value.resolved = False
        mock_module_loader.return_value.resolved = True
        mock_module_loader.return_value.resolved_fqcn = 'resolved.module'

        result = instance._resolve_action('test_action')

        assert result == 'resolved.module'
        mock_action_loader.assert_called_once_with('test_action')
        mock_module_loader.assert_called_once_with('test_action')

    @patch('ansible.plugins.loader.action_loader.find_plugin_with_context')
    @patch('ansible.plugins.loader.module_loader.find_plugin_with_context')
    def test_resolve_action_failure_mandatory(self, mock_module_loader, mock_action_loader):
        instance = FieldAttributeBase()
        mock_action_loader.return_value.resolved = False
        mock_module_loader.return_value.resolved = False

        with pytest.raises(AnsibleParserError, match="Could not resolve action test_action in module_defaults"):
            instance._resolve_action('test_action')

        mock_action_loader.assert_called_once_with('test_action')
        mock_module_loader.assert_called_once_with('test_action')

    @patch('ansible.plugins.loader.action_loader.find_plugin_with_context')
    @patch('ansible.plugins.loader.module_loader.find_plugin_with_context')
    @patch('ansible.utils.display.Display.vvvvv')
    def test_resolve_action_failure_non_mandatory(self, mock_display, mock_module_loader, mock_action_loader):
        instance = FieldAttributeBase()
        mock_action_loader.return_value.resolved = False
        mock_module_loader.return_value.resolved = False

        result = instance._resolve_action('test_action', mandatory=False)

        assert result is None
        mock_action_loader.assert_called_once_with('test_action')
        mock_module_loader.assert_called_once_with('test_action')
        mock_display.assert_called_once_with("Could not resolve action test_action in module_defaults")
