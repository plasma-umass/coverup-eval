# file: semantic_release/settings.py:97-118
# asked: {"lines": [97, 103, 104, 106, 107, 109, 110, 112, 113, 114, 115, 118], "branches": [[106, 107], [106, 118]]}
# gained: {"lines": [97, 103, 104, 106, 107, 109, 110, 112, 113, 114, 115, 118], "branches": [[106, 107], [106, 118]]}

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.settings import current_changelog_components, ImproperConfigurationError

@pytest.fixture
def mock_config(monkeypatch):
    config = {
        "changelog_components": "module1.func1,module2.func2"
    }
    monkeypatch.setattr('semantic_release.settings.config', config)
    return config

def test_current_changelog_components_success(mock_config):
    with patch('importlib.import_module') as mock_import_module:
        mock_func1 = MagicMock()
        mock_func2 = MagicMock()
        mock_module1 = MagicMock()
        mock_module2 = MagicMock()
        mock_module1.func1 = mock_func1
        mock_module2.func2 = mock_func2
        mock_import_module.side_effect = [mock_module1, mock_module2]
        
        components = current_changelog_components()
        
        assert len(components) == 2
        assert components[0] == mock_func1
        assert components[1] == mock_func2

def test_current_changelog_components_import_error(mock_config):
    with patch('importlib.import_module', side_effect=ImportError):
        with pytest.raises(ImproperConfigurationError) as excinfo:
            current_changelog_components()
        assert 'Unable to import changelog component "module1.func1"' in str(excinfo.value)

def test_current_changelog_components_attribute_error(mock_config):
    with patch('importlib.import_module') as mock_import_module:
        mock_module1 = MagicMock()
        del mock_module1.func1  # Ensure func1 does not exist
        mock_import_module.side_effect = [mock_module1, MagicMock()]
        
        with pytest.raises(ImproperConfigurationError) as excinfo:
            current_changelog_components()
        assert 'Unable to import changelog component "module1.func1"' in str(excinfo.value)
