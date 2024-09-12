# file: lib/ansible/playbook/base.py:507-516
# asked: {"lines": [508, 509, 510, 512, 513, 514, 515, 516], "branches": [[509, 510], [509, 512], [512, 513], [512, 514], [514, 515], [514, 516]]}
# gained: {"lines": [508, 509, 510, 512, 513, 514, 515, 516], "branches": [[509, 510], [509, 512], [512, 513], [512, 514], [514, 515], [514, 516]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.plugins.loader import module_loader, action_loader
from ansible.playbook.base import FieldAttributeBase

class MockContext:
    def __init__(self, resolved, resolved_fqcn=None):
        self.resolved = resolved
        self.resolved_fqcn = resolved_fqcn

@pytest.fixture
def mock_action_loader(mocker):
    return mocker.patch('ansible.plugins.loader.action_loader.find_plugin_with_context')

@pytest.fixture
def mock_module_loader(mocker):
    return mocker.patch('ansible.plugins.loader.module_loader.find_plugin_with_context')

@pytest.fixture
def mock_display_vvvvv(mocker):
    return mocker.patch('ansible.utils.display.Display.vvvvv')

def test_resolve_action_success_action_loader(mock_action_loader, mock_module_loader):
    mock_action_loader.return_value = MockContext(resolved=True, resolved_fqcn='action_fqcn')
    mock_module_loader.return_value = MockContext(resolved=False)

    base = FieldAttributeBase()
    result = base._resolve_action('test_action')
    assert result == 'action_fqcn'
    mock_action_loader.assert_called_once_with('test_action')
    mock_module_loader.assert_not_called()

def test_resolve_action_success_module_loader(mock_action_loader, mock_module_loader):
    mock_action_loader.return_value = MockContext(resolved=False)
    mock_module_loader.return_value = MockContext(resolved=True, resolved_fqcn='module_fqcn')

    base = FieldAttributeBase()
    result = base._resolve_action('test_action')
    assert result == 'module_fqcn'
    mock_action_loader.assert_called_once_with('test_action')
    mock_module_loader.assert_called_once_with('test_action')

def test_resolve_action_failure_mandatory(mock_action_loader, mock_module_loader):
    mock_action_loader.return_value = MockContext(resolved=False)
    mock_module_loader.return_value = MockContext(resolved=False)

    base = FieldAttributeBase()
    with pytest.raises(AnsibleParserError, match="Could not resolve action test_action in module_defaults"):
        base._resolve_action('test_action')
    mock_action_loader.assert_called_once_with('test_action')
    mock_module_loader.assert_called_once_with('test_action')

def test_resolve_action_failure_non_mandatory(mock_action_loader, mock_module_loader, mock_display_vvvvv):
    mock_action_loader.return_value = MockContext(resolved=False)
    mock_module_loader.return_value = MockContext(resolved=False)

    base = FieldAttributeBase()
    result = base._resolve_action('test_action', mandatory=False)
    assert result is None
    mock_action_loader.assert_called_once_with('test_action')
    mock_module_loader.assert_called_once_with('test_action')
    mock_display_vvvvv.assert_called_once_with("Could not resolve action test_action in module_defaults")
