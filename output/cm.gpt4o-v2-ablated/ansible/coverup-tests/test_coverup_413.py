# file: lib/ansible/utils/vars.py:235-254
# asked: {"lines": [236, 237, 241, 244, 245, 246, 248, 249, 251, 252, 254], "branches": [[236, 237], [236, 241], [248, 249], [248, 251], [251, 252], [251, 254]]}
# gained: {"lines": [236, 237, 241, 244, 245, 246, 248, 249, 251, 252, 254], "branches": [[236, 237], [236, 241], [248, 249], [248, 251], [251, 252], [251, 254]]}

import pytest
import keyword
from ansible.utils.vars import _isidentifier_PY3

def test_isidentifier_py3_valid_identifier():
    assert _isidentifier_PY3("valid_identifier") == True

def test_isidentifier_py3_invalid_type():
    assert _isidentifier_PY3(123) == False

def test_isidentifier_py3_non_ascii():
    assert _isidentifier_PY3("valid_ñ_identifier") == False

def test_isidentifier_py3_not_identifier():
    assert _isidentifier_PY3("123invalid") == False

def test_isidentifier_py3_keyword():
    assert _isidentifier_PY3("for") == False
