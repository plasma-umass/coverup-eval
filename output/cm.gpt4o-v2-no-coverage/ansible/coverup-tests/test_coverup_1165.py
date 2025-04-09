# file: lib/ansible/plugins/cache/jsonfile.py:52-64
# asked: {"lines": [52, 53, 57, 59, 60, 62, 63, 64], "branches": []}
# gained: {"lines": [52, 53, 57, 59, 60, 62, 63, 64], "branches": []}

import pytest
import json
import os
import codecs
from unittest import mock
from ansible.plugins.cache.jsonfile import CacheModule
from ansible.parsing.ajson import AnsibleJSONEncoder, AnsibleJSONDecoder
from ansible.errors import AnsibleError

@pytest.fixture
def cache_module(tmp_path):
    with mock.patch('ansible.plugins.cache.BaseFileCacheModule._get_cache_connection', return_value=str(tmp_path)):
        with mock.patch('ansible.plugins.cache.BaseFileCacheModule.get_option', side_effect=lambda x: 86400 if x == '_timeout' else str(tmp_path)):
            return CacheModule()

def test_load(cache_module, tmp_path):
    test_data = {"key": "value"}
    test_file = tmp_path / "test.json"
    with codecs.open(test_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(test_data, cls=AnsibleJSONEncoder, sort_keys=True, indent=4))

    result = cache_module._load(test_file)
    assert result == test_data

def test_dump(cache_module, tmp_path):
    test_data = {"key": "value"}
    test_file = tmp_path / "test.json"

    cache_module._dump(test_data, test_file)

    with codecs.open(test_file, 'r', encoding='utf-8') as f:
        result = json.load(f, cls=AnsibleJSONDecoder)
    
    assert result == test_data
