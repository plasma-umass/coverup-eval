# file lib/ansible/utils/collection_loader/_collection_finder.py:77-108
# lines [82]
# branches ['81->82']

import os
import sys
import pytest
from unittest import mock
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder

@pytest.fixture
def mock_ansible_module():
    with mock.patch.dict('sys.modules', {'ansible': mock.Mock()}):
        sys.modules['ansible'].__file__ = '/fake/path/to/ansible/__init__.py'
        yield sys.modules['ansible']

def test_ansible_collection_finder_with_string_path(mock_ansible_module):
    # Mock the os.path functions used in the class
    with mock.patch('os.path.dirname', return_value='/fake/path/to/ansible'), \
         mock.patch('os.path.expanduser', side_effect=lambda x: x), \
         mock.patch('os.path.basename', return_value='ansible_collections'), \
         mock.patch('os.path.isdir', return_value=True), \
         mock.patch('ansible.utils.collection_loader._collection_finder.to_bytes', side_effect=lambda x, errors=None: x), \
         mock.patch('ansible.utils.collection_loader._collection_finder.to_native', side_effect=lambda x, errors=None: x):

        # Create an instance with a string path
        finder = _AnsibleCollectionFinder(paths='/fake/path/to/ansible/ansible_collections')

        # Verify that the paths attribute is correctly set
        assert finder._n_configured_paths == ['/fake/path/to/ansible']

def test_ansible_collection_finder_with_none_path(mock_ansible_module):
    # Mock the os.path functions used in the class
    with mock.patch('os.path.dirname', return_value='/fake/path/to/ansible'), \
         mock.patch('os.path.expanduser', side_effect=lambda x: x), \
         mock.patch('os.path.basename', return_value='ansible_collections'), \
         mock.patch('os.path.isdir', return_value=True), \
         mock.patch('ansible.utils.collection_loader._collection_finder.to_bytes', side_effect=lambda x, errors=None: x), \
         mock.patch('ansible.utils.collection_loader._collection_finder.to_native', side_effect=lambda x, errors=None: x):

        # Create an instance with None as paths
        finder = _AnsibleCollectionFinder(paths=None, scan_sys_paths=False)

        # Verify that the paths attribute is correctly set
        assert finder._n_configured_paths == []
