# file lib/ansible/plugins/filter/core.py:558-566
# lines [558, 561, 562, 563, 564, 566]
# branches ['561->562', '561->563', '563->564', '563->566']

import pytest
import os
from ansible.errors import AnsibleFilterTypeError

# Assuming the presence of string_types and is_sequence functions
# If not present, they need to be imported or defined for the test to work
from ansible.plugins.filter.core import path_join, string_types, is_sequence

def test_path_join_with_string(mocker):
    # Mock os.path.join to ensure it is called correctly
    mock_os_path_join = mocker.patch('os.path.join', return_value='/fake/path')
    test_string = '/fake/path'
    result = path_join(test_string)
    mock_os_path_join.assert_called_once_with(test_string)
    assert result == '/fake/path'

def test_path_join_with_sequence(mocker):
    # Mock os.path.join to ensure it is called correctly
    mock_os_path_join = mocker.patch('os.path.join', return_value='/fake/path/combined')
    test_sequence = ['/fake', 'path', 'combined']
    result = path_join(test_sequence)
    mock_os_path_join.assert_called_once_with(*test_sequence)
    assert result == '/fake/path/combined'

def test_path_join_with_invalid_type():
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        path_join(123)
    assert "|path_join expects string or sequence, got <class 'int'> instead." in str(excinfo.value)
