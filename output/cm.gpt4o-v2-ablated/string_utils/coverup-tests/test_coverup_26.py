# file: string_utils/validation.py:42-78
# asked: {"lines": [42, 43, 44, 45, 47, 49, 50, 51, 53, 54, 55, 56, 58, 60, 61, 63, 65, 66, 67, 69, 70, 71, 73, 75, 76, 78], "branches": [[44, 45], [44, 47], [50, 51], [50, 63], [54, 55], [54, 58], [66, 67], [66, 78], [70, 71], [70, 73]]}
# gained: {"lines": [42, 43, 44, 45, 47, 49, 50, 51, 53, 54, 55, 56, 58, 60, 61, 63, 65, 66, 67, 69, 70, 71, 73, 75, 76, 78], "branches": [[44, 45], [44, 47], [50, 51], [50, 63], [54, 55], [54, 58], [66, 67], [66, 78], [70, 71], [70, 73]]}

import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

def test_isbn_checker_init_invalid_input():
    with pytest.raises(InvalidInputError):
        __ISBNChecker(12345)

def test_isbn_checker_init_normalize():
    checker = __ISBNChecker("978-3-16-148410-0")
    assert checker.input_string == "9783161484100"

def test_isbn_checker_init_no_normalize():
    checker = __ISBNChecker("978-3-16-148410-0", normalize=False)
    assert checker.input_string == "978-3-16-148410-0"

def test_isbn_13_valid():
    checker = __ISBNChecker("9783161484100")
    assert checker.is_isbn_13() is True

def test_isbn_13_invalid_length():
    checker = __ISBNChecker("978316148410")
    assert checker.is_isbn_13() is False

def test_isbn_13_invalid_characters():
    checker = __ISBNChecker("97831614841X0")
    assert checker.is_isbn_13() is False

def test_isbn_10_valid():
    checker = __ISBNChecker("0306406152")
    assert checker.is_isbn_10() is True

def test_isbn_10_invalid_length():
    checker = __ISBNChecker("030640615")
    assert checker.is_isbn_10() is False

def test_isbn_10_invalid_characters():
    checker = __ISBNChecker("03064061X2")
    assert checker.is_isbn_10() is False
