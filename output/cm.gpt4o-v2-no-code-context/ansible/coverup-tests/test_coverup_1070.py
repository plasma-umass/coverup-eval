# file: lib/ansible/module_utils/common/validation.py:42-67
# asked: {"lines": [67], "branches": [[65, 67]]}
# gained: {"lines": [67], "branches": [[65, 67]]}

import pytest
from ansible.module_utils.common.validation import safe_eval

def test_safe_eval_non_string():
    assert safe_eval(123) == 123
    assert safe_eval(123, include_exceptions=True) == (123, None)

def test_safe_eval_method_call():
    assert safe_eval("os.system('ls')") == "os.system('ls')"
    assert safe_eval("os.system('ls')", include_exceptions=True) == ("os.system('ls')", None)

def test_safe_eval_import():
    assert safe_eval("import os") == "import os"
    assert safe_eval("import os", include_exceptions=True) == ("import os", None)

def test_safe_eval_literal():
    assert safe_eval("123") == 123
    assert safe_eval("'abc'") == 'abc'
    assert safe_eval("[1, 2, 3]") == [1, 2, 3]
    assert safe_eval("{'key': 'value'}") == {'key': 'value'}
    assert safe_eval("123", include_exceptions=True) == (123, None)

def test_safe_eval_exception():
    assert safe_eval("invalid_syntax") == "invalid_syntax"
    result, exception = safe_eval("invalid_syntax", include_exceptions=True)
    assert result == "invalid_syntax"
    assert isinstance(exception, Exception)
