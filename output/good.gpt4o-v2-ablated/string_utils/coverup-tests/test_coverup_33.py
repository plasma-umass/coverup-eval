# file: string_utils/manipulation.py:324-354
# asked: {"lines": [341, 342, 344, 345, 347, 349, 350, 352, 354], "branches": [[341, 342], [341, 344], [344, 345], [344, 347], [349, 350], [349, 352]]}
# gained: {"lines": [341, 342, 344, 345, 347, 349, 350, 352, 354], "branches": [[341, 342], [341, 344], [344, 345], [344, 347], [349, 350], [349, 352]]}

import pytest
from string_utils.manipulation import snake_case_to_camel, InvalidInputError
from string_utils.validation import is_string, is_snake_case, is_full_string

def test_snake_case_to_camel_valid_input_upper_case_first(monkeypatch):
    def mock_is_string(input_string):
        return True

    def mock_is_snake_case(input_string, separator):
        return True

    def mock_is_full_string(s):
        return True

    monkeypatch.setattr('string_utils.manipulation.is_string', mock_is_string)
    monkeypatch.setattr('string_utils.manipulation.is_snake_case', mock_is_snake_case)
    monkeypatch.setattr('string_utils.manipulation.is_full_string', mock_is_full_string)

    result = snake_case_to_camel('the_snake_is_green')
    assert result == 'TheSnakeIsGreen'

def test_snake_case_to_camel_valid_input_lower_case_first(monkeypatch):
    def mock_is_string(input_string):
        return True

    def mock_is_snake_case(input_string, separator):
        return True

    def mock_is_full_string(s):
        return True

    monkeypatch.setattr('string_utils.manipulation.is_string', mock_is_string)
    monkeypatch.setattr('string_utils.manipulation.is_snake_case', mock_is_snake_case)
    monkeypatch.setattr('string_utils.manipulation.is_full_string', mock_is_full_string)

    result = snake_case_to_camel('the_snake_is_green', upper_case_first=False)
    assert result == 'theSnakeIsGreen'

def test_snake_case_to_camel_invalid_input_not_string(monkeypatch):
    def mock_is_string(input_string):
        return False

    monkeypatch.setattr('string_utils.manipulation.is_string', mock_is_string)

    with pytest.raises(InvalidInputError):
        snake_case_to_camel(123)

def test_snake_case_to_camel_invalid_input_not_snake_case(monkeypatch):
    def mock_is_string(input_string):
        return True

    def mock_is_snake_case(input_string, separator):
        return False

    monkeypatch.setattr('string_utils.manipulation.is_string', mock_is_string)
    monkeypatch.setattr('string_utils.manipulation.is_snake_case', mock_is_snake_case)

    result = snake_case_to_camel('not_snake_case')
    assert result == 'not_snake_case'

def test_snake_case_to_camel_custom_separator(monkeypatch):
    def mock_is_string(input_string):
        return True

    def mock_is_snake_case(input_string, separator):
        return True

    def mock_is_full_string(s):
        return True

    monkeypatch.setattr('string_utils.manipulation.is_string', mock_is_string)
    monkeypatch.setattr('string_utils.manipulation.is_snake_case', mock_is_snake_case)
    monkeypatch.setattr('string_utils.manipulation.is_full_string', mock_is_full_string)

    result = snake_case_to_camel('the-snake-is-green', separator='-')
    assert result == 'TheSnakeIsGreen'
