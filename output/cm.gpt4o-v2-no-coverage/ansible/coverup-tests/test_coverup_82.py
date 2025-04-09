# file: lib/ansible/galaxy/api.py:618-662
# asked: {"lines": [618, 619, 626, 628, 629, 630, 631, 632, 633, 635, 636, 638, 639, 640, 641, 642, 643, 648, 649, 650, 653, 654, 656, 658, 659, 660, 662], "branches": [[629, 630], [629, 631], [631, 632], [631, 635], [653, 654], [653, 656]]}
# gained: {"lines": [618, 619, 626, 628, 629, 630, 631, 632, 633, 635, 636, 638, 639, 640, 641, 642, 643, 648, 649, 650, 653, 654, 658, 659, 660, 662], "branches": [[629, 630], [629, 631], [631, 632], [631, 635], [653, 654]]}

import pytest
import os
import tarfile
import hashlib
from unittest.mock import patch, mock_open, MagicMock
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_bytes, to_native
from ansible.module_utils.urls import prepare_multipart
from ansible.utils.hashing import secure_hash_s
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(galaxy='fake_galaxy', name='fake_name', url='http://fake_url', available_api_versions={'v2': 'v2/', 'v3': 'v3/'})

def test_publish_collection_success(galaxy_api, monkeypatch):
    collection_path = 'test_collection.tar.gz'
    b_collection_path = to_bytes(collection_path, errors='surrogate_or_strict')
    fake_sha256 = 'fake_sha256_hash'
    fake_response = {'task': 'fake_task_uri'}

    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    monkeypatch.setattr(tarfile, 'is_tarfile', lambda x: True)
    monkeypatch.setattr(secure_hash_s, '__call__', lambda data, hash_func: fake_sha256)
    monkeypatch.setattr(GalaxyAPI, '_call_galaxy', lambda self, url, args, headers, method, auth_required, error_context_msg: fake_response)

    with patch('builtins.open', mock_open(read_data=b'fake_data')):
        result = galaxy_api.publish_collection(collection_path)

    assert result == 'fake_task_uri'

def test_publish_collection_path_not_exist(galaxy_api, monkeypatch):
    collection_path = 'non_existent_collection.tar.gz'
    b_collection_path = to_bytes(collection_path, errors='surrogate_or_strict')

    monkeypatch.setattr(os.path, 'exists', lambda x: False)

    with pytest.raises(AnsibleError, match=f"The collection path specified '{to_native(collection_path)}' does not exist."):
        galaxy_api.publish_collection(collection_path)

def test_publish_collection_not_tarfile(galaxy_api, monkeypatch):
    collection_path = 'invalid_collection.txt'
    b_collection_path = to_bytes(collection_path, errors='surrogate_or_strict')

    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    monkeypatch.setattr(tarfile, 'is_tarfile', lambda x: False)

    with pytest.raises(AnsibleError, match=f"The collection path specified '{to_native(collection_path)}' is not a tarball, use 'ansible-galaxy collection build' to create a proper release artifact."):
        galaxy_api.publish_collection(collection_path)
