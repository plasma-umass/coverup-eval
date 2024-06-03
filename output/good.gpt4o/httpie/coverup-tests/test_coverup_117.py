# file httpie/config.py:99-121
# lines []
# branches ['103->106', '106->109']

import pytest
from unittest.mock import MagicMock, patch
import json
from httpie.config import BaseConfigDict

@pytest.fixture
def config_dict():
    config = BaseConfigDict(path=MagicMock())
    config.helpurl = "http://example.com/help"
    config.about = "About information"
    config.ensure_directory = MagicMock()
    return config

def test_save_with_helpurl_and_about(config_dict):
    with patch('httpie.config.__version__', '1.0.0'):
        config_dict.save()
        
        assert '__meta__' in config_dict
        assert config_dict['__meta__']['httpie'] == '1.0.0'
        assert config_dict['__meta__']['help'] == "http://example.com/help"
        assert config_dict['__meta__']['about'] == "About information"
        config_dict.ensure_directory.assert_called_once()
        config_dict.path.write_text.assert_called_once()
        
        json_string = json.dumps(
            obj=config_dict,
            indent=4,
            sort_keys=True,
            ensure_ascii=True,
        )
        config_dict.path.write_text.assert_called_with(json_string + '\n')

def test_save_without_helpurl_and_about():
    config = BaseConfigDict(path=MagicMock())
    config.helpurl = None
    config.about = None
    config.ensure_directory = MagicMock()

    with patch('httpie.config.__version__', '1.0.0'):
        config.save()
        
        assert '__meta__' in config
        assert config['__meta__']['httpie'] == '1.0.0'
        assert 'help' not in config['__meta__']
        assert 'about' not in config['__meta__']
        config.ensure_directory.assert_called_once()
        config.path.write_text.assert_called_once()
        
        json_string = json.dumps(
            obj=config,
            indent=4,
            sort_keys=True,
            ensure_ascii=True,
        )
        config.path.write_text.assert_called_with(json_string + '\n')
