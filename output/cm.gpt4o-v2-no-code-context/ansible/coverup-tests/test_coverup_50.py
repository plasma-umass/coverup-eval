# file: lib/ansible/module_utils/common/validation.py:42-67
# asked: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67], "branches": [[44, 46], [44, 49], [46, 47], [46, 48], [49, 50], [49, 54], [50, 51], [50, 52], [54, 55], [54, 58], [55, 56], [55, 57], [60, 61], [60, 63], [65, 66], [65, 67]]}
# gained: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66], "branches": [[44, 46], [44, 49], [46, 47], [46, 48], [49, 50], [49, 54], [50, 51], [50, 52], [54, 55], [54, 58], [55, 56], [55, 57], [60, 61], [60, 63], [65, 66]]}

import pytest
from ansible.module_utils.common.validation import safe_eval

def test_safe_eval_non_string():
    assert safe_eval(123) == 123
    assert safe_eval(123, include_exceptions=True) == (123, None)

def test_safe_eval_method_call():
    assert safe_eval("os.system('ls')") == "os.system('ls')"
    assert safe_eval("os.system('ls')", include_exceptions=True) == ("os.system('ls')", None)

def test_safe_eval_import_statement():
    assert safe_eval("import os") == "import os"
    assert safe_eval("import os", include_exceptions=True) == ("import os", None)

def test_safe_eval_literal_eval():
    assert safe_eval("123") == 123
    assert safe_eval("123", include_exceptions=True) == (123, None)

def test_safe_eval_literal_eval_exception():
    result, exception = safe_eval("invalid_literal", include_exceptions=True)
    assert result == "invalid_literal"
    assert isinstance(exception, Exception)
