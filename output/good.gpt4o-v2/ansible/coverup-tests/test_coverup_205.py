# file: lib/ansible/plugins/filter/core.py:290-305
# asked: {"lines": [290, 291, 293, 294, 295, 296, 298, 300, 301, 303, 305], "branches": [[294, 295], [294, 305], [295, 296], [295, 298], [300, 301], [300, 303]]}
# gained: {"lines": [290, 291, 293, 294, 295, 296, 298, 300, 301, 303, 305], "branches": [[294, 295], [294, 305], [295, 296], [295, 298], [300, 301], [300, 303]]}

import pytest
from jinja2.runtime import Undefined
from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_native, to_text
from ansible.plugins.filter.core import mandatory

class CustomUndefined(Undefined):
    def __init__(self, name=None):
        super().__init__()
        self._undefined_name = name

def test_mandatory_with_undefined_variable_with_name():
    var = CustomUndefined(name="test_var")
    with pytest.raises(AnsibleFilterError) as excinfo:
        mandatory(var)
    assert str(excinfo.value) == "Mandatory variable 'test_var'  not defined."

def test_mandatory_with_undefined_variable_without_name():
    var = CustomUndefined()
    with pytest.raises(AnsibleFilterError) as excinfo:
        mandatory(var)
    assert str(excinfo.value) == "Mandatory variable  not defined."

def test_mandatory_with_undefined_variable_with_custom_message():
    var = CustomUndefined(name="test_var")
    custom_msg = "Custom error message"
    with pytest.raises(AnsibleFilterError) as excinfo:
        mandatory(var, msg=custom_msg)
    assert str(excinfo.value) == custom_msg

def test_mandatory_with_defined_variable():
    var = "defined_var"
    assert mandatory(var) == var
