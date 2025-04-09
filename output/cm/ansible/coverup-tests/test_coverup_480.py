# file lib/ansible/config/manager.py:306-314
# lines [306, 309, 310, 311, 312, 313, 314]
# branches ['310->311', '310->313']

import os
import pytest
from ansible.errors import AnsibleError
from ansible.config.manager import ConfigManager
from ansible.module_utils._text import to_bytes, to_native

# Mocking yaml_load since the original import failed
def yaml_load(stream):
    import yaml
    return yaml.safe_load(stream)

@pytest.fixture
def config_manager():
    return ConfigManager()

@pytest.fixture
def temp_yaml_file(tmp_path):
    file = tmp_path / "temp_config.yml"
    file.write_text("example: value")
    return str(file)

@pytest.fixture
def cleanup():
    # Fixture to clean up any created files or other resources after tests
    yield
    # Here you would add any cleanup logic that is needed after the tests run
    # For this example, there is no persistent state to clean up

def test_read_config_yaml_file_exists(config_manager, temp_yaml_file, cleanup):
    # Test that the method reads an existing YAML file correctly
    result = config_manager._read_config_yaml_file(temp_yaml_file)
    assert result == {'example': 'value'}

def test_read_config_yaml_file_missing(config_manager, cleanup):
    # Test that the method raises an AnsibleError when the file is missing
    with pytest.raises(AnsibleError) as excinfo:
        config_manager._read_config_yaml_file('/path/to/nonexistent/file.yml')
    assert "Missing base YAML definition file" in str(excinfo.value)
