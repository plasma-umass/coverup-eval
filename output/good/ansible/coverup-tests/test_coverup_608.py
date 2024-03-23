# file lib/ansible/utils/helpers.py:37-43
# lines [37, 41, 42, 43]
# branches ['41->42', '41->43']

import pytest
from ansible.utils.helpers import object_to_dict

class MockObject:
    def __init__(self):
        self.public_attr = 'value'
        self._private_attr = 'should not be included'

    def public_method(self):
        pass

    def _private_method(self):
        pass

@pytest.fixture
def mock_object():
    return MockObject()

def test_object_to_dict_excludes_private_and_specified_attributes(mock_object):
    # Test excluding private attributes and a specified public attribute
    result = object_to_dict(mock_object, exclude=['public_method'])
    assert 'public_attr' in result
    assert result['public_attr'] == 'value'
    assert '_private_attr' not in result
    assert 'public_method' not in result
    assert '_private_method' not in result

def test_object_to_dict_with_no_exclusions(mock_object):
    # Test with no exclusions, private attributes should still be excluded
    result = object_to_dict(mock_object)
    assert 'public_attr' in result
    assert result['public_attr'] == 'value'
    assert '_private_attr' not in result
    assert 'public_method' in result
    assert '_private_method' not in result

def test_object_to_dict_with_non_list_exclude(mock_object):
    # Test with exclude parameter that is not a list
    result = object_to_dict(mock_object, exclude='public_method')
    assert 'public_attr' in result
    assert result['public_attr'] == 'value'
    assert '_private_attr' not in result
    assert 'public_method' in result
    assert '_private_method' not in result
