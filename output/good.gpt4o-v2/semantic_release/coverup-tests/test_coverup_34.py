# file: semantic_release/settings.py:97-118
# asked: {"lines": [97, 103, 104, 106, 107, 109, 110, 112, 113, 114, 115, 118], "branches": [[106, 107], [106, 118]]}
# gained: {"lines": [97, 103, 104, 106, 107, 109, 110, 112, 113, 114, 115, 118], "branches": [[106, 107], [106, 118]]}

import pytest
import importlib
from unittest.mock import patch, MagicMock
from semantic_release.settings import current_changelog_components, ImproperConfigurationError

@pytest.fixture
def mock_config(monkeypatch):
    config = MagicMock()
    monkeypatch.setattr('semantic_release.settings.config', config)
    return config

def test_current_changelog_components_success(mock_config):
    mock_config.get.return_value = 'os.path.basename,os.path.dirname'
    
    components = current_changelog_components()
    
    assert len(components) == 2
    assert components[0] == importlib.import_module('os.path').basename
    assert components[1] == importlib.import_module('os.path').dirname

def test_current_changelog_components_import_error(mock_config):
    mock_config.get.return_value = 'nonexistent.module.function'
    
    with pytest.raises(ImproperConfigurationError) as excinfo:
        current_changelog_components()
    
    assert 'Unable to import changelog component "nonexistent.module.function"' in str(excinfo.value)

def test_current_changelog_components_attribute_error(mock_config):
    mock_config.get.return_value = 'os.nonexistent_function'
    
    with pytest.raises(ImproperConfigurationError) as excinfo:
        current_changelog_components()
    
    assert 'Unable to import changelog component "os.nonexistent_function"' in str(excinfo.value)
