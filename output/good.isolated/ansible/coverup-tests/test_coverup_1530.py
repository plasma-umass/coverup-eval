# file lib/ansible/galaxy/api.py:145-177
# lines [148, 150, 151, 152, 153, 155, 156, 157, 158, 159, 161, 162, 164, 165, 166, 167, 169, 170, 171, 174, 175, 177]
# branches ['150->151', '150->155', '156->157', '156->161', '169->170', '169->177']

import json
import os
import pytest
import stat
from ansible.galaxy.api import _load_cache
from ansible.utils.display import Display

# Mock the Display class to capture output
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'vvvv', autospec=True)

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch.object(Display, 'warning', autospec=True)

@pytest.fixture
def cache_file(tmp_path):
    cache_path = tmp_path / "galaxy_cache.json"
    yield cache_path
    if cache_path.exists():
        cache_path.unlink()

def test_load_cache_new_file(mock_display, cache_file):
    assert not cache_file.exists()
    cache = _load_cache(str(cache_file).encode('utf-8'))
    assert cache_file.exists()
    assert cache == {'version': 1}
    mock_display.assert_called()

def test_load_cache_world_writable(mock_display_warning, cache_file):
    cache_file.touch()
    cache_file.chmod(0o666)  # Make the file world writable
    cache = _load_cache(str(cache_file).encode('utf-8'))
    assert cache is None
    mock_display_warning.assert_called_once()

def test_load_cache_invalid_json(cache_file):
    cache_file.write_text(u'invalid json')
    cache = _load_cache(str(cache_file).encode('utf-8'))
    assert cache == {'version': 1}

def test_load_cache_invalid_version(mock_display, cache_file):
    cache_file.write_text(json.dumps({'version': 999}))
    cache = _load_cache(str(cache_file).encode('utf-8'))
    assert cache == {'version': 1}
    mock_display.assert_called()

def test_load_cache_valid_cache(cache_file):
    valid_cache = {'version': 1, 'data': 'test'}
    cache_file.write_text(json.dumps(valid_cache))
    cache = _load_cache(str(cache_file).encode('utf-8'))
    assert cache == valid_cache
