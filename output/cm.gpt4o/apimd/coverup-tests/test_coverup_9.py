# file apimd/parser.py:62-71
# lines [62, 64, 66, 67, 69, 70, 71]
# branches ['64->66', '64->71', '66->67', '66->69', '69->64', '69->70']

import pytest
from apimd.parser import is_public_family

def test_is_public_family(mocker):
    # Mock the is_magic function to control its behavior
    mock_is_magic = mocker.patch('apimd.parser.is_magic', side_effect=lambda x: x.startswith('__') and x.endswith('__'))

    # Test case where name is from public modules
    assert is_public_family('public.module') == True

    # Test case where name contains a magic name
    assert is_public_family('public.__magic__.module') == True

    # Test case where name contains a local or private name
    assert is_public_family('public._private.module') == False

    # Test case where name is entirely magic names
    assert is_public_family('__magic__.__anothermagic__') == True

    # Test case where name is a mix of public and private names
    assert is_public_family('public._private.__magic__') == False
