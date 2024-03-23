# file httpie/config.py:99-121
# lines [99, 100, 101, 103, 104, 106, 107, 109, 111, 112, 113, 114, 115, 117, 118, 119, 120, 121]
# branches ['103->104', '103->106', '106->107', '106->109', '120->exit', '120->121']

import json
import pytest
from httpie.config import BaseConfigDict
from pathlib import Path
from unittest.mock import Mock

class TestableBaseConfigDict(BaseConfigDict):
    def __init__(self, *args, **kwargs):
        kwargs['path'] = Path('/tmp/test_config.json')
        super().__init__(*args, **kwargs)
        self.helpurl = 'http://example.com/help'
        self.about = 'Test About'

    def ensure_directory(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)

@pytest.fixture
def config_dict():
    return TestableBaseConfigDict()

def test_base_config_dict_save(config_dict, mocker):
    mocker.patch('httpie.config.__version__', new='1.0.0')
    config_dict.save()
    with open(config_dict.path) as f:
        data = json.load(f)
    assert data['__meta__']['httpie'] == '1.0.0'
    assert data['__meta__']['help'] == 'http://example.com/help'
    assert data['__meta__']['about'] == 'Test About'
    config_dict.path.unlink()

def test_base_config_dict_save_fail_silently(config_dict, mocker):
    mocker.patch('httpie.config.__version__', new='1.0.0')
    mocker.patch.object(Path, 'write_text', side_effect=IOError)
    with pytest.raises(IOError):
        config_dict.save(fail_silently=False)
    config_dict.save(fail_silently=True)
    if config_dict.path.exists():
        config_dict.path.unlink()
