# file: lib/ansible/utils/vars.py:235-254
# asked: {"lines": [235, 236, 237, 241, 244, 245, 246, 248, 249, 251, 252, 254], "branches": [[236, 237], [236, 241], [248, 249], [248, 251], [251, 252], [251, 254]]}
# gained: {"lines": [235, 236, 237, 241, 244, 245, 246, 248, 249, 251, 252, 254], "branches": [[236, 237], [236, 241], [248, 249], [248, 251], [251, 252], [251, 254]]}

import pytest
from ansible.utils.vars import _isidentifier_PY3
from ansible.module_utils.six import string_types

def test_isidentifier_py3_with_non_string():
    assert _isidentifier_PY3(123) == False

def test_isidentifier_py3_with_non_ascii():
    assert _isidentifier_PY3('naïve') == False

def test_isidentifier_py3_with_non_identifier():
    assert _isidentifier_PY3('123abc') == False

def test_isidentifier_py3_with_keyword():
    assert _isidentifier_PY3('for') == False

def test_isidentifier_py3_with_valid_identifier():
    assert _isidentifier_PY3('valid_identifier') == True

def test_isidentifier_py3_with_empty_string():
    assert _isidentifier_PY3('') == False
