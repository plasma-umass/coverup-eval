# file lib/ansible/plugins/filter/core.py:290-305
# lines [290, 291, 293, 294, 295, 296, 298, 300, 301, 303, 305]
# branches ['294->295', '294->305', '295->296', '295->298', '300->301', '300->303']

import pytest
from jinja2.runtime import Undefined
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import mandatory
from ansible.module_utils._text import to_text, to_native

def test_mandatory_with_undefined_name(mocker):
    mock_undefined = mocker.Mock(spec=Undefined)
    mock_undefined._undefined_name = 'test_var'
    
    with pytest.raises(AnsibleFilterError) as excinfo:
        mandatory(mock_undefined)
    
    assert "Mandatory variable 'test_var'  not defined." in str(excinfo.value)

def test_mandatory_with_undefined_name_and_custom_msg(mocker):
    mock_undefined = mocker.Mock(spec=Undefined)
    mock_undefined._undefined_name = 'test_var'
    
    with pytest.raises(AnsibleFilterError) as excinfo:
        mandatory(mock_undefined, msg="Custom error message")
    
    assert "Custom error message" in str(excinfo.value)

def test_mandatory_with_undefined_no_name(mocker):
    mock_undefined = mocker.Mock(spec=Undefined)
    mock_undefined._undefined_name = None
    
    with pytest.raises(AnsibleFilterError) as excinfo:
        mandatory(mock_undefined)
    
    assert "Mandatory variable  not defined." in str(excinfo.value)

def test_mandatory_with_defined():
    defined_var = "defined_value"
    result = mandatory(defined_var)
    assert result == defined_var
