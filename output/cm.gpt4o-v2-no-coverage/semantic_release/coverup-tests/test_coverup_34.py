# file: semantic_release/settings.py:97-118
# asked: {"lines": [97, 103, 104, 106, 107, 109, 110, 112, 113, 114, 115, 118], "branches": [[106, 107], [106, 118]]}
# gained: {"lines": [97, 103, 104, 106, 107, 109, 110, 112, 113, 114, 115, 118], "branches": [[106, 107], [106, 118]]}

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.settings import current_changelog_components
from semantic_release.errors import ImproperConfigurationError

@pytest.fixture
def mock_config(monkeypatch):
    config = MagicMock()
    monkeypatch.setattr('semantic_release.settings.config', config)
    return config

def test_current_changelog_components_success(mock_config):
    mock_config.get.return_value = 'module1.func1,module2.func2'
    
    with patch('importlib.import_module') as mock_import_module:
        mock_module1 = MagicMock()
        mock_module1.func1 = lambda: "func1"
        mock_module2 = MagicMock()
        mock_module2.func2 = lambda: "func2"
        mock_import_module.side_effect = [mock_module1, mock_module2]
        
        components = current_changelog_components()
        
        assert len(components) == 2
        assert callable(components[0])
        assert callable(components[1])

def test_current_changelog_components_import_error(mock_config):
    mock_config.get.return_value = 'nonexistent.module.func'
    
    with patch('importlib.import_module', side_effect=ImportError):
        with pytest.raises(ImproperConfigurationError) as excinfo:
            current_changelog_components()
        assert 'Unable to import changelog component "nonexistent.module.func"' in str(excinfo.value)

def test_current_changelog_components_attribute_error(mock_config):
    mock_config.get.return_value = 'module.nonexistent_func'
    
    mock_module = MagicMock()
    del mock_module.nonexistent_func
    
    with patch('importlib.import_module', return_value=mock_module):
        with pytest.raises(ImproperConfigurationError) as excinfo:
            current_changelog_components()
        assert 'Unable to import changelog component "module.nonexistent_func"' in str(excinfo.value)
