# file lib/ansible/template/native_helpers.py:23-43
# lines [23, 27, 28, 29, 30, 31, 32, 34, 41, 43]
# branches ['27->28', '27->30', '28->29', '28->43', '30->31', '30->34', '31->32', '31->43', '34->41', '34->43']

import pytest
from ansible.template.native_helpers import _fail_on_undefined
from jinja2.runtime import StrictUndefined, UndefinedError
from collections.abc import Mapping, Sequence

# Test function to cover the missing lines/branches
def test_fail_on_undefined_with_strict_undefined():
    with pytest.raises(UndefinedError):
        _fail_on_undefined(StrictUndefined())

    with pytest.raises(UndefinedError):
        _fail_on_undefined({'key': StrictUndefined()})

    with pytest.raises(UndefinedError):
        _fail_on_undefined([StrictUndefined()])

    # Verify that non-undefined values pass through without error
    assert _fail_on_undefined({'key': 'value'}) == {'key': 'value'}
    assert _fail_on_undefined(['value']) == ['value']
    assert _fail_on_undefined('value') == 'value'
