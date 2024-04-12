# file lib/ansible/utils/collection_loader/_collection_finder.py:860-877
# lines [868, 870, 871, 873, 875, 876]
# branches ['870->871', '870->873']

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils._text import to_text
from keyword import iskeyword

def is_python_identifier(name):
    try:
        compile('{} = None'.format(name), '<string>', 'exec')
        return True
    except SyntaxError:
        return False

@pytest.fixture
def cleanup():
    # Setup if necessary
    yield
    # Teardown if necessary

def test_ansible_collection_ref_is_valid_collection_name(mocker):
    mocker.patch('ansible.module_utils._text.to_text', side_effect=lambda x: x)
    mocker.patch('keyword.iskeyword', return_value=False)
    mocker.patch('ansible.utils.collection_loader._collection_finder.is_python_identifier', side_effect=is_python_identifier)

    # Test with a valid collection name
    valid_collection_name = 'namespace.collection'
    assert AnsibleCollectionRef.is_valid_collection_name(valid_collection_name) is True

    # Test with an invalid collection name (no dot)
    invalid_collection_name_no_dot = 'namespacecollection'
    assert AnsibleCollectionRef.is_valid_collection_name(invalid_collection_name_no_dot) is False

    # Test with an invalid collection name (more than one dot)
    invalid_collection_name_many_dots = 'namespace.sub.collection'
    assert AnsibleCollectionRef.is_valid_collection_name(invalid_collection_name_many_dots) is False

    # Test with an invalid collection name (Python keyword)
    mocker.patch('keyword.iskeyword', return_value=True)
    invalid_collection_name_keyword = 'namespace.if'
    assert AnsibleCollectionRef.is_valid_collection_name(invalid_collection_name_keyword) is False

    # Test with an invalid collection name (not a Python identifier)
    mocker.patch('keyword.iskeyword', return_value=False)
    mocker.patch('ansible.utils.collection_loader._collection_finder.is_python_identifier', side_effect=is_python_identifier)
    invalid_collection_name_not_identifier = 'namespace.123'
    assert AnsibleCollectionRef.is_valid_collection_name(invalid_collection_name_not_identifier) is False
