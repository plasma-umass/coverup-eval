# file lib/ansible/module_utils/common/validation.py:103-134
# lines [103, 118, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 134]
# branches ['119->120', '119->122', '122->123', '122->127', '124->122', '124->125', '127->128', '127->134', '128->129', '128->134', '130->131', '130->132']

import pytest
from ansible.module_utils.common.validation import check_required_one_of
from ansible.module_utils._text import to_native

def test_check_required_one_of_missing_terms():
    parameters = {'name': 'test'}
    terms = [('missing1', 'missing2'), ('missing3', 'missing4')]
    options_context = ['parent', 'child']

    with pytest.raises(TypeError) as excinfo:
        check_required_one_of(terms, parameters, options_context=options_context)

    assert "one of the following is required: missing1, missing2 found in parent -> child" in str(excinfo.value)

def test_check_required_one_of_present_terms():
    parameters = {'name': 'test', 'missing1': 'value', 'missing3': 'value'}
    terms = [('missing1', 'missing2'), ('missing3', 'missing4')]

    result = check_required_one_of(terms, parameters)
    assert result == []

def test_check_required_one_of_no_terms():
    parameters = {'name': 'test'}
    terms = None

    result = check_required_one_of(terms, parameters)
    assert result == []

def test_check_required_one_of_empty_terms():
    parameters = {'name': 'test'}
    terms = []

    result = check_required_one_of(terms, parameters)
    assert result == []
