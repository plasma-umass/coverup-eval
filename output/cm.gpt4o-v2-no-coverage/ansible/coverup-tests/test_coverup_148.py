# file: lib/ansible/plugins/inventory/toml.py:226-247
# asked: {"lines": [226, 228, 229, 230, 233, 234, 236, 237, 238, 239, 241, 242, 243, 244, 246, 247], "branches": [[228, 229], [228, 233], [241, 242], [241, 243], [243, 244], [243, 246], [246, 0], [246, 247]]}
# gained: {"lines": [226, 228, 229, 230, 233, 234, 236, 237, 238, 239, 241, 242, 243, 244, 246, 247], "branches": [[228, 229], [228, 233], [241, 242], [241, 243], [243, 244], [243, 246], [246, 0], [246, 247]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.toml import InventoryModule

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_parse_no_toml_library(inventory_module):
    with patch('ansible.plugins.inventory.toml.HAS_TOML', False):
        with pytest.raises(AnsibleParserError, match='The TOML inventory plugin requires the python "toml" library'):
            inventory_module.parse(None, None, None)

def test_parse_load_file_exception(inventory_module):
    with patch('ansible.plugins.inventory.toml.HAS_TOML', True), \
         patch.object(InventoryModule, 'set_options'), \
         patch.object(InventoryModule, '_load_file', side_effect=Exception('load error')):
        with pytest.raises(AnsibleParserError, match='load error'):
            inventory_module.parse(None, None, 'dummy_path')

def test_parse_empty_toml_file(inventory_module):
    with patch('ansible.plugins.inventory.toml.HAS_TOML', True), \
         patch.object(InventoryModule, 'set_options'), \
         patch.object(InventoryModule, '_load_file', return_value=None):
        with pytest.raises(AnsibleParserError, match='Parsed empty TOML file'):
            inventory_module.parse(None, None, 'dummy_path')

def test_parse_plugin_configuration_toml_file(inventory_module):
    with patch('ansible.plugins.inventory.toml.HAS_TOML', True), \
         patch.object(InventoryModule, 'set_options'), \
         patch.object(InventoryModule, '_load_file', return_value={'plugin': 'some_plugin'}):
        with pytest.raises(AnsibleParserError, match='Plugin configuration TOML file, not TOML inventory'):
            inventory_module.parse(None, None, 'dummy_path')

def test_parse_valid_toml_file(inventory_module):
    with patch('ansible.plugins.inventory.toml.HAS_TOML', True), \
         patch.object(InventoryModule, 'set_options'), \
         patch.object(InventoryModule, '_load_file', return_value={'group1': {}}), \
         patch.object(InventoryModule, '_parse_group') as mock_parse_group:
        inventory_module.parse(None, None, 'dummy_path')
        mock_parse_group.assert_called_once_with('group1', {})
