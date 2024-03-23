# file lib/ansible/utils/vars.py:235-254
# lines [235, 236, 237, 241, 244, 245, 246, 248, 249, 251, 252, 254]
# branches ['236->237', '236->241', '248->249', '248->251', '251->252', '251->254']

import pytest
import keyword
from ansible.utils.vars import _isidentifier_PY3

@pytest.fixture
def non_string_objects():
    return [None, 123, 3.14, [], {}]

@pytest.fixture
def non_ascii_identifiers():
    return ['var_测试', '变量', 'переменная']

@pytest.fixture
def python_keywords():
    return keyword.kwlist

@pytest.fixture
def valid_identifiers():
    return ['_valid', 'var123', 'identifier_with_underscores']

def test_isidentifier_py3_with_non_string(non_string_objects):
    for obj in non_string_objects:
        assert not _isidentifier_PY3(obj), "Non-string object should not be considered a valid identifier"

def test_isidentifier_py3_with_non_ascii(non_ascii_identifiers):
    for ident in non_ascii_identifiers:
        assert not _isidentifier_PY3(ident), "Non-ASCII identifier should not be considered valid"

def test_isidentifier_py3_with_keywords(python_keywords):
    for keyword in python_keywords:
        assert not _isidentifier_PY3(keyword), "Python keyword should not be considered a valid identifier"

def test_isidentifier_py3_with_valid_identifiers(valid_identifiers):
    for ident in valid_identifiers:
        assert _isidentifier_PY3(ident), "Valid identifier should be considered valid"
