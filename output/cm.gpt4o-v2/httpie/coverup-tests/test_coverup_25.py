# file: httpie/config.py:99-121
# asked: {"lines": [99, 100, 101, 103, 104, 106, 107, 109, 111, 112, 113, 114, 115, 117, 118, 119, 120, 121], "branches": [[103, 104], [103, 106], [106, 107], [106, 109], [120, 0], [120, 121]]}
# gained: {"lines": [99, 100, 101, 103, 104, 106, 107, 109, 111, 112, 113, 114, 115, 117, 118, 119, 120, 121], "branches": [[103, 104], [106, 107], [120, 0], [120, 121]]}

import pytest
import json
from unittest.mock import MagicMock, patch
from pathlib import Path
from httpie.config import BaseConfigDict
from httpie import __version__

class TestBaseConfigDict:
    
    @pytest.fixture
    def config_dict(self, tmp_path):
        config = BaseConfigDict(path=tmp_path / "config.json")
        config.helpurl = "http://example.com/help"
        config.about = "About information"
        config.ensure_directory = MagicMock()
        return config

    @patch("pathlib.Path.write_text")
    def test_save_success(self, mock_write_text, config_dict):
        config_dict.save()
        
        config_dict.ensure_directory.assert_called_once()
        mock_write_text.assert_called_once()
        
        saved_data = json.loads(mock_write_text.call_args[0][0])
        assert saved_data['__meta__']['httpie'] == __version__
        assert saved_data['__meta__']['help'] == "http://example.com/help"
        assert saved_data['__meta__']['about'] == "About information"

    @patch("pathlib.Path.write_text", side_effect=IOError)
    def test_save_ioerror(self, mock_write_text, config_dict):
        with pytest.raises(IOError):
            config_dict.save(fail_silently=False)
        
        config_dict.ensure_directory.assert_called_once()
        mock_write_text.assert_called_once()

    @patch("pathlib.Path.write_text", side_effect=IOError)
    def test_save_ioerror_silent(self, mock_write_text, config_dict):
        config_dict.save(fail_silently=True)
        
        config_dict.ensure_directory.assert_called_once()
        mock_write_text.assert_called_once()
