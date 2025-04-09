# file: lib/ansible/module_utils/common/text/converters.py:150-238
# asked: {"lines": [223, 224, 225, 226, 228], "branches": []}
# gained: {"lines": [223, 224, 225, 226, 228], "branches": []}

import pytest
from ansible.module_utils.common.text.converters import to_text

def test_to_text_simplerepr_unicode_error(monkeypatch):
    class UnicodeErrorObj:
        def __str__(self):
            raise UnicodeError("str error")
        
        def __repr__(self):
            raise UnicodeError("repr error")
    
    obj = UnicodeErrorObj()
    result = to_text(obj, nonstring='simplerepr')
    assert result == u''

def test_to_text_simplerepr_repr_unicode_error(monkeypatch):
    class UnicodeErrorObj:
        def __str__(self):
            raise UnicodeError("str error")
        
        def __repr__(self):
            return "repr string"
    
    obj = UnicodeErrorObj()
    result = to_text(obj, nonstring='simplerepr')
    assert result == "repr string"

def test_to_text_simplerepr_str_unicode_error(monkeypatch):
    class UnicodeErrorObj:
        def __str__(self):
            raise UnicodeError("str error")
        
        def __repr__(self):
            return "repr string"
    
    obj = UnicodeErrorObj()
    result = to_text(obj, nonstring='simplerepr')
    assert result == "repr string"

def test_to_text_simplerepr_no_unicode_error(monkeypatch):
    class NoUnicodeErrorObj:
        def __str__(self):
            return "str string"
        
        def __repr__(self):
            return "repr string"
    
    obj = NoUnicodeErrorObj()
    result = to_text(obj, nonstring='simplerepr')
    assert result == "str string"
