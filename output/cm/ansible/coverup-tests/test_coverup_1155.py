# file lib/ansible/utils/collection_loader/_collection_finder.py:914-949
# lines [916, 918, 920, 921, 923, 924, 925, 926, 927, 929, 930, 932, 933, 934, 936, 938, 940, 941, 943, 944, 945, 947, 949]
# branches ['916->918', '916->920', '921->923', '921->926', '926->927', '926->929', '932->933', '932->949', '938->932', '938->940']

import os
import sys
from importlib import import_module
from unittest.mock import MagicMock, patch

import pytest

from ansible.utils.collection_loader._collection_finder import _get_collection_resource_path

class AnsibleCollectionRef:
    @staticmethod
    def try_parse_fqcr(name, ref_type):
        # Mock implementation for AnsibleCollectionRef.try_parse_fqcr
        if name.startswith("valid"):
            return MagicMock(collection="test.collection", subdirs="", resource="test_resource")
        return None

    def __init__(self, collection_name, subdirs, resource, ref_type):
        # Mock implementation for AnsibleCollectionRef.__init__
        self.n_python_package_name = "test.collection"

@pytest.fixture
def mock_ansible_collection_ref(mocker):
    mocker.patch('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef', AnsibleCollectionRef)

def test_get_collection_resource_path_playbook():
    with patch('ansible.utils.collection_loader._collection_finder._get_collection_playbook_path') as mock_playbook_path:
        mock_playbook_path.return_value = "playbook_path"
        result = _get_collection_resource_path("playbook_name", "playbook")
        assert result == "playbook_path"

def test_get_collection_resource_path_valid_fqcr(mock_ansible_collection_ref):
    with patch.dict('sys.modules', {'test.collection': MagicMock(__file__='test_file.py')}):
        result = _get_collection_resource_path("valid.collection.test_resource", "role")
        assert result is not None
        assert result[1] is not None
        assert result[2] == "test.collection"

def test_get_collection_resource_path_invalid_fqcr_no_collection_list():
    result = _get_collection_resource_path("invalid.collection.test_resource", "role")
    assert result is None

def test_get_collection_resource_path_unqualified_with_collection_list(mock_ansible_collection_ref):
    with patch.dict('sys.modules', {'test.collection': MagicMock(__file__='test_file.py')}):
        result = _get_collection_resource_path("unqualified_resource", "role", collection_list=["test.collection"])
        assert result is not None
        assert result[1] is not None
        assert result[2] == "test.collection"

def test_get_collection_resource_path_module_not_found(mock_ansible_collection_ref):
    with patch.dict('sys.modules', {}):
        result = _get_collection_resource_path("unqualified_resource", "role", collection_list=["nonexistent.collection"])
        assert result is None

def test_get_collection_resource_path_general_exception(mock_ansible_collection_ref):
    with patch.dict('sys.modules', {'test.collection': MagicMock(__file__='test_file.py')}):
        with patch('ansible.utils.collection_loader._collection_finder.import_module', side_effect=Exception):
            result = _get_collection_resource_path("unqualified_resource", "role", collection_list=["test.collection"])
            assert result is None

# Run the tests
def run_tests():
    pytest.main([__file__])

if __name__ == "__main__":
    run_tests()
