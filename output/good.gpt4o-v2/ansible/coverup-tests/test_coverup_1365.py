# file: lib/ansible/module_utils/common/parameters.py:541-566
# asked: {"lines": [544, 554, 555, 560, 561, 562, 563, 564, 565], "branches": [[543, 544], [551, 557], [552, 554], [554, 555], [554, 557], [562, 563], [562, 564]]}
# gained: {"lines": [554, 555, 560, 561, 562, 563, 564, 565], "branches": [[551, 557], [552, 554], [554, 555], [562, 563], [562, 564]]}

import pytest
from ansible.module_utils.common.parameters import _validate_elements
from ansible.module_utils.errors import AnsibleValidationErrorMultiple, ElementError
from ansible.module_utils.six import string_types

def test_validate_elements_with_string_parameter():
    errors = AnsibleValidationErrorMultiple()
    result = _validate_elements('str', 'param', ['value1', 'value2'], errors=errors)
    assert result == ['value1', 'value2']
    assert len(errors.errors) == 0

def test_validate_elements_with_dict_parameter():
    errors = AnsibleValidationErrorMultiple()
    result = _validate_elements('str', {'param': 'value'}, ['value1', 'value2'], errors=errors)
    assert result == ['value1', 'value2']
    assert len(errors.errors) == 0

def test_validate_elements_with_type_error():
    errors = AnsibleValidationErrorMultiple()
    result = _validate_elements('int', 'param', ['value1', 'value2'], errors=errors)
    assert result == []
    assert len(errors.errors) == 2
    assert "Elements value for option 'param' is of type <class 'str'> and we were unable to convert to int" in str(errors.errors[0])

def test_validate_elements_with_options_context():
    errors = AnsibleValidationErrorMultiple()
    result = _validate_elements('int', 'param', ['value1'], options_context=['context1', 'context2'], errors=errors)
    assert result == []
    assert len(errors.errors) == 1
    assert "Elements value for option 'param' found in 'context1 -> context2' is of type <class 'str'> and we were unable to convert to int" in str(errors.errors[0])
