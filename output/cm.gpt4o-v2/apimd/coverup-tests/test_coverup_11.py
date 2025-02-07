# file: apimd/parser.py:62-71
# asked: {"lines": [62, 64, 66, 67, 69, 70, 71], "branches": [[64, 66], [64, 71], [66, 67], [66, 69], [69, 64], [69, 70]]}
# gained: {"lines": [62, 64, 66, 67, 69, 70, 71], "branches": [[64, 66], [64, 71], [66, 67], [66, 69], [69, 64], [69, 70]]}

import pytest
from apimd.parser import is_public_family

def test_is_public_family_with_magic_name(mocker):
    mocker.patch('apimd.parser.is_magic', return_value=True)
    assert is_public_family('__magic__') == True

def test_is_public_family_with_private_name(mocker):
    mocker.patch('apimd.parser.is_magic', return_value=False)
    assert is_public_family('_private') == False

def test_is_public_family_with_public_name(mocker):
    mocker.patch('apimd.parser.is_magic', return_value=False)
    assert is_public_family('public') == True

def test_is_public_family_with_mixed_names(mocker):
    mocker.patch('apimd.parser.is_magic', side_effect=lambda x: x == '__magic__')
    assert is_public_family('__magic__._private.public') == False
