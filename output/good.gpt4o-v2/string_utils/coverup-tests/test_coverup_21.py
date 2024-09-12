# file: string_utils/manipulation.py:300-321
# asked: {"lines": [300, 315, 316, 318, 319, 321], "branches": [[315, 316], [315, 318], [318, 319], [318, 321]]}
# gained: {"lines": [300, 315, 316, 318, 319, 321], "branches": [[315, 316], [315, 318], [318, 319], [318, 321]]}

import pytest
from string_utils.manipulation import camel_case_to_snake
from string_utils.errors import InvalidInputError

def test_camel_case_to_snake_valid_camel_case():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'

def test_camel_case_to_snake_invalid_string():
    with pytest.raises(InvalidInputError):
        camel_case_to_snake(12345)

def test_camel_case_to_snake_not_camel_case():
    assert camel_case_to_snake('notcamelcase') == 'notcamelcase'

def test_camel_case_to_snake_custom_separator():
    assert camel_case_to_snake('ThisIsACamelStringTest', separator='-') == 'this-is-a-camel-string-test'
