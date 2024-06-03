# file string_utils/validation.py:42-78
# lines [42, 43, 44, 45, 47, 49, 50, 51, 53, 54, 55, 56, 58, 60, 61, 63, 65, 66, 67, 69, 70, 71, 73, 75, 76, 78]
# branches ['44->45', '44->47', '50->51', '50->63', '54->55', '54->58', '66->67', '66->78', '70->71', '70->73']

import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

def test_isbn_checker_invalid_input():
    with pytest.raises(InvalidInputError):
        __ISBNChecker(12345)

def test_isbn_checker_normalize():
    checker = __ISBNChecker("978-3-16-148410-0")
    assert checker.input_string == "9783161484100"

def test_isbn_checker_no_normalize():
    checker = __ISBNChecker("978-3-16-148410-0", normalize=False)
    assert checker.input_string == "978-3-16-148410-0"

def test_isbn_13_valid():
    checker = __ISBNChecker("9783161484100")
    assert checker.is_isbn_13() == True

def test_isbn_13_invalid():
    checker = __ISBNChecker("9783161484101")
    assert checker.is_isbn_13() == False

def test_isbn_13_invalid_characters():
    checker = __ISBNChecker("97831614841A0")
    assert checker.is_isbn_13() == False

def test_isbn_10_valid():
    checker = __ISBNChecker("0306406152")
    assert checker.is_isbn_10() == True

def test_isbn_10_invalid():
    checker = __ISBNChecker("0306406153")
    assert checker.is_isbn_10() == False

def test_isbn_10_invalid_characters():
    checker = __ISBNChecker("03064061A2")
    assert checker.is_isbn_10() == False
