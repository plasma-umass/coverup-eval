# file: string_utils/manipulation.py:300-321
# asked: {"lines": [300, 315, 316, 318, 319, 321], "branches": [[315, 316], [315, 318], [318, 319], [318, 321]]}
# gained: {"lines": [300, 315, 316, 318, 319, 321], "branches": [[315, 316], [315, 318], [318, 319], [318, 321]]}

import pytest
from string_utils.manipulation import camel_case_to_snake, InvalidInputError
from string_utils.validation import is_string, is_camel_case
import re

CAMEL_CASE_REPLACE_RE = re.compile(r'(.)([A-Z][a-z]+)')

def test_camel_case_to_snake_valid_input(monkeypatch):
    def mock_is_string(input_string):
        return True

    def mock_is_camel_case(input_string):
        return True

    monkeypatch.setattr('string_utils.manipulation.is_string', mock_is_string)
    monkeypatch.setattr('string_utils.manipulation.is_camel_case', mock_is_camel_case)

    result = camel_case_to_snake('ThisIsACamelStringTest')
    assert result == 'this_is_a_camel_string_test'

def test_camel_case_to_snake_invalid_string(monkeypatch):
    def mock_is_string(input_string):
        return False

    monkeypatch.setattr('string_utils.manipulation.is_string', mock_is_string)

    with pytest.raises(InvalidInputError):
        camel_case_to_snake('ThisIsACamelStringTest')

def test_camel_case_to_snake_not_camel_case(monkeypatch):
    def mock_is_string(input_string):
        return True

    def mock_is_camel_case(input_string):
        return False

    monkeypatch.setattr('string_utils.manipulation.is_string', mock_is_string)
    monkeypatch.setattr('string_utils.manipulation.is_camel_case', mock_is_camel_case)

    result = camel_case_to_snake('this_is_not_camel_case')
    assert result == 'this_is_not_camel_case'
