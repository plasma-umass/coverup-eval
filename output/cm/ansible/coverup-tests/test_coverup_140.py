# file lib/ansible/plugins/inventory/toml.py:226-247
# lines [226, 228, 229, 230, 233, 234, 236, 237, 238, 239, 241, 242, 243, 244, 246, 247]
# branches ['228->229', '228->233', '241->242', '241->243', '243->244', '243->246', '246->exit', '246->247']

import pytest
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.toml import InventoryModule
from ansible.inventory.data import InventoryData
from ansible.parsing.dataloader import DataLoader
from unittest.mock import MagicMock

# Mocking the HAS_TOML constant to simulate the absence of the 'toml' library
@pytest.fixture
def mock_has_toml(mocker):
    mocker.patch('ansible.plugins.inventory.toml.HAS_TOML', False)

# Mocking the HAS_TOML constant to simulate the presence of the 'toml' library
@pytest.fixture
def mock_has_toml_true(mocker):
    mocker.patch('ansible.plugins.inventory.toml.HAS_TOML', True)

# Mocking the _load_file method to return an empty dictionary
@pytest.fixture
def mock_load_file_empty(mocker):
    mocker.patch.object(InventoryModule, '_load_file', return_value={})

# Mocking the _load_file method to return a dictionary with 'plugin' key
@pytest.fixture
def mock_load_file_plugin(mocker):
    mocker.patch.object(InventoryModule, '_load_file', return_value={'plugin': 'dummy'})

# Mocking the set_options method to avoid AttributeError
@pytest.fixture
def mock_set_options(mocker):
    mocker.patch.object(InventoryModule, 'set_options')

# Test when 'toml' library is not available
def test_parse_without_toml(mock_has_toml):
    inventory = InventoryData()
    loader = DataLoader()
    path = '/fake/path'

    with pytest.raises(AnsibleParserError) as excinfo:
        InventoryModule().parse(inventory, loader, path)
    assert 'The TOML inventory plugin requires the python "toml" library' in str(excinfo.value)

# Test when the TOML file is empty
def test_parse_empty_toml_file(mock_has_toml_true, mock_load_file_empty, mock_set_options):
    inventory = InventoryData()
    loader = DataLoader()
    path = '/fake/path'

    with pytest.raises(AnsibleParserError) as excinfo:
        InventoryModule().parse(inventory, loader, path)
    assert 'Parsed empty TOML file' in str(excinfo.value)

# Test when the TOML file is a plugin configuration file
def test_parse_plugin_configuration_toml_file(mock_has_toml_true, mock_load_file_plugin, mock_set_options):
    inventory = InventoryData()
    loader = DataLoader()
    path = '/fake/path'

    with pytest.raises(AnsibleParserError) as excinfo:
        InventoryModule().parse(inventory, loader, path)
    assert 'Plugin configuration TOML file, not TOML inventory' in str(excinfo.value)
