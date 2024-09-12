# file: lib/ansible/utils/vars.py:235-254
# asked: {"lines": [235, 236, 237, 241, 244, 245, 246, 248, 249, 251, 252, 254], "branches": [[236, 237], [236, 241], [248, 249], [248, 251], [251, 252], [251, 254]]}
# gained: {"lines": [235, 236, 237, 241, 244, 245, 246, 248, 249, 251, 252, 254], "branches": [[236, 237], [236, 241], [248, 249], [248, 251], [251, 252], [251, 254]]}

import pytest
from ansible.utils.vars import _isidentifier_PY3

def test_isidentifier_py3_non_string():
    assert not _isidentifier_PY3(123)  # Non-string input

def test_isidentifier_py3_non_ascii():
    assert not _isidentifier_PY3('naïve')  # Non-ASCII input

def test_isidentifier_py3_not_identifier():
    assert not _isidentifier_PY3('123abc')  # Not a valid identifier

def test_isidentifier_py3_keyword():
    assert not _isidentifier_PY3('for')  # Python keyword

def test_isidentifier_py3_valid_identifier():
    assert _isidentifier_PY3('valid_identifier')  # Valid identifier

