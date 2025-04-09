# file semantic_release/settings.py:97-118
# lines [97, 103, 104, 106, 107, 109, 110, 112, 113, 114, 115, 118]
# branches ['106->107', '106->118']

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.settings import current_changelog_components, ImproperConfigurationError

@pytest.fixture
def mock_config(mocker):
    return mocker.patch('semantic_release.settings.config')

@pytest.fixture
def mock_importlib(mocker):
    return mocker.patch('semantic_release.settings.importlib')

def test_current_changelog_components_success(mock_config, mock_importlib):
    mock_config.get.return_value = "module1.func1,module2.func2"
    mock_importlib.import_module.side_effect = [MagicMock(func1=lambda: None), MagicMock(func2=lambda: None)]
    
    components = current_changelog_components()
    
    assert len(components) == 2
    assert callable(components[0])
    assert callable(components[1])

def test_current_changelog_components_import_error(mock_config, mock_importlib):
    mock_config.get.return_value = "module1.func1,module2.func2"
    mock_importlib.import_module.side_effect = ImportError
    
    with pytest.raises(ImproperConfigurationError):
        current_changelog_components()

def test_current_changelog_components_attribute_error(mock_config, mock_importlib):
    mock_config.get.return_value = "module1.func1,module2.func2"
    mock_importlib.import_module.side_effect = [MagicMock(), MagicMock()]
    
    def mock_getattr(module, name):
        if name == "func1":
            raise AttributeError
        return lambda: None
    
    with patch('semantic_release.settings.getattr', side_effect=mock_getattr):
        with pytest.raises(ImproperConfigurationError):
            current_changelog_components()
