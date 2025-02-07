# file: lib/ansible/plugins/inventory/toml.py:226-247
# asked: {"lines": [226, 228, 229, 230, 233, 234, 236, 237, 238, 239, 241, 242, 243, 244, 246, 247], "branches": [[228, 229], [228, 233], [241, 242], [241, 243], [243, 244], [243, 246], [246, 0], [246, 247]]}
# gained: {"lines": [226, 228, 229, 230, 233, 234, 236, 237, 238, 239, 241, 242, 243, 244, 246, 247], "branches": [[228, 229], [228, 233], [241, 242], [241, 243], [243, 244], [243, 246], [246, 0], [246, 247]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.toml import InventoryModule
from unittest.mock import MagicMock, patch

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module._load_name = 'toml'
    return module

def test_parse_no_toml_library(inventory_module, monkeypatch):
    monkeypatch.setattr('ansible.plugins.inventory.toml.HAS_TOML', False)
    with pytest.raises(AnsibleParserError, match='The TOML inventory plugin requires the python "toml" library'):
        inventory_module.parse(None, None, None)

def test_parse_load_file_exception(inventory_module, monkeypatch):
    monkeypatch.setattr('ansible.plugins.inventory.toml.HAS_TOML', True)
    inventory_module._load_file = MagicMock(side_effect=Exception('load file error'))
    with pytest.raises(AnsibleParserError, match='load file error'):
        inventory_module.parse(None, None, 'dummy_path')

def test_parse_empty_data(inventory_module, monkeypatch):
    monkeypatch.setattr('ansible.plugins.inventory.toml.HAS_TOML', True)
    inventory_module._load_file = MagicMock(return_value=None)
    with pytest.raises(AnsibleParserError, match='Parsed empty TOML file'):
        inventory_module.parse(None, None, 'dummy_path')

def test_parse_plugin_configuration_file(inventory_module, monkeypatch):
    monkeypatch.setattr('ansible.plugins.inventory.toml.HAS_TOML', True)
    inventory_module._load_file = MagicMock(return_value={'plugin': 'some_plugin'})
    with pytest.raises(AnsibleParserError, match='Plugin configuration TOML file, not TOML inventory'):
        inventory_module.parse(None, None, 'dummy_path')

def test_parse_valid_data(inventory_module, monkeypatch):
    monkeypatch.setattr('ansible.plugins.inventory.toml.HAS_TOML', True)
    data = {
        'group1': {
            'hosts': {
                'host1': None
            }
        }
    }
    inventory_module._load_file = MagicMock(return_value=data)
    inventory_module._parse_group = MagicMock()
    inventory_module.parse(None, None, 'dummy_path')
    inventory_module._parse_group.assert_called_once_with('group1', data['group1'])
