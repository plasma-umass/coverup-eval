# file: lib/ansible/galaxy/api.py:618-662
# asked: {"lines": [626, 628, 629, 630, 631, 632, 633, 635, 636, 638, 639, 640, 641, 642, 643, 648, 649, 650, 653, 654, 656, 658, 659, 660, 662], "branches": [[629, 630], [629, 631], [631, 632], [631, 635], [653, 654], [653, 656]]}
# gained: {"lines": [626, 628, 629, 630, 631, 632, 633, 635, 636, 638, 639, 640, 641, 642, 643, 648, 649, 650, 653, 654, 658, 659, 660, 662], "branches": [[629, 630], [629, 631], [631, 632], [631, 635], [653, 654]]}

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
    return GalaxyAPI(galaxy='fake_galaxy', name='fake_name', url='http://fake_api_server', available_api_versions={'v2': 'v2', 'v3': 'v3'})

def test_publish_collection_path_does_not_exist(galaxy_api, monkeypatch):
    monkeypatch.setattr(galaxy_api, '_call_galaxy', lambda *args, **kwargs: {'task': 'fake_task_uri'})
    with pytest.raises(AnsibleError, match="The collection path specified 'non_existent_path' does not exist."):
        galaxy_api.publish_collection('non_existent_path')

def test_publish_collection_not_a_tarball(galaxy_api, monkeypatch):
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    monkeypatch.setattr(tarfile, 'is_tarfile', lambda x: False)
    monkeypatch.setattr(galaxy_api, '_call_galaxy', lambda *args, **kwargs: {'task': 'fake_task_uri'})
    with pytest.raises(AnsibleError, match="The collection path specified 'not_a_tarball' is not a tarball, use 'ansible-galaxy collection build' to create a proper release artifact."):
        galaxy_api.publish_collection('not_a_tarball')

def test_publish_collection_success(galaxy_api, monkeypatch):
    mock_file_content = b"fake tar content"
    mock_sha256 = secure_hash_s(mock_file_content, hash_func=hashlib.sha256)
    mock_b_form_data = b"mock_form_data"
    mock_headers = {'Content-type': 'multipart/form-data', 'Content-length': len(mock_b_form_data)}
    mock_response = {'task': 'fake_task_uri'}

    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    monkeypatch.setattr(tarfile, 'is_tarfile', lambda x: True)
    monkeypatch.setattr('builtins.open', mock_open(read_data=mock_file_content))
    monkeypatch.setattr('ansible.module_utils.urls.prepare_multipart', lambda x: ('multipart/form-data', mock_b_form_data))
    monkeypatch.setattr(galaxy_api, '_call_galaxy', lambda *args, **kwargs: mock_response)

    result = galaxy_api.publish_collection('fake_collection_path')
    assert result == 'fake_task_uri'
