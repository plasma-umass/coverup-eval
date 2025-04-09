# file lib/ansible/collections/list.py:50-102
# lines [58, 59, 60, 61, 62, 63, 64, 65, 67, 69, 70, 72, 73, 75, 77, 79, 80, 82, 84, 85, 87, 89, 90, 92, 94, 97, 98, 99, 100, 101, 102]
# branches ['60->61', '60->69', '61->62', '61->67', '70->exit', '70->72', '72->73', '72->75', '77->70', '77->79', '79->80', '79->82', '84->70', '84->85', '87->84', '87->89', '89->90', '89->92', '94->84', '94->97', '97->94', '97->98', '100->94', '100->101']

import os
import pytest
from ansible.errors import AnsibleError
from ansible.collections.list import list_collection_dirs
from ansible.module_utils._text import to_bytes

def test_list_collection_dirs_with_filter(mocker, tmp_path):
    # Setup mock for list_valid_collection_paths
    mocker.patch('ansible.collections.list.list_valid_collection_paths', return_value=[str(tmp_path)])
    
    # Create a fake collection structure
    namespace = 'test_namespace'
    collection = 'test_collection'
    coll_root = tmp_path / 'ansible_collections' / namespace / collection
    coll_root.mkdir(parents=True)
    
    # Create a file inside the collection directory to simulate a valid collection
    (coll_root / 'MANIFEST.json').touch()
    
    # Mock os.path.isdir to return True for our fake collection path
    mocker.patch('os.path.isdir', return_value=True)
    
    # Mock is_collection_path to return True for our fake collection path
    mocker.patch('ansible.collections.list.is_collection_path', return_value=True)
    
    # Test with a specific collection filter
    coll_filter = f'{namespace}.{collection}'
    result = list(list_collection_dirs(coll_filter=coll_filter))
    
    # Verify that the result contains the path to the collection
    expected_path = to_bytes(str(coll_root), errors='surrogate_or_strict')
    assert expected_path in result
    
    # Test with a specific namespace filter
    coll_filter = namespace
    result = list(list_collection_dirs(coll_filter=coll_filter))
    
    # Verify that the result contains the path to the collection
    assert expected_path in result
    
    # Test with an invalid collection filter
    with pytest.raises(AnsibleError):
        list(list_collection_dirs(coll_filter='invalid.collection.name'))
    
    # Test with no filter
    result = list(list_collection_dirs())
    
    # Verify that the result contains the path to the collection
    assert expected_path in result

    # Cleanup
    mocker.stopall()
