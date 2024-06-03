# file lib/ansible/utils/collection_loader/_collection_finder.py:110-128
# lines [114, 119, 128]
# branches ['113->114', '118->119', '127->128']

import sys
import pytest
from unittest import mock

# Assuming the module and classes are imported correctly
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder, AnsibleCollectionConfig

@pytest.fixture
def setup_and_teardown():
    # Setup: Add mock objects to sys.meta_path and sys.path_hooks
    mock_meta_path = mock.Mock(spec=_AnsibleCollectionFinder)
    mock_path_hook = mock.Mock()
    mock_path_hook.__self__ = mock_meta_path

    sys.meta_path.append(mock_meta_path)
    sys.path_hooks.append(mock_path_hook)

    # Ensure AnsibleCollectionConfig._collection_finder is set
    AnsibleCollectionConfig._collection_finder = mock_meta_path

    yield

    # Teardown: Clean up sys.meta_path and sys.path_hooks
    if mock_meta_path in sys.meta_path:
        sys.meta_path.remove(mock_meta_path)
    if mock_path_hook in sys.path_hooks:
        sys.path_hooks.remove(mock_path_hook)

    # Reset AnsibleCollectionConfig._collection_finder
    AnsibleCollectionConfig._collection_finder = None

def test_remove_method(setup_and_teardown):
    # Call the _remove method
    _AnsibleCollectionFinder._remove()

    # Assertions to verify the postconditions
    assert not any(isinstance(mps, _AnsibleCollectionFinder) for mps in sys.meta_path), "meta_path not cleaned up"
    assert not any(hasattr(ph, '__self__') and isinstance(ph.__self__, _AnsibleCollectionFinder) for ph in sys.path_hooks), "path_hooks not cleaned up"
    assert AnsibleCollectionConfig.collection_finder is None, "collection_finder not reset"
