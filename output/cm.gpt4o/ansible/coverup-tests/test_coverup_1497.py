# file lib/ansible/utils/collection_loader/_collection_finder.py:765-767
# lines [767]
# branches []

import pytest
from unittest.mock import patch

# Assuming the AnsibleCollectionRef class is imported from the module
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

class TestAnsibleCollectionRef(AnsibleCollectionRef):
    def __init__(self, fqcr_value):
        self._fqcr = fqcr_value

@pytest.fixture
def mock_ansible_collection_ref():
    with patch('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef', new=TestAnsibleCollectionRef):
        yield

def test_fqcr_property(mock_ansible_collection_ref):
    # Arrange
    expected_fqcr = 'some_fqcr_value'
    ansible_collection_ref_instance = TestAnsibleCollectionRef(expected_fqcr)

    # Act
    result = ansible_collection_ref_instance.fqcr

    # Assert
    assert result == expected_fqcr

    # Clean up
    del ansible_collection_ref_instance
