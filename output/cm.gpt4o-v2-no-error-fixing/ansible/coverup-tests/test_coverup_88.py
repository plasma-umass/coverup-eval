# file: lib/ansible/utils/collection_loader/_collection_finder.py:110-128
# asked: {"lines": [110, 111, 112, 113, 114, 117, 118, 119, 122, 124, 127, 128], "branches": [[112, 113], [112, 117], [113, 112], [113, 114], [117, 118], [117, 122], [118, 117], [118, 119], [127, 0], [127, 128]]}
# gained: {"lines": [110, 111, 112, 113, 114, 117, 118, 122, 124, 127], "branches": [[112, 113], [112, 117], [113, 112], [113, 114], [117, 118], [117, 122], [118, 117], [127, 0]]}

import pytest
import sys
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
from ansible.utils.collection_loader._collection_config import AnsibleCollectionConfig

@pytest.fixture
def setup_and_teardown():
    # Setup: Ensure _AnsibleCollectionFinder is in sys.meta_path and sys.path_hooks
    finder_instance = _AnsibleCollectionFinder()
    sys.meta_path.append(finder_instance)
    sys.path_hooks.append(lambda: finder_instance)
    AnsibleCollectionConfig._collection_finder = finder_instance

    yield

    # Teardown: Clean up sys.meta_path, sys.path_hooks, and sys.path_importer_cache
    if finder_instance in sys.meta_path:
        sys.meta_path.remove(finder_instance)
    sys.path_hooks = [ph for ph in sys.path_hooks if not (hasattr(ph, '__self__') and isinstance(ph.__self__, _AnsibleCollectionFinder))]
    sys.path_importer_cache.clear()
    AnsibleCollectionConfig._collection_finder = None

def test_remove_method(setup_and_teardown):
    # Ensure the finder is set before removal
    assert AnsibleCollectionConfig._collection_finder is not None

    # Call the _remove method
    _AnsibleCollectionFinder._remove()

    # Assertions to verify the postconditions
    assert _AnsibleCollectionFinder not in sys.meta_path
    assert all(not (hasattr(ph, '__self__') and isinstance(ph.__self__, _AnsibleCollectionFinder)) for ph in sys.path_hooks)
    assert AnsibleCollectionConfig._collection_finder is None
